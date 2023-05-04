import constantes.rutas
import constantes.longitud_campos
import modelos.empleadores
from os.path import isfile, normpath, expanduser
import os
import json


def leer():
    empleadores_list=list()
    if not isfile(normpath(expanduser(constantes.rutas.BD_EMPLEADORES))):
        return empleadores_list
    with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'r') as ar:
        lista_dict_empleadores=json.loads(ar.read())
        for e_dict in lista_dict_empleadores:
            empleador=modelos.empleadores.Empleador()
            empleador.__dict__=e_dict
            empleadores_list.append(empleador)
    return empleadores_list


def escribir(empleadores_list):
    os.makedirs(os.path.split(constantes.rutas.BD_EMPLEADORES)[0],exist_ok=True)
    lista_dict=list()
    for e in empleadores_list:
        lista_dict.append(e.__dict__)
    with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'w') as ar:
        ar.write(json.dumps(lista_dict))
    return None;


def crear(empleador=modelos.empleadores.Empleador):
    lista_dict_empleadores=list()
    if isfile(normpath(expanduser(constantes.rutas.BD_EMPLEADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'r') as ar:
            lista_dict_empleadores=json.loads(ar.read())
    for e_dict in lista_dict_empleadores:
        e=modelos.empleadores.Empleador()
        e.__dict__=e_dict
        if empleador.cuit == e.cuit:
            return None
    lista_dict_empleadores.append(empleador.__dict__)
    os.makedirs(os.path.split(constantes.rutas.BD_EMPLEADORES)[0], exist_ok=True)
    with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'w') as ar:
        ar.write(json.dumps(lista_dict_empleadores))
    return None


def borrar(empleador = modelos.empleadores.Empleador):
    lista_dict_empleadores_leidos=list()
    lista_dict_empleadores_resultantes=list()
    if isfile(normpath(expanduser(constantes.rutas.BD_EMPLEADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'r') as ar:
            lista_dict_empleadores_leidos=json.loads(ar.read())
    for e_dict in lista_dict_empleadores_leidos:
        if e_dict != empleador.__dict__:
            lista_dict_empleadores_resultantes.append(e_dict)
    if isfile(normpath(expanduser(constantes.rutas.BD_EMPLEADORES))):
        with open(normpath(expanduser(constantes.rutas.BD_EMPLEADORES)), 'w') as ar:
            ar.write(json.dumps(lista_dict_empleadores_resultantes))
    return None
