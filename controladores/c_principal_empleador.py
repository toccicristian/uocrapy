import vistas.v_empleadores
import repositorios.bd_empleadores


def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for empleador in repositorios.bd_empleadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(empleador.nombre, empleador.cuit))
        i+=1


def agregar(toplevel, tview_empleador):
    vistas.v_empleadores.mostrar(toplevel, tview_empleador)


def quitar(tview_empleador):
    repositorios.bd_empleadores.borrar(
        repositorios.bd_empleadores.busca_por_cuit(
            tview_empleador.item(tview_empleador.focus())["values"][1]
        )[0]
    )
    actualiza_tview(tview_empleador)
