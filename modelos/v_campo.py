import tkinter as tk

class Campo:
    def __init__ (self, master, texto_label=str(),
                  ancho_label=int(), ancho_campo=int(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0)):
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
        #self._text=tk.Text(self._frame, height=1, width=self._ancho_campo)

    @property
    def text(self):
        return self._entry.get()

    def pack(self):
        self._frame.pack(side=self._packside, anchor=self._packanchor, padx=self._padx, pady=self._pady)
        self._label.pack(side=tk.LEFT)
        self._entry.pack(side=tk.LEFT)

    def focus_set(self):
        self._entry.focus_set()

    def bind(self, secuencia, funcion):
        self._entry.bind(secuencia, funcion)

    def disable(self):
        self._entry.config(state=tk.DISABLED)

    def enable(self):
        self._entry.config(state=tk.NORMAL)
