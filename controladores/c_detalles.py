import repositorios.bd_trabajadores
import repositorios.tabla_convenios
import repositorios.tabla_categorias
import controladores.c_trabajadores
import controladores.c_categoria as c_categoria
import controladores.c_convenio as c_convenio
import modelos.trabajadores
import modelos.v_mensaje
import utiles.cuit
import utiles.fechas
import utiles.montos

def busca_campo(lista_campos, nombre=str()):
    for campo in lista_campos:
        if f'{campo.nombre}' == f'{nombre}':
            return campo


def guardar_cambios(v, tview_empleadores, lista_campos, tview_empleados):
    errores=''
    if len(busca_campo(lista_campos,nombre="nombre").text)==0:
        errores+='Falta nombre de trabajador\n'

    if not utiles.cuit.escuil(busca_campo(lista_campos, nombre="cuil").text):
        errores+='El CUIL no es válido\n'

    if not utiles.montos.validar(str((busca_campo(lista_campos, nombre="remcuota").text)).replace(",",".")):
        errores+="La remuneracion cuota sindical debe ser un número\n"

    if not utiles.montos.validar(str((busca_campo(lista_campos, nombre="remcese").text)).replace(",",".")):
        errores+="La remuneracion de cese laboral debe ser un número\n"

    if not utiles.fechas.valida(busca_campo(lista_campos, nombre="ingreso").text):
        errores+='La fecha no es válida\n'

    if len(busca_campo(lista_campos, nombre="codpostal").text)!=4:
        errores+='El Codigo Postal no es válido.'

    if len(errores)>0:
        modelos.v_mensaje.Mensaje(v, f"{errores}", width="350")
        return False

    trabajador = modelos.trabajadores.Trabajador(nombre = busca_campo(lista_campos,nombre="nombre").text,
                                                 cuit_empleador = tview_empleadores.item(tview_empleadores.focus())['values'][1],
                                                 cuil = busca_campo(lista_campos, nombre="cuil").text,
                                                 rem_cuota_sind = f'{round(float(busca_campo(lista_campos, nombre="remcuota").text.replace(",",".")),2):.2f}',
                                                 rem_cese_laboral = f'{round(float(busca_campo(lista_campos, nombre="remcese").text.replace(",",".")),2):.2f}',
                                                 ingreso = busca_campo(lista_campos, nombre="ingreso").text,
                                                 codigo_postal = busca_campo(lista_campos, nombre="codpostal").text,
                                                 convenio = c_convenio.codigo_de(
                                                     busca_campo(lista_campos, nombre="convenio").text),
                                                 categoria = c_categoria.codigo_de(
                                                     busca_campo(lista_campos, nombre="categoria").text),
                                                 administracion_publica = busca_campo(lista_campos, nombre="adminpublica").tildada,
                                                 afiliado = busca_campo(lista_campos, nombre="afiliado").tildada,
                                                 exportar = busca_campo(lista_campos, nombre="exportar").tildada)

    for t in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(trabajador.cuit_empleador):
        if f'{t.cuil}' == f'{trabajador.cuil}':
            repositorios.bd_trabajadores.borrar(t)
            repositorios.bd_trabajadores.crear(trabajador)
            controladores.c_trabajadores.actualiza_tview(tview_empleados, tview_empleadores)
            modelos.v_mensaje.Mensaje(v, f"Se actualizó el trabajador \n{trabajador.nombre}", width="450")
            return True

    repositorios.bd_trabajadores.crear(trabajador)
    controladores.c_trabajadores.actualiza_tview(tview_empleados, tview_empleadores)
    modelos.v_mensaje.Mensaje(v, f"Se creó el trabajador \n{trabajador.nombre}", width="450")
    return True
