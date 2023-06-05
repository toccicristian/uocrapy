import repositorios.bd_empleadores
import modelos.empleadores


def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for empleador in repositorios.bd_empleadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(empleador.nombre, empleador.cuit))
        i+=1


def agregar(v, tview_empleadores, nombre, cuit):
    for empleador in repositorios.bd_empleadores.leer():
        if empleador.cuit == cuit:
            return False

    empleador=modelos.empleadores.Empleador(cuit=cuit, nombre=nombre)
    repositorios.bd_empleadores.crear(empleador)
    actualiza_tview(tview_empleadores)
    v.destroy()

