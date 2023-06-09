import repositorios.bd_empleadores
import repositorios.bd_trabajadores
import modelos.empleadores
import modelos.v_mensaje
import utiles.cuit


def actualiza_tview(tview):
    tview.delete(*tview.get_children())
    i=0
    for empleador in repositorios.bd_empleadores.leer():
        tview.insert(parent="", index=i, iid=i, text="", values=(empleador.nombre, empleador.cuit))
        i+=1
    return None


def actualiza_tview_empleados(tview_empleados, tview_empleadores):
    tview_empleados.delete(*tview_empleados.get_children())
    if tview_empleadores.item(tview_empleadores.focus())['values'] == '':
        return False
    i=0
    for empleado in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(
        tview_empleadores.item(tview_empleadores.focus())['values'][1]):
        tview_empleados.insert(parent="", index=i, iid=i, text="", values=(empleado.nombre, empleado.cuit))
    return True


def agregar(v, tview_empleadores, tview_empleados, nombre, cuit):
    if len(cuit)!=11:
        modelos.v_mensaje.Mensaje(
            v, f"El numero es muy { 'corto' if len(cuit)<11 else 'largo'} ({len(cuit)} caracteres)"
        )
        return False

    if not str(cuit[0:2]) in ['20','23','24','27','30','33','34']:
        modelos.v_mensaje.Mensaje(
            v, f"El tipo de cuit es inválido."
        )
        return False

    if utiles.cuit.digitver(str(cuit)[:-1]) != str(cuit)[-1]:
        modelos.v_mensaje.Mensaje(
            v, f"El numero ingresado NO es un CUIT.\nDV calculado: {utiles.cuit.digitver(str(cuit)[:-1])}"
        )
        return False

    for empleador in repositorios.bd_empleadores.leer():
        if str(empleador.cuit) == str(cuit):
            modelos.v_mensaje.Mensaje(v,"El CUIT ya existe en Base de Datos")
            return False

    empleador=modelos.empleadores.Empleador(cuit=cuit, nombre=nombre)
    repositorios.bd_empleadores.crear(empleador)
    actualiza_tview(tview_empleadores)
    actualiza_tview_empleados(tview_empleados, tview_empleadores)
    v.destroy()

