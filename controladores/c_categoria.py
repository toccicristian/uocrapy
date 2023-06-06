import repositorios.tabla_categorias

def lista_por_nombre():
    return [categoria.nombre for categoria in repositorios.tabla_categorias.cargar()]

def default_nombre(orden=0):
    return [categoria for categoria in repositorios.tabla_categorias.cargar()][orden].nombre

def codigo_de(nombre=str()):
    return repositorios.tabla_categorias.busca_por_nombre(nombre).codigo

def nombre_de(codigo=str()):
    return repositorios.tabla_categorias.busca_por_codigo(codigo).nombre
