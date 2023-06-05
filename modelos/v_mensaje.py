import tkinter as tk

class Mensaje:
    def __init__(self, toplevel, mensaje=""):
        v=tk.Toplevel(toplevel)
        v.geometry("250x100")
        l=tk.Label(v, text=mensaje)
        b=tk.Button(v, text="Aceptar", height=5, width=10, command = lambda : v.destroy())
        b.focus_set()
        b.bind("<Return>", lambda event : v.destroy())
        l.pack(pady=(10,10))
        b.pack()
