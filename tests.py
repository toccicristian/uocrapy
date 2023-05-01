#!/usr/bin/python3


import constantes.rutas
import constantes.longitud_campos
import modelos.trabajadores
import repositorios.bd_trabajadores
import repositorios.tabla_categorias
import repositorios.tabla_convenios


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



repositorios_bd_trabajadores_test()
