import vistas.v_empleadores
import repositorios.bd_empleadores
import controladores.c_tviews as c_tviews


def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for empleador in repositorios.bd_empleadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(empleador.nombre, empleador.cuit))
        i+=1


def agregar(toplevel, tview_empleador):
    vistas.v_empleadores.mostrar(toplevel, tview_empleador)


def quitar(lista_campos, tview_empleador, l_exportacion):
    l_exportacion.config(text="")
    if len(tview_empleador.item(tview_empleador.focus())['values']) == 0:
        for campo in lista_campos:
            campo.disable()
        l_exportacion.config(text="")
        return False

    repositorios.bd_empleadores.borrar(
        repositorios.bd_empleadores.busca_por_cuit(
            tview_empleador.item(tview_empleador.focus())["values"][1]
        )[0]
    )
    actualiza_tview(tview_empleador)
    if len(tview_empleador.selection()) == 0:
        for campo in lista_campos:
            campo.disable()
    return None


def selecciona_empleador(lista_campos, b_guardar, b_exportar, tview_empleados, tview_empleadores, l_exportacion):

    if len(tview_empleadores.item(tview_empleadores.focus())['values']) == 0:
        b_guardar.configure(state="disabled")
        b_exportar.configure(state="disabled")
        for campo in lista_campos:
            campo.disable()
        l_exportacion.config(text="")
        return False

    for campo in lista_campos:
        campo.enable()

    c_tviews.actualiza_trabajadores(
        tview_empleados, cuit_empleador=tview_empleadores.item(tview_empleadores.focus())['values'][1])

    b_guardar.configure(state="normal")
    b_exportar.configure(state="normal")

    l_exportacion.config(text=f"Exportando para :{tview_empleadores.item(tview_empleadores.focus())['values'][0]}")
    return None

