class Empleador:
    def __init__ (self, cuit="00000000000",nombre=""):
        self.__cuit=cuit
        self.__nombre=nombre

    @property
    def cuit (self):
        return self._Empleador__cuit

    @cuit.setter
    def cuit (self, cuit):
        self._Empleador__cuit=cuit

    @property
    def nombre (self):
        return self._Empleador__nombre

    @nombre.setter
    def nombre (self, nombre):
        self._Empleador__nombre = nombre

    def __str__(self):
        return f"{self.__cuit};{self.__nombre}"
