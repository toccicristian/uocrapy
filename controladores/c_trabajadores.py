import repositorios.bd_trabajadores

def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for trabajador in repositorios.bd_trabajadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(trabajador.nombre , trabajador.cuil))
        i+=1
