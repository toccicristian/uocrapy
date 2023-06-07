import repositorios.tabla_convenios


def lista_por_nombre():
    return [convenio.nombre for convenio in repositorios.tabla_convenios.cargar()]

def default_nombre(orden=0):
    return [convenio for convenio in repositorios.tabla_convenios.cargar()][orden].nombre

def codigo_de(nombre=str()):
    return repositorios.tabla_convenios.busca_por_nombre(nombre).codigo

def nombre_de(codigo=str()):
    return repositorios.tabla_convenios.busca_por_codigo(codigo).nombre
