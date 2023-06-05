#!/usr/bin/python3


import constantes.rutas
import constantes.longitud_campos
import modelos.trabajadores
import modelos.empleadores
import repositorios.bd_trabajadores
import repositorios.bd_empleadores
import repositorios.tabla_categorias
import repositorios.tabla_convenios
import vistas.vista_principal

def repositorios_bd_trabajadores_test():
  t_nuevo = modelos.trabajadores.Trabajador()

  estado="ERROR"
  cant_trabajadores=0
  print("Creando trabajador... ",end="")
  repositorios.bd_trabajadores.crear(trabajador = t_nuevo)
  print("trabajadores con trabajador creado... ",end="")
  for t_leido in repositorios.bd_trabajadores.leer():
    if (t_leido.__dict__ == t_nuevo.__dict__):
      estado="OK"
  print(f"[{estado}]")
  print("borrando trabajador... ",end="")
  repositorios.bd_trabajadores.borrar(t_nuevo)
  for t_leido in repositorios.bd_trabajadores.leer():
    if(t_leido.__dict__ == t_nuevo.__dict__):
      cant_trabajadores+=1
  print(f"Veces que ocurre trabajador :{cant_trabajadores}")

  estado="ERROR"
  cant_trabajadores=0
  print("Leyendo lista de trabajadores...")
  trabajadores = repositorios.bd_trabajadores.leer()
  print("Creando nuevo trabajador y agregandolo a la lista...")
  t_nuevo2 = modelos.trabajadores.Trabajador(cuil='11111111111',cuit_empleador='11111111111')
  trabajadores.append(t_nuevo2)
  print("escribiendo lista de trabajadores a la base de datos... ",end="")
  repositorios.bd_trabajadores.escribir(trabajadores_list=trabajadores)
  for t_leido in repositorios.bd_trabajadores.leer():
    if(t_leido.__dict__ == t_nuevo2.__dict__):
      estado="OK"
  print(f"[{estado}]")
  print("borrando trabajador de prueba...",end="")
  repositorios.bd_trabajadores.borrar(t_nuevo2)
  for t_leido in repositorios.bd_trabajadores.leer():
    if(t_leido.__dict__ == t_nuevo2.__dict__):
      cant_trabajadores+=1
  print(f"Veces que ocurre el trabajador :{cant_trabajadores}")

  print("=====================================================")


def repositorios_bd_empleadores_test():
  empleador_prueba = modelos.empleadores.Empleador (cuit = '20000000000', nombre = 'Nombre de Prueba')

  print(f"Creando empleador {empleador_prueba.nombre} con cuit {empleador_prueba.cuit}... ")
  repositorios.bd_empleadores.crear(empleador_prueba)

  estado="ERROR"
  print(f"Leyendo el empleador en la base de datos... ",end="")
  for e in repositorios.bd_empleadores.leer():
    if e.__dict__ == empleador_prueba.__dict__:
      estado="OK"
  print(f"[{estado}]")

  estado="OK"
  print(f"Borrando empleador {empleador_prueba.nombre} con cuit {empleador_prueba.cuit}... ")
  repositorios.bd_empleadores.borrar(empleador_prueba)
  print(f"Comprobando si fue eliminado de la base de datos... ",end="")
  for e in repositorios.bd_empleadores.leer():
    if e.__dict__ == empleador_prueba.__dict__:
      estado="ERROR"
  print(f"[{estado}]")

  estado="ERROR"
  print("Abriendo la base de datos...")
  bd=repositorios.bd_empleadores.leer()
  print("Añadiendo empleador a la lista...")
  bd.append(empleador_prueba)
  print("Actualizando la base de datos...")
  repositorios.bd_empleadores.escribir(bd)
  print("Comprobando si el cambio se realizó... ",end="")
  for e in repositorios.bd_empleadores.leer():
    if e.__dict__ == empleador_prueba.__dict__:
      estado="OK"
  print(f"[{estado}]")

  estado='OK'
  print("Eliminando de la base de datos... ",end="")
  repositorios.bd_empleadores.borrar(empleador_prueba)
  for e in repositorios.bd_empleadores.leer():
    if e.__dict__ == empleador_prueba.__dict__:
      estado="ERROR"
  print(f"[{estado}]")

  print("=====================================================")


def vista_principal_test():
    vistas.vista_principal.mostrar()

repositorios_bd_trabajadores_test()
repositorios_bd_empleadores_test()
vista_principal_test()

