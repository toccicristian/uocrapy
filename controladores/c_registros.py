import repositorios.bd_trabajadores
import repositorios.registros
import vistas.v_exportacion
import modelos.v_mensaje
import utiles.fechas
import constantes.longitud_campos as const_l

def exportar (toplevel, tview_empleadores):
    url=vistas.v_exportacion.guardar_como()
    if not url:
        return False

    registros=list()
    for trabajador in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(
        tview_empleadores.item(tview_empleadores.focus())['values'][1]):
        if trabajador.exportar:
          registros.append(
              str(trabajador.cuil)+
              str('S' if trabajador.afiliado else 'N')+
              str(int(float(trabajador.rem_cuota_sind)*100)).zfill(const_l.REMUNERACION_CUOTA_SINDICAL)+
              str(int(float(trabajador.rem_cese_laboral)*100)).zfill(const_l.REMUNERACION_CESE_LABORAL)+
              str(utiles.fechas.amdtodma(trabajador.ingreso))+
              str(trabajador.codigo_postal.zfill(const_l.CODIGO_POSTAL))+
              str(trabajador.convenio.zfill(const_l.CONVENIO))+
              str(trabajador.categoria.zfill(const_l.CATEGORIA))+
              str('S' if trabajador.administracion_publica else 'N')+
              '\n'
            )
    modelos.v_mensaje.Mensaje(toplevel, "ARCHIVO GENERADO CORRECTAMENTE",width="300")
    repositorios.registros.grabar(registros, url)
    return True
