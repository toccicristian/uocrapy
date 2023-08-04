import tkinter as tk

class Mensaje:
    def __init__(self, toplevel, mensaje="", width="250", height="100", titulo="Atencion!"):
        self.__v=tk.Toplevel(toplevel)
        self.__v.geometry(f"{width}x{height}")
        self.__v.title(titulo)
        self.__l=tk.Label(self.__v, text=mensaje)
        self.__b=tk.Button(self.__v, text="Aceptar", height=1, width=10, command = lambda : self.__v.destroy())
        self.__b.focus_set()
        self.__b.bind("<Return>", lambda event : self.__v.destroy())
        self.__l.pack(pady=(10,10))
        self.__b.pack()
