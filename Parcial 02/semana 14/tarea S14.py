"""
Agenda personal con GUI en Tkinter
Archivo: agenda_tkinter.py
Descripción: Aplicación que permite agregar, ver y eliminar eventos/tareas.
Requisitos implementados:
 - Interfaz con Tkinter (Treeview para lista de eventos)
 - Campos de entrada para fecha, hora y descripción
 - Botones: Agregar Evento, Eliminar Evento Seleccionado, Salir
 - DatePicker: usa tkcalendar.DateEntry si está instalado; si no, cae a un DatePicker personalizado
 - Confirmación al eliminar (diálogo)
 - Organización con Frames
 - Persistencia sencilla en 'events.json' (opcional, automática)

Cómo ejecutar:
    python agenda_tkinter.py

Requiere: Python 3.8+ (tkinter ya incluido). Si quieres la mejor experiencia de DatePicker instala 'tkcalendar' con:
    pip install tkcalendar

"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import calendar

# Intentar usar tkcalendar si está disponible
try:
    from tkcalendar import DateEntry
    TKCALENDAR_AVAILABLE = True
except Exception:
    TKCALENDAR_AVAILABLE = False

DATA_FILE = 'events.json'

class CustomDateEntry(ttk.Frame):
    """Entry con botón que abre un calendario simple en Toplevel.
    Usamos calendar.monthcalendar para mostrar días y permitir seleccionar.
    """
    def __init__(self, master=None, date_format='%Y-%m-%d', **kwargs):
        super().__init__(master, **kwargs)
        self.date_format = date_format
        self.var = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.var, width=12)
        self.entry.grid(row=0, column=0, sticky='w')
        self.btn = ttk.Button(self, text='📅', width=3, command=self.open_calendar)
        self.btn.grid(row=0, column=1, padx=(4,0))

    def open_calendar(self):
        top = tk.Toplevel(self)
        top.transient(self)
        top.title('Seleccione fecha')
        today = datetime.today()
        year, month = today.year, today.month

        cal_frame = ttk.Frame(top)
        cal_frame.pack(padx=8, pady=8)

        header = ttk.Frame(cal_frame)
        header.grid(row=0, column=0, columnspan=7)

        month_var = tk.IntVar(value=month)
        year_var = tk.IntVar(value=year)

        def redraw():
            for w in cal_body.winfo_children():
                w.destroy()
            y = year_var.get()
            m = month_var.get()
            cal = calendar.monthcalendar(y, m)
            days = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
            for i, d in enumerate(days):
                ttk.Label(cal_body, text=d).grid(row=0, column=i, padx=2, pady=2)
            for r, week in enumerate(cal, start=1):
                for c, day in enumerate(week):
                    if day == 0:
                        ttk.Label(cal_body, text='').grid(row=r, column=c, padx=2, pady=2)
                    else:
                        btn = ttk.Button(cal_body, text=str(day), width=3,
                                         command=lambda d=day, m=m, y=y: pick(d, m, y))
                        btn.grid(row=r, column=c, padx=1, pady=1)

        def prev_month():
            m = month_var.get() - 1
            y = year_var.get()
            if m < 1:
                m = 12
                y -= 1
            month_var.set(m)
            year_var.set(y)
            redraw()

        def next_month():
            m = month_var.get() + 1
            y = year_var.get()
            if m > 12:
                m = 1
                y += 1
            month_var.set(m)
            year_var.set(y)
            redraw()

        def pick(day, month, year):
            dt = datetime(year, month, day)
            self.var.set(dt.strftime(self.date_format))
            top.destroy()

        btn_prev = ttk.Button(header, text='<', width=3, command=prev_month)
        btn_prev.grid(row=0, column=0, padx=2)
        lbl_month = ttk.Label(header, textvariable=month_var)
        lbl_month.grid(row=0, column=1)
        lbl_slash = ttk.Label(header, text='/')
        lbl_slash.grid(row=0, column=2)
        lbl_year = ttk.Label(header, textvariable=year_var)
        lbl_year.grid(row=0, column=3)
        btn_next = ttk.Button(header, text='>', width=3, command=next_month)
        btn_next.grid(row=0, column=4, padx=2)

        cal_body = ttk.Frame(cal_frame)
        cal_body.grid(row=1, column=0)

        redraw()

    def get(self):
        return self.var.get().strip()

    def set(self, val):
        self.var.set(val)


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Agenda Personal')
        self.root.geometry('700x420')
        self.events = []

        # --- Frames ---
        top_frame = ttk.Frame(root, padding=8)
        top_frame.pack(fill='both', expand=True)

        left_frame = ttk.Frame(top_frame)
        left_frame.pack(side='left', fill='both', expand=True)

        right_frame = ttk.Frame(top_frame, width=260)
        right_frame.pack(side='right', fill='y')

        # --- Treeview (lista de eventos) ---
        tree_frame = ttk.Frame(left_frame)
        tree_frame.pack(fill='both', expand=True)

        columns = ('date', 'time', 'desc')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings', selectmode='browse')
        self.tree.heading('date', text='Fecha')
        self.tree.column('date', width=100, anchor='center')
        self.tree.heading('time', text='Hora')
        self.tree.column('time', width=80, anchor='center')
        self.tree.heading('desc', text='Descripción')
        self.tree.column('desc', width=380, anchor='w')

        vsb = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')

        # --- Input area ---
        entry_frame = ttk.LabelFrame(right_frame, text='Agregar / Editar evento', padding=8)
        entry_frame.pack(fill='both', padx=6, pady=6)

        # Date input
        ttk.Label(entry_frame, text='Fecha:').grid(row=0, column=0, sticky='w')
        if TKCALENDAR_AVAILABLE:
            self.date_entry = DateEntry(entry_frame, date_pattern='yyyy-mm-dd')
        else:
            self.date_entry = CustomDateEntry(entry_frame)
        self.date_entry.grid(row=0, column=1, pady=4, sticky='w')

        # Time input
        ttk.Label(entry_frame, text='Hora (HH:MM):').grid(row=1, column=0, sticky='w')
        self.time_var = tk.StringVar()
        self.time_entry = ttk.Entry(entry_frame, textvariable=self.time_var, width=12)
        self.time_entry.grid(row=1, column=1, pady=4, sticky='w')

        # Description
        ttk.Label(entry_frame, text='Descripción:').grid(row=2, column=0, sticky='nw')
        self.desc_text = tk.Text(entry_frame, width=28, height=6)
        self.desc_text.grid(row=2, column=1, pady=4, sticky='w')

        # Buttons
        btn_frame = ttk.Frame(right_frame)
        btn_frame.pack(fill='x', padx=6, pady=(0,6))

        add_btn = ttk.Button(btn_frame, text='Agregar Evento', command=self.add_event)
        add_btn.pack(fill='x', pady=4)

        del_btn = ttk.Button(btn_frame, text='Eliminar Evento Seleccionado', command=self.delete_selected)
        del_btn.pack(fill='x', pady=4)

        exit_btn = ttk.Button(btn_frame, text='Salir', command=self.on_exit)
        exit_btn.pack(fill='x', pady=4)

        # Load stored events si existen
        self.load_events()
        self.refresh_tree()

        # Doble click para editar (opcional simple)
        self.tree.bind('<Double-1>', self.on_tree_double_click)

    def validate_time(self, t_str):
        try:
            datetime.strptime(t_str, '%H:%M')
            return True
        except Exception:
            return False

    def add_event(self):
        # obtener datos
        if TKCALENDAR_AVAILABLE:
            date_str = self.date_entry.get_date().strftime('%Y-%m-%d')
        else:
            date_str = self.date_entry.get()
        time_str = self.time_var.get().strip()
        desc = self.desc_text.get('1.0', 'end').strip()

        # validaciones
        if not date_str:
            messagebox.showwarning('Validación', 'Ingrese una fecha.')
            return
        if not time_str:
            messagebox.showwarning('Validación', 'Ingrese la hora (HH:MM).')
            return
        if not self.validate_time(time_str):
            messagebox.showwarning('Validación', 'Hora inválida. Use formato HH:MM (24h).')
            return
        if not desc:
            messagebox.showwarning('Validación', 'Ingrese una descripción.')
            return

        # crear evento
        event = {
            'id': datetime.now().timestamp(),
            'date': date_str,
            'time': time_str,
            'desc': desc
        }
        self.events.append(event)
        self.events.sort(key=lambda e: (e['date'], e['time']))
        self.save_events()
        self.refresh_tree()
        # limpiar campos
        if TKCALENDAR_AVAILABLE:
            # DateEntry tiene su propio manejo; no seteamos nada
            pass
        else:
            self.date_entry.set('')
        self.time_var.set('')
        self.desc_text.delete('1.0', 'end')

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for ev in self.events:
            self.tree.insert('', 'end', iid=str(ev['id']), values=(ev['date'], ev['time'], ev['desc']))

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo('Eliminar', 'No hay ningún evento seleccionado.')
            return
        iid = sel[0]
        # confirmación
        if not messagebox.askyesno('Confirmar', '¿Eliminar el evento seleccionado?'):
            return
        # eliminar
        self.events = [e for e in self.events if str(e['id']) != iid]
        self.save_events()
        self.refresh_tree()

    def on_tree_double_click(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        ev = next((e for e in self.events if str(e['id']) == iid), None)
        if not ev:
            return
        # Cargar en inputs para posible edición
        if TKCALENDAR_AVAILABLE:
            try:
                self.date_entry.set_date(datetime.strptime(ev['date'], '%Y-%m-%d'))
            except Exception:
                pass
        else:
            self.date_entry.set(ev['date'])
        self.time_var.set(ev['time'])
        self.desc_text.delete('1.0', 'end')
        self.desc_text.insert('1.0', ev['desc'])

        # Preguntar si el usuario quiere eliminar o actualizar
        r = messagebox.askquestion('Acción', '¿Desea eliminar este evento? (Si) - Para editar, presione No y haga los cambios y luego "Agregar Evento" (creará una copia).')
        if r == 'yes':
            self.events = [e for e in self.events if str(e['id']) != iid]
            self.save_events()
            self.refresh_tree()

    def save_events(self):
        try:
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.events, f, ensure_ascii=False, indent=2)
        except Exception as ex:
            messagebox.showerror('Error', f'Error guardando eventos: {ex}')

    def load_events(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    self.events = json.load(f)
            except Exception:
                self.events = []
        else:
            self.events = []

    def on_exit(self):
        self.root.quit()


if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style(root)
    try:
        style.theme_use('clam')
    except Exception:
        pass
    app = AgendaApp(root)
    root.mainloop()
