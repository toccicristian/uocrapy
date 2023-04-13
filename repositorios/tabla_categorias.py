import constantes.rutas
import modelos.categorias
import constantes.longitud_campos as long_campos
from os.path import isfile, normpath, expanduser


def cargar():
    categorias=list()
    with open(normpath(expanduser(constantes.rutas.TABLA_CATEGORIAS)), 'r') as ar:
        for l in ar.readlines():
            categoria=modelos.categorias.Categoria(codigo=l.split(':')[0].zfill(long_campos.CATEGORIA),nombre=l.split(':')[1])
            categorias.append(categoria)

    return categorias


def busca_por_nombre(nombre=''):
    with open(normpath(expanduser(constantes.rutas.TABLA_CATEGORIAS)),'r') as ar:
        for l in ar.readlines():
            if len(l.split(':'))>1 and l.split(':')[1].rstrip() == nombre:
                categoria=modelos.categorias.Categoria(codigo=l.zfill(long_campos.CATEGORIA),nombre=nombre)
                return categoria
    categoria=modelos.categorias.Categoria(codigo='',nombre='')
    return categoria

        #categoria=modelos.categorias.Categoria(codigo=([l.rstrip() for l in ar.readlines() if len(l.split(':'))>1 and l.split(':')[1].rstrip() == nombre][0:1] or ('',))[0],nombre=nombre)
