import tkinter as tk

class Campo:
    def __init__ (self, master, texto_label=str(),
                  ancho_label=int(), ancho_campo=int(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0), nombre=""):
        self.__master=master
        self.__texto_label=texto_label
        self.__ancho_label=ancho_label
        self.__ancho_campo=ancho_campo
        self.__packside=packside
        self.__packanchor=packanchor
        self.__padx=padx
        self.__pady=pady
        self.__frame=tk.Frame(self.__master)
        self.__label=tk.Label(self.__frame, text=self.__texto_label, width=self.__ancho_label, anchor=tk.W)
        self.__entry = tk.Entry(self.__frame, width=self.__ancho_campo)
        self.__nombre=nombre

    @property
    def text(self):
        return self._Campo__entry.get()

    @text.setter
    def text(self, text=str()):
        self._Campo__entry.delete(0, tk.END)
        self._Campo__entry.insert(0, text)
        return None

    @property
    def nombre(self):
        return self._Campo__nombre

    def pack(self):
        self._Campo__frame.pack(side=self.__packside, anchor=self.__packanchor, padx=self.__padx, pady=self.__pady)
        self._Campo__label.pack(side=tk.LEFT)
        self._Campo__entry.pack(side=tk.LEFT)

    def focus_set(self):
        self._Campo__entry.focus_set()

    def bind(self, secuencia, funcion):
        self._Campo__entry.bind(secuencia, funcion)

    def disable(self):
        self._Campo__entry.configure(state=tk.DISABLED)

    def enable(self):
        self._Campo__entry.configure(state=tk.NORMAL)
