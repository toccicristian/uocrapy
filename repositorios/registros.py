from os.path import normpath, expanduser, isdir
import os.path

def grabar(registros=None, url_destino):
    if registros is None:
        registros = list()
    if not isdir (os.path.split(normpath(expanduser(url_destino)))[0]):
        return False

    with open(url_destino,'w') as ar:
        ar.writelines(registros)

    return True

