import tkinter as tk

class Mensaje:
    def __init__(self, toplevel, mensaje="", width="250", height="100", titulo="Atencion!"):
        self._v=tk.Toplevel(toplevel)
        self._v.geometry(f"{width}x{height}")
        self._v.title(titulo)
        self._l=tk.Label(self._v, text=mensaje)
        self._b=tk.Button(self._v, text="Aceptar", height=1, width=10, command = lambda : self._v.destroy())
        self._b.focus_set()
        self._b.bind("<Return>", lambda event : self._v.destroy())
        self._l.pack(pady=(10,10))
        self._b.pack()
