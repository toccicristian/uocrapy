import constantes.rutas
import modelos.convenios
import constantes.longitud_campos as long_campos
from os.path import isfile, normpath, expanduser


def cargar():
    convenios=list()
    with open(normpath(expanduser(constantes.rutas.TABLA_CONVENIOS)), 'r') as ar:
        for l in ar.readlines():
            convenio=modelos.convenios.Convenio(codigo=l.split(':')[0].zfill(long_campos.CONVENIO),nombre=l.split(':')[1].rstrip())
            convenios.append(convenio)

    return convenios


def busca_por_nombre(nombre=''):
    with open(normpath(expanduser(constantes.rutas.TABLA_CONVENIOS)),'r') as ar:
        for l in ar.readlines():
            if len(l.split(':'))>1 and l.split(':')[1].rstrip() == nombre:
                convenio=modelos.convenios.Convenio(codigo=l.zfill(long_campos.CONVENIO), nombre=nombre)
                return convenio
    convenio=modelos.convenios.Convenio(codigo='', nombre='')
    return convenio


def busca_por_codigo(codigo=''):
    with open(normpath(expanduser(constantes.rutas.TABLA_CONVENIOS)), 'r') as ar:
        for l in ar.readlines():
            if len(l.split(':'))>1 and l.split(':')[0].rstrip() == codigo:
                convenio=modelos.convenios.Convenio(codigo=l.zfill(long_campos.CONVENIO), nombre=l.split(':')[1].rstrip())
                return convenio
    convenio=modelos.convenios.Convenio(codigo='', nombre='')
    return convenio

