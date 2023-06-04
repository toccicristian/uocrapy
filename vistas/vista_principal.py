import tkinter as tk
from tkinter import ttk

def mostrar():
    v_min_w="800"
    v_min_h="600"
    v=tk.Tk()
    v.title("UOCRA PY")
    v.geometry(f"{v_min_w}x{v_min_h}")
    v.resizable(width=False, height=False)
    # DEFINICIONES
    f_personas = tk.Frame(v)
    # EMPLEADORES DEFINICIONES
    f_empleadores = tk.Frame(f_personas)
    l_empleadores = tk.Label(f_empleadores, text="Empleadores")
    tview_empleadores = ttk.Treeview(f_empleadores, height=10)
    f_empleador_botones = tk.Frame(f_empleadores)
    b_empleador_quitar = tk.Button(f_empleador_botones, text="Quitar")
    b_empleador_agregar = tk.Button(f_empleador_botones, text="Agregar")
    # EMPLEADOS DEFINICIONES
    f_empleados = tk.Frame(f_personas)
    l_empleados = tk.Label(f_empleados, text="Empleados")
    tview_empleados = ttk.Treeview(f_empleados, height=10)
    f_empleados_botones = tk.Frame(f_empleados)
    b_empleado_quitar = tk.Button(f_empleados_botones, text="Quitar")
    b_empleado_agregar = tk.Button(f_empleados_botones, text="Agregar")
    # PACKS
    f_personas.pack(side=tk.LEFT)
    # EMPLEADORES PACK
    f_empleadores.pack(side=tk.TOP)
    l_empleadores.pack(side=tk.TOP)
    tview_empleadores.pack(side=tk.TOP)
    f_empleador_botones.pack(side=tk.TOP)
    b_empleador_quitar.pack(side=tk.LEFT)
    b_empleador_agregar.pack(side=tk.LEFT)
    # EMPLEADOS PACK
    f_empleados.pack(side=tk.TOP)
    l_empleados.pack(side=tk.TOP)
    tview_empleados.pack(side=tk.TOP)
    f_empleados_botones.pack(side=tk.TOP)
    b_empleado_quitar.pack(side=tk.LEFT)
    b_empleado_agregar.pack(side=tk.LEFT)

    v.mainloop()


mostrar()
