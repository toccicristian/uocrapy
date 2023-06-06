import tkinter as tk

class ListaDesplegable:
    def __init__ (self, toplevel, texto_label=str(), ancho_label=int(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0),
                  nombre="", opcion_default='', lista_opciones=None):
        if lista_opciones is None:
            lista_opciones=list()
        self._toplevel=toplevel
        self._texto_label=texto_label
        self._ancho_label=ancho_label
        self._packside=packside
        self._packanchor=packanchor
        self._padx=padx
        self._pady=pady
        self._frame=tk.Frame(toplevel)
        self._label=tk.Label(self._frame, text=self._texto_label, width=self._ancho_label, anchor=tk.W)
        self._nombre=nombre
        self._opcion_seleccionada=tk.StringVar(self._frame)
        self._opcion_seleccionada.set(opcion_default)
        self._lista_opciones=lista_opciones
        self._dropdown = tk.OptionMenu(self._frame, self._opcion_seleccionada, *self._lista_opciones)

    @property
    def opcion_seleccionada(self):
        return self._opcion_seleccionada.get()

    @property
    def text(self):
        return self._opcion_seleccionada.get()

    @property
    def nombre(self):
        return self._nombre

    def pack(self):
        self._frame.pack(side=self._packside, anchor=self._packanchor, padx=self._padx, pady=self._pady)
        self._label.pack(side=tk.LEFT)
        self._dropdown.pack(side=tk.LEFT)

    def disable(self):
        self._dropdown.configure(state="disabled")

    def enable(self):
        self._dropdown.configure(state="normal")
