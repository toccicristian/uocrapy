import tkinter as tk

class ListaDesplegable:
    def __init__ (self, toplevel, texto_label=str(), ancho_label=int(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0),
                  nombre="", opcion_default='', lista_opciones=None):
        if lista_opciones is None:
            lista_opciones=list()
        self.__toplevel=toplevel
        self.__texto_label=texto_label
        self.__ancho_label=ancho_label
        self.__packside=packside
        self.__packanchor=packanchor
        self.__padx=padx
        self.__pady=pady
        self.__frame=tk.Frame(toplevel)
        self.__label=tk.Label(self.__frame, text=self.__texto_label, width=self.__ancho_label, anchor=tk.W)
        self.__nombre=nombre
        self.__opcion_seleccionada=tk.StringVar(self.__frame)
        self.__opcion_seleccionada.set(opcion_default)
        self.__lista_opciones=lista_opciones
        self.__dropdown = tk.OptionMenu(self.__frame, self.__opcion_seleccionada, *self.__lista_opciones)

    @property
    def opcion_seleccionada(self):
        return self.__opcion_seleccionada.get()

    @opcion_seleccionada.setter
    def opcion_seleccionada(self, opcion):
        self.__opcion_seleccionada.set(opcion)

    @property
    def text(self):
        return self.__opcion_seleccionada.get()

    @property
    def nombre(self):
        return self.__nombre

    def pack(self):
        self.__frame.pack(side=self.__packside, anchor=self.__packanchor, padx=self.__padx, pady=self.__pady)
        self.__label.pack(side=tk.LEFT)
        self.__dropdown.pack(side=tk.LEFT)

    def disable(self):
        self.__dropdown.configure(state="disabled")

    def enable(self):
        self.__dropdown.configure(state="normal")
