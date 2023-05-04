class Empleador:
    def __init__ (self, cuit="00000000000",nombre=""):
        self._cuit=cuit
        self._nombre=nombre

    @property
    def cuit (self):
        return self._cuit

    @cuit.setter
    def cuit (self, cuit):
        self._cuit=cuit

    @property
    def nombre (self):
        return self._nombre

    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"{self._cuit};{self._nombre}"
