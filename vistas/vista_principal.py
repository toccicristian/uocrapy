import tkinter as tk
from tkinter import ttk
import modelos.v_campo as campos

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
    f_empleador_botones = tk.Frame(f_empleadores)
    b_empleador_quitar = tk.Button(f_empleador_botones, text="Quitar")
    b_empleador_agregar = tk.Button(f_empleador_botones, text="Agregar")
    # EMPLEADOS DEFINICIONES
    f_empleados = tk.Frame(f_personas)
    l_empleados = tk.Label(f_empleados, text="Empleados")
    tview_empleados = ttk.Treeview(f_empleados, height=8)
    f_empleados_botones = tk.Frame(f_empleados)
    b_empleado_quitar = tk.Button(f_empleados_botones, text="Quitar")
    b_empleado_agregar = tk.Button(f_empleados_botones, text="Agregar")
    # DETALLES DEFINICIONES
    f_detalles = tk.Frame(v)
    campo_nombre = campos.Campo(f_detalles, texto_label="Nombre:", ancho_label=25, ancho_campo=40, pady=detalles_pady)
    campo_cuil = campos.Campo(f_detalles, texto_label="Cuil:", ancho_label=25, ancho_campo=13, pady=detalles_pady)
    campo_afiliado = campos.Campo(f_detalles, texto_label="Afiliado:", ancho_label=25, ancho_campo=1, pady=detalles_pady)
    campo_rem_cuota_sind = campos.Campo(f_detalles, texto_label="Remunerac. cuota sind.",
                                        ancho_label=25, ancho_campo=13, pady=detalles_pady)
    campo_rem_cese_laboral = campos.Campo(f_detalles, texto_label="Remunerac. cese laboral:",
                                          ancho_label=25, ancho_campo=13, pady=detalles_pady)
    campo_ingreso = campos.Campo(f_detalles, texto_label="Ingreso:", ancho_label=25, ancho_campo=10, pady=detalles_pady)
    campo_codigo_postal = campos.Campo(f_detalles, texto_label="Codigo postal:",
                                       ancho_label=25, ancho_campo=4, pady=detalles_pady)
    campo_convenio = campos.Campo(f_detalles, texto_label="Convenio:", ancho_label=25, ancho_campo=2, pady=detalles_pady)
    campo_categoria = campos.Campo(f_detalles, texto_label="Categoria:", ancho_label=25, ancho_campo=2, pady=detalles_pady)
    campo_admin_publica = campos.Campo(f_detalles, texto_label="Admin. Publica:",
                                       ancho_label=25, ancho_campo=1, pady=detalles_pady)
    lista_campos=[campo_nombre, campo_cuil, campo_afiliado, campo_rem_cuota_sind, campo_rem_cese_laboral, campo_ingreso,
                  campo_codigo_postal, campo_convenio, campo_categoria, campo_admin_publica]
    f_detalles_botones = tk.Frame(f_detalles)
    l_detalles_status = tk.Label(f_detalles_botones, text="", width=20, anchor=tk.W)
    b_detalles_guardar = tk.Button(f_detalles_botones, text="Guardar cambios")
    f_exportacion = tk.Frame(v)
    l_exportacion = tk.Label(f_exportacion, text="Exportando para:", width=48, anchor=tk.W)
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
    b_empleado_agregar.pack(side=tk.LEFT)
    # DETALLES PACK
    f_detalles.pack(side=tk.TOP, padx=(40,10),pady=(50,10))
    for campo in lista_campos:
        campo.pack()

    f_detalles_botones.pack(side=tk.TOP, pady=(40,20))
    l_detalles_status.pack(side=tk.LEFT, anchor=tk.W)
    b_detalles_guardar.pack(side=tk.LEFT, anchor=tk.W)
    # EXPORTACION PACK
    f_exportacion.pack(side=tk.RIGHT, anchor=tk.S, padx=(0,25), pady=(0,25))
    l_exportacion.pack(side=tk.LEFT, padx=(0,25))
    b_exportacion.pack(side=tk.RIGHT)
    #b_exportacion.pack(side=tk.RIGHT, anchor=tk.S, padx=(0,25), pady=(0,25))

    v.mainloop()

