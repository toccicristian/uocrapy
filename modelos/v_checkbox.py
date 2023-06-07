import tkinter as tk

class Checkbox:
    def __init__ (self, toplevel, text=str(),
                  packside=tk.TOP, packanchor=tk.W, padx=(0,0), pady=(0,0), nombre=""):
        self._toplevel = toplevel
        self._text = text
        self._packside = packside
        self._packanchor = packanchor,
        self._padx = padx
        self._pady = pady
        self._frame = tk.Frame(self._toplevel)
        self._var = tk.IntVar()
        self._checkbox = tk.Checkbutton(self._frame, text=self._text,
                                        variable=self._var, onvalue=1, offvalue=0)
        self._nombre=nombre

    @property
    def tildada(self):
        if self._var.get() == 1:
            return True
        return False

    @property
    def nombre(self):
        return self._nombre

    @tildada.setter
    def tildada(self, status=True):
        if status:
            self._var.set(1)
            return None
        self._var.set(0)
        return None

    def pack (self):
        self._frame.pack(side=self._packside, anchor=self._packanchor, padx=self._padx, pady=self._pady)
        self._checkbox.pack(side=tk.LEFT)

    def disable(self):
        self._checkbox.config(state=tk.DISABLED)

    def enable(self):
        self._checkbox.config(state=tk.NORMAL)
