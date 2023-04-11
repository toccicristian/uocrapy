class Convenio:
    def __init__ (self, codigo=str(), nombre=str()):
        self._codigo=codigo
        self._nombre=nombre

    @property
    def codigo (self):
        return self._codigo

    @property
    def nombre (self):
        return self._nombre
