class Trabajador:
    def __init__ (self, cuit_empleador='00000000000',cuil='00000000000', afiliado='N', rem_cuota_sind='00000000', rem_cese_laboral='00000000', ingreso='00000000',codigo_postal='0000',convenio='00', categoria='00',administracion_publica='N'):
        self._cuit_empleador=cuit_empleador
        self._cuil=cuil
        self._afiliado=afiliado
        self._rem_cuota_sind=rem_cuota_sind
        self._rem_cese_laboral=rem_cese_laboral
        self._ingreso=ingreso
        self._codigo_postal=codigo_postal
        self._convenio=convenio
        self._categoria=categoria
        self._administracion_publica=administracion_publica

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
    def afiliado (self):
        return self._afiliado

    @afiliado.setter
    def afiliado (self, afiliado=str()):
        self._afiliado=afiliado

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
    def administracion_publica (self):
        return self._administracion_publica

    @administracion_publica.setter
    def administracion_publica (self, administracion_publica=str()):
        self._administracion_publica=administracion_publica
