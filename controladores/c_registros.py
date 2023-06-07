import repositorios.bd_trabajadores
import repositorios.registros
import vistas.v_exportacion
import utiles.fechas
import constantes.longitud_campos as const_l

def exportar (tview_empleadores):
    url=vistas.v_exportacion.guardar_como()
    if not url:
        return False

    registros=list()
    for trabajador in repositorios.bd_trabajadores.busca_por_cuit_de_empleador(
        tview_empleadores.item(tview_empleadores.focus())['values'][1]):
        if trabajador.exportar:
            registros.append(f"{trabajador.cuil}{'S' if trabajador.afiliado else 'N'}{trabajador.rem_cuota_sind.zfill(const_l.REMUNERACION_CUOTA_SINDICAL)}{trabajador.rem_cese_laboral.zfill(const_l.REMUNERACION_CESE_LABORAL)
              }{utiles.fechas.amdtodma(trabajador.ingreso)
                }{trabajador.codigo_postal.zfill(const_l.CODIGO_POSTAL)
                  }{trabajador.convenio.zfill(const_l.CONVENIO)
                    }{trabajador.categoria.zfill(const_l.CATEGORIA)
                      }{'S' if trabajador.administracion_publica else 'N'}")
            print(f"Longitud {len(registros[:-1])}")

    repositorios.registros.grabar(registros, url)
    return True
