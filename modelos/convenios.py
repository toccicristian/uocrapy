class Convenio:
    def __init__ (self, codigo=str(), nombre=str()):
        self.__codigo=codigo
        self.__nombre=nombre

    @property
    def codigo (self):
        return self._Convenio__codigo

    @property
    def nombre (self):
        return self._Convenio__nombre
