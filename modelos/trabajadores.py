class Trabajador:
    def __init__ (self, nombre='', cuit_empleador='00000000000',cuil='00000000000', afiliado=False, rem_cuota_sind='00000000', rem_cese_laboral='00000000', ingreso='00000000',codigo_postal='0000',convenio='00', categoria='00',administracion_publica=False, exportar=False):
        self.__nombre=nombre
        self.__cuit_empleador=cuit_empleador
        self.__cuil=cuil
        self.__rem_cuota_sind=rem_cuota_sind
        self.__rem_cese_laboral=rem_cese_laboral
        self.__ingreso=ingreso
        self.__codigo_postal=codigo_postal
        self.__convenio=convenio
        self.__categoria=categoria
        self.__afiliado=afiliado
        self.__administracion_publica=administracion_publica
        self.__exportar=exportar

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre=str()):
        self.__nombre=nombre

    @property
    def cuit_empleador (self):
        return self.__cuit_empleador

    @cuit_empleador.setter
    def cuit_empleador (self, cuit_empleador=str()):
        self.__cuit_empleador=cuit_empleador

    @property
    def cuil (self):
        return self.__cuil

    @cuil.setter
    def cuil (self, cuil=str()):
        self.__cuil=cuil

    @property
    def rem_cuota_sind (self):
        return self.__rem_cuota_sind

    @rem_cuota_sind.setter
    def rem_cuota_sind (self, rem_cuota_sind=str()):
        self.__rem_cuota_sind=rem_cuota_sind

    @property
    def rem_cese_laboral (self):
        return self.__rem_cese_laboral

    @rem_cese_laboral.setter
    def rem_cese_laboral (self, rem_cese_laboral=str()):
        self.__rem_cese_laboral=rem_cese_laboral

    @property
    def ingreso (self):
        return self.__ingreso

    @ingreso.setter
    def ingreso (self, ingreso=str()):
        self.__ingreso=ingreso

    @property
    def codigo_postal (self):
        return self.__codigo_postal

    @codigo_postal.setter
    def codigo_postal (self, codigo_postal=str()):
        self.__codigo_postal=codigo_postal

    @property
    def convenio (self):
        return self.__convenio

    @convenio.setter
    def convenio (self, convenio=str()):
        self.__convenio=convenio

    @property
    def categoria (self):
        return self.__categoria

    @categoria.setter
    def categoria (self, categoria=str()):
        self.__categoria=categoria

    @property
    def afiliado (self):
        return self.__afiliado

    @afiliado.setter
    def afiliado (self, afiliado=True):
        self.__afiliado=afiliado

    @property
    def administracion_publica (self):
        return self.__administracion_publica

    @administracion_publica.setter
    def administracion_publica (self, administracion_publica=True):
        self.__administracion_publica=administracion_publica

    @property
    def exportar(self):
        return self.__exportar

    @exportar.setter
    def exportar (self, exportar=True):
        self.__exportar=exportar
