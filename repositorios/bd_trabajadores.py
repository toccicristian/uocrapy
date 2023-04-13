import constantes.rutas
import constantes.longitud_campos
import modelos.trabajadores
from os.path import isfile, normpath, expanduser
import json

def leer():
    trabajadores_list=list()
    if not isfile(normpath(expanduser(constantes.rutas.BD_TRABAJADORES))):
        return trabajadores_list
    with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'r') as ar:
        lista_dict_trabajadores=json.loads(ar.read())
        for t_dict in lista_dict_trabajadores:
            trabajador=modelos.trabajadores.Trabajador()
            trabajador.__dict__=t_dict
            trabajadores_list.append(trabajador)
    return trabajadores_list


def escribir(trabajadores_list):
    with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'w') as ar:
        lista_dict=list()
        for t in trabajadores_list:
            lista_dict.append(t.__dict__)
        ar.write(json.dumps(lista_dict))
    return None


def crear(trabajador=modelos.trabajadores.Trabajador):
    lista_dict_trabajadores=list()
    if isfile(normpath(expanduser(constantes.rutas.BD_TRABAJADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'r') as ar:
            lista_dict_trabajadores=json.loads(ar.read())
    for t_dict in lista_dict_trabajadores:
        t=modelos.trabajadores.Trabajador()
        t.__dict__=t_dict
        if trabajador.cuil == t.cuil and trabajador.cuit_empleador == t.cuit_empleador:
            return None
    lista_dict_trabajadores.append(trabajador.__dict__)
    with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'w') as ar:
        ar.write(json.dumps(lista_dict_trabajadores))
    return None


def borrar(trabajador=modelos.trabajadores.Trabajador):
    lista_dict_trabajadores_leidos=list()
    lista_dict_trabajadores_resultantes=list()
    if isfile(normpath(expanduser(constantes.rutas.BD_TRABAJADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'r') as ar:
            lista_dict_trabajadores_leidos=json.loads(ar.read())
    for t_dict in lista_dict_trabajadores_leidos:
        if t_dict != trabajador.__dict__:
            lista_dict_trabajadores_resultantes.append(t_dict)
    if isfile(normpath(expanduser(constantes.rutas.BD_TRABAJADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_TRABAJADORES)),'w') as ar:
            ar.write(json.dumps(lista_dict_trabajadores_resultantes))
    return None
