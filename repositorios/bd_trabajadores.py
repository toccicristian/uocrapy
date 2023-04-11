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

