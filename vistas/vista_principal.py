import tkinter as tk
from tkinter import ttk
import modelos.v_campo as campos
import modelos.v_checkbox as checkbox
import modelos.v_dropdown as dropdown
import controladores.c_principal_empleador as empleador
import controladores.c_principal_empleado as empleado
import controladores.c_convenio as convenios
import controladores.c_categoria as categorias
import controladores.c_detalles as detalles
import controladores.c_registros as c_registros

def mostrar():
    v_min_w="800"
    v_min_h="600"
    detalles_pady=5
    v=tk.Tk()
    v.title("UOCRA PY")
    v.geometry(f"{v_min_w}x{v_min_h}")
    v.resizable(width=False, height=False)
    # DEFINICIONES
    f_personas = tk.Frame(v)
    # EMPLEADORES DEFINICIONES
    f_empleadores = tk.Frame(f_personas)
    l_empleadores = tk.Label(f_empleadores, text="Empleadores")
    tview_empleadores = ttk.Treeview(f_empleadores, height=8)

    tview_empleadores["columns"] = ("NOMBRE", "CUIT")
    tview_empleadores.column("#0", width=0, stretch=tk.NO)
    tview_empleadores.column("NOMBRE", anchor=tk.E, stretch=tk.YES, width="100")
    tview_empleadores.column("CUIT", anchor=tk.E, stretch=tk.YES, width="100")
    tview_empleadores.heading("#0", text="", anchor=tk.W)
    tview_empleadores.heading("NOMBRE", text="NOMBRE", anchor=tk.W)
    tview_empleadores.heading("CUIT", text="CUIT", anchor=tk.W)
    scrollb_empleadores=tk.Scrollbar(f_empleadores, orient="vertical")
    tview_empleadores.config(yscrollcommand=scrollb_empleadores.set)
    scrollb_empleadores.config(command=tview_empleadores.yview)

    f_empleador_botones = tk.Frame(f_empleadores)
    b_empleador_quitar = tk.Button(f_empleador_botones, text="Quitar")
    b_empleador_agregar = tk.Button(f_empleador_botones, text="Agregar")
    # EMPLEADOS DEFINICIONES
    f_empleados = tk.Frame(f_personas)
    l_empleados = tk.Label(f_empleados, text="Empleados")
    tview_empleados = ttk.Treeview(f_empleados, height=8)

    tview_empleados["columns"] = ("NOMBRE", "CUIT")
    tview_empleados.column("#0", width=0, stretch=tk.NO)
    tview_empleados.column("NOMBRE", anchor=tk.E, stretch=tk.YES, width="100")
    tview_empleados.column("CUIT", anchor=tk.E, stretch=tk.YES, width="100")
    tview_empleados.heading("#0", text="", anchor=tk.W)
    tview_empleados.heading("NOMBRE", text="NOMBRE", anchor=tk.W)
    tview_empleados.heading("CUIT", text="CUIT", anchor=tk.W)
    scrollb_empleados=tk.Scrollbar(f_empleados, orient="vertical")
    tview_empleados.config(yscrollcommand=scrollb_empleados.set)
    scrollb_empleados.config(command=tview_empleados.yview)

    f_empleados_botones = tk.Frame(f_empleados)
    b_empleado_quitar = tk.Button(f_empleados_botones, text="Quitar")
    # DETALLES DEFINICIONES
    f_detalles = tk.Frame(v)

    campo_nombre = campos.Campo(f_detalles, texto_label="Nombre:",
                                ancho_label=25, ancho_campo=40, pady=detalles_pady, nombre="nombre")
    campo_cuil = campos.Campo(f_detalles, texto_label="Cuil:",
                              ancho_label=25, ancho_campo=13, pady=detalles_pady, nombre="cuil")
    campo_rem_cuota_sind = campos.Campo(f_detalles, texto_label="Remunerac. cuota sind.",
                                        ancho_label=25, ancho_campo=13, pady=detalles_pady, nombre="remcuota")
    campo_rem_cese_laboral = campos.Campo(f_detalles, texto_label="Remunerac. cese laboral:",
                                          ancho_label=25, ancho_campo=13, pady=detalles_pady, nombre="remcese")
    campo_ingreso = campos.Campo(f_detalles, texto_label="Ingreso:",
                                 ancho_label=25, ancho_campo=10, pady=detalles_pady, nombre="ingreso")
    campo_codigo_postal = campos.Campo(f_detalles, texto_label="Codigo postal:",
                                       ancho_label=25, ancho_campo=4, pady=detalles_pady, nombre="codpostal")
    dropdown_convenio = dropdown.ListaDesplegable(f_detalles, texto_label="Convenio:",
                                                  ancho_label=25,
                                                  pady=detalles_pady, nombre="convenio",
                                                  opcion_default=convenios.default_nombre(0),
                                                  lista_opciones=convenios.lista_por_nombre()
                                                  )
    dropdown_categoria = dropdown.ListaDesplegable(f_detalles, texto_label="Categoria:",
                                                  ancho_label=25,
                                                  pady=detalles_pady, nombre="categoria",
                                                  opcion_default=categorias.default_nombre(0),
                                                  lista_opciones=categorias.lista_por_nombre()
                                                  )
    check_afiliado = checkbox.Checkbox(f_detalles, text="Afiliado",pady=detalles_pady, nombre="afiliado")
    check_admin_publica = checkbox.Checkbox(f_detalles, text="Admin. Publica",pady=detalles_pady, nombre="adminpublica")
    check_exportar = checkbox.Checkbox(f_detalles, text="EXPORTAR",
                                       padx=(0,20), pady=detalles_pady*2,
                                       packanchor=tk.E, nombre="exportar")

    lista_campos=[campo_nombre, campo_cuil, campo_rem_cuota_sind, campo_rem_cese_laboral, campo_ingreso,
                  campo_codigo_postal, dropdown_convenio, dropdown_categoria, check_afiliado, check_admin_publica,
                  check_exportar]

    f_detalles_botones = tk.Frame(f_detalles)
    l_detalles_status = tk.Label(f_detalles_botones, text="", width=20, anchor=tk.W)
    b_detalles_guardar = tk.Button(f_detalles_botones, text="Guardar cambios")
    f_exportacion = tk.Frame(v)
    l_exportacion = tk.Label(f_exportacion, text="", width=48, anchor=tk.W)
    b_exportacion = tk.Button(f_exportacion, text="Exportar a UOCRA...")
    # PACKS
    f_personas.pack(side=tk.LEFT, padx=(20,10))
    # EMPLEADORES PACK
    f_empleadores.pack(side=tk.TOP, pady=(0,20))
    l_empleadores.pack(side=tk.TOP)
    tview_empleadores.pack(side=tk.TOP)
    f_empleador_botones.pack(side=tk.TOP)
    b_empleador_quitar.pack(side=tk.LEFT)
    b_empleador_agregar.pack(side=tk.LEFT)
    # EMPLEADOS PACK
    f_empleados.pack(side=tk.TOP, pady=(20,0))
    l_empleados.pack(side=tk.TOP)
    tview_empleados.pack(side=tk.TOP)
    f_empleados_botones.pack(side=tk.TOP)
    b_empleado_quitar.pack(side=tk.LEFT)
    # DETALLES PACK
    f_detalles.pack(side=tk.TOP, padx=(35,10),pady=(63,10))
    for campo in lista_campos:
        campo.disable()
        campo.pack()

    f_detalles_botones.pack(side=tk.TOP, pady=(40,20))
    l_detalles_status.pack(side=tk.LEFT, anchor=tk.W)
    b_detalles_guardar.pack(side=tk.LEFT, anchor=tk.W)
    # EXPORTACION PACK
    f_exportacion.pack(side=tk.RIGHT, anchor=tk.S, padx=(0,25), pady=(0,25))
    l_exportacion.pack(side=tk.LEFT, padx=(0,25))
    b_exportacion.pack(side=tk.RIGHT)

    # BINDEOS Y COMANDOS
    b_empleador_quitar.configure(command = lambda : empleador.quitar(
        lista_campos, tview_empleadores,l_exportacion))
    b_empleador_agregar.configure(command = lambda : empleador.agregar(
        v, tview_empleadores))
    b_empleado_quitar.configure(command = lambda : empleado.quitar(
        lista_campos, tview_empleados, tview_empleadores))
    b_detalles_guardar.configure(command = lambda : detalles.guardar_cambios(
        v, tview_empleadores,lista_campos, tview_empleados))
    b_exportacion.configure(command = lambda : c_registros.exportar(tview_empleadores))
    v.bind('<Escape>', lambda event: v.destroy())
    tview_empleadores.bind("<<TreeviewSelect>>",
                           lambda event: empleador.selecciona_empleador(lista_campos, tview_empleados, tview_empleadores, l_exportacion))
    tview_empleados.bind("<<TreeviewSelect>>",
                         lambda event: empleado.selecciona_trabajador(lista_campos, tview_empleados,
                        tview_empleadores))

    empleador.actualiza_tview(tview_empleadores)
    # empleado.actualiza_tview(tview_empleados)
    v.mainloop()

#TODO : CUANDO NO QUEDAN EMPLEADORES SELECCIONADOS, VACIAR EL TVIEW DE TRABAJADORES
