import tkinter as tk

class Campo:
    def __init__ (self, master, texto_label=str(),
                  ancho_label=int(), ancho_campo=int(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0), nombre=""):
        self._master=master
        self._texto_label=texto_label
        self._ancho_label=ancho_label
        self._ancho_campo=ancho_campo
        self._packside=packside
        self._packanchor=packanchor
        self._padx=padx
        self._pady=pady
        self._frame=tk.Frame(self._master)
        self._label=tk.Label(self._frame, text=self._texto_label, width=self._ancho_label, anchor=tk.W)
        self._entry = tk.Entry(self._frame, width=self._ancho_campo)
        self._nombre=nombre

    @property
    def text(self):
        return self._entry.get()

    @text.setter
    def text(self, text=str()):
        self._entry.delete(0, tk.END)
        self._entry.insert(0, text)
        return None

    @property
    def nombre(self):
        return self._nombre

    def pack(self):
        self._frame.pack(side=self._packside, anchor=self._packanchor, padx=self._padx, pady=self._pady)
        self._label.pack(side=tk.LEFT)
        self._entry.pack(side=tk.LEFT)

    def focus_set(self):
        self._entry.focus_set()

    def bind(self, secuencia, funcion):
        self._entry.bind(secuencia, funcion)

    def disable(self):
        self._entry.configure(state=tk.DISABLED)

    def enable(self):
        self._entry.configure(state=tk.NORMAL)
