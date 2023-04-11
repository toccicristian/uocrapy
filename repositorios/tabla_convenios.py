import constantes.rutas
import modelos.convenios
import constantes.longitud_campos as long_campos
from os.path import isfile, normpath, expanduser


def cargar():
    convenios=list()
    with open(normpath(expanduser(constantes.rutas.TABLA_CONVENIOS)), 'r') as ar:
        for l in ar.readlines():
            convenio=modelos.convenios.Convenio(codigo=l.split(':')[0].zfill(long_campos.CONVENIO),nombre=l.split(':')[1])
            convenios.append(convenio)

    return convenios
