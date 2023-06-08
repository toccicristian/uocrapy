import repositorios.bd_trabajadores

def actualiza_tview(tview, tview_empleadores):
    tview.delete(*tview.get_children())
    i=0
    for trabajador in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(
        tview_empleadores.item(tview_empleadores.focus())['values'][1]):
        tview.insert(parent="", index=i, iid=i, text="", values=(trabajador.nombre , trabajador.cuil))
        i+=1
