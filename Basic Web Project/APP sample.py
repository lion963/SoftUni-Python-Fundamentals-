from tkinter import *
from tkcalendar import DateEntry

def clear_view(tk):
    for s in tk.grid_slaves():
        s.destroy()

def render_create_task_view(tk):
    clear_view(tk)
    Label(tk, text='Enter your task name:').grid(row=0, column=0, padx=20, pady=20)
    Entry(tk).grid(row=0, column=1)
    Label(tk, text='Due date:').grid(row=1, column=0, padx=20, pady=20)


def render_main_view(tk):
    Button(tk, text='List tasks', bg='blue', fg='white').grid(row=0, column=0, padx=200, pady=200)
    Button(tk, text='Create task', bg='green', fg='white', command=lambda: render_create_task_view(tk)).grid(row=0, column=1, padx=100, pady=200)

tk = Tk()
tk.title('Wellcome to my first APP')
tk.geometry('900x700')
tk.configure(bg='pink')
render_main_view(tk)

tk.mainloop()