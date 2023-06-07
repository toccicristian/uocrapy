import repositorios.bd_empleadores
import repositorios.bd_trabajadores

def actualiza_empleadores(tview):
    tview.delete(*tview.get_children())
    i=0
    for empleador in repositorios.bd_empleadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(empleador.nombre, empleador.cuit))
        i+=1


def actualiza_trabajadores(tview,cuit_empleador=str()):
    tview.delete(*tview.get_children())
    i=0
    for trabajador in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(cuit_empleador):
        tview.insert(parent="", index=i, iid=i, text="", values=(trabajador.nombre, trabajador.cuil))
        i+=1
