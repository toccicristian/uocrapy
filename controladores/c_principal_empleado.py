import repositorios.bd_trabajadores
import repositorios.tabla_convenios
import repositorios.tabla_categorias


def busca_campo(lista_campos, nombre=str()):
    for campo in lista_campos:
        if f'{campo.nombre}' == f'{nombre}':
            return campo


def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for trabajador in repositorios.bd_trabajadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(trabajador.nombre, trabajador.cuil))
        i+=1


def selecciona_trabajador(lista_campos, tview_empleados, tview_empleadores):
    if tview_empleados.item  (tview_empleados.focus()  )['values'] == '':
        return None

    trabajador=repositorios.bd_trabajadores.busca_por_cuil_trabajador_y_cuit_empleador(
        tview_empleados.item  (tview_empleados.focus()  )['values'][1],
        tview_empleadores.item(tview_empleadores.focus())['values'][1]
        )
    busca_campo(lista_campos,"nombre").text=trabajador.nombre
    busca_campo(lista_campos,"cuil").text=trabajador.cuil
    busca_campo(lista_campos,"remcuota").text=trabajador.rem_cuota_sind
    busca_campo(lista_campos,"remcese").text=trabajador.rem_cese_laboral
    busca_campo(lista_campos,"ingreso").text=trabajador.ingreso
    busca_campo(lista_campos,"codpostal").text=trabajador.codigo_postal
    busca_campo(lista_campos,"convenio").opcion_seleccionada=repositorios.tabla_convenios.busca_por_codigo(
        trabajador.convenio).nombre
    busca_campo(lista_campos,"categoria").opcion_seleccionada=repositorios.tabla_categorias.busca_por_codigo(
        trabajador.categoria).nombre
    busca_campo(lista_campos,"afiliado").tildada=trabajador.afiliado
    busca_campo(lista_campos,"adminpublica").tildada=trabajador.administracion_publica
    busca_campo(lista_campos,"exportar").tildada=trabajador.exportar
    return None



"""
def selecciona_empleador(lista_campos, tview_empleados, tview_empleadores, l_exportacion):
    for campo in lista_campos:
        campo.enable()
    if len(tview_empleadores.item(tview_empleadores.focus())['values']) == 0:
        for campo in lista_campos:
            campo.disable()
        l_exportacion.config(text="")
        return False

    l_exportacion.config(text=f"Exportando para :{tview_empleadores.item(tview_empleadores.focus())['values'][0]}")
    return None
"""
