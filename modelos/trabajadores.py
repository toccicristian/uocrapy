class Trabajador:
    def __init__ (self, nombre='', cuit_empleador='00000000000',cuil='00000000000', afiliado=False, rem_cuota_sind='00000000', rem_cese_laboral='00000000', ingreso='00000000',codigo_postal='0000',convenio='00', categoria='00',administracion_publica=False, exportar=False):
        self._nombre=nombre
        self._cuit_empleador=cuit_empleador
        self._cuil=cuil
        self._rem_cuota_sind=rem_cuota_sind
        self._rem_cese_laboral=rem_cese_laboral
        self._ingreso=ingreso
        self._codigo_postal=codigo_postal
        self._convenio=convenio
        self._categoria=categoria
        self._afiliado=afiliado
        self._administracion_publica=administracion_publica
        self._exportar=exportar

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre=str()):
        self._nombre=nombre

    @property
    def cuit_empleador (self):
        return self._cuit_empleador

    @cuit_empleador.setter
    def cuit_empleador (self, cuit_empleador=str()):
        self._cuit_empleador=cuit_empleador

    @property
    def cuil (self):
        return self._cuil

    @cuil.setter
    def cuil (self, cuil=str()):
        self._cuil=cuil

    @property
    def rem_cuota_sind (self):
        return self._rem_cuota_sind

    @rem_cuota_sind.setter
    def rem_cuota_sind (self, rem_cuota_sind=str()):
        self._rem_cuota_sind=rem_cuota_sind

    @property
    def rem_cese_laboral (self):
        return self._rem_cese_laboral

    @rem_cese_laboral.setter
    def rem_cese_laboral (self, rem_cese_laboral=str()):
        self._rem_cese_laboral=rem_cese_laboral

    @property
    def ingreso (self):
        return self._ingreso

    @ingreso.setter
    def ingreso (self, ingreso=str()):
        self._ingreso=ingreso

    @property
    def codigo_postal (self):
        return self._codigo_postal

    @codigo_postal.setter
    def codigo_postal (self, codigo_postal=str()):
        self._codigo_postal=codigo_postal

    @property
    def convenio (self):
        return self._convenio

    @convenio.setter
    def convenio (self, convenio=str()):
        self._convenio=convenio

    @property
    def categoria (self):
        return self._categoria

    @categoria.setter
    def categoria (self, categoria=str()):
        self._categoria=categoria

    @property
    def afiliado (self):
        return self._afiliado

    @afiliado.setter
    def afiliado (self, afiliado=True):
        self._afiliado=afiliado

    @property
    def administracion_publica (self):
        return self._administracion_publica

    @administracion_publica.setter
    def administracion_publica (self, administracion_publica=True):
        self._administracion_publica=administracion_publica

    @property
    def exportar(self):
        return self._exportar

    @exportar.setter
    def exportar (self, exportar=True):
        self._exportar=exportar
