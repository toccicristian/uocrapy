import tkinter as tk

class Checkbox:
    def __init__ (self, toplevel, text=str(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0), nombre=""):
        self.__toplevel = toplevel
        self.__text = text
        self.__packside = packside
        self.__packanchor = packanchor,
        self.__padx = padx
        self.__pady = pady
        self.__frame = tk.Frame(self.__toplevel)
        self.__var = tk.IntVar()
        self.__checkbox = tk.Checkbutton(self.__frame, text=self.__text,
                                        variable=self.__var, onvalue=1, offvalue=0)
        self.__nombre=nombre

    @property
    def tildada(self):
        if self._Checkbox__var.get() == 1:
            return True
        return False

    @property
    def nombre(self):
        return self._Checkbox__nombre

    @tildada.setter
    def tildada(self, status=True):
        if status:
            self._Checkbox__var.set(1)
            return None
        self._Checkbox__var.set(0)
        return None

    def pack (self):
        self._Checkbox__frame.pack(side=self._Checkbox__packside, anchor=self._Checkbox__packanchor, padx=self._Checkbox__padx, pady=self._Checkbox__pady)
        self._Checkbox__checkbox.pack(side=tk.LEFT)

    def disable(self):
        self._Checkbox__checkbox.config(state=tk.DISABLED)

    def enable(self):
        self._Checkbox__checkbox.config(state=tk.NORMAL)
