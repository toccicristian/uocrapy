import tkinter as tk
import modelos.v_campo as campos
import controladores.c_empleadores

def mostrar(toplevel, tview_empleador, width="600", height="150"):
    v=tk.Toplevel(toplevel)
    v.title("Agregar empleador")
    v.geometry(f"{width}x{height}")
    v.resizable(width=False, height=False)
    f_campos=tk.Frame(v)
    campo_nombre=campos.Campo(f_campos, texto_label="Nombre:", ancho_label=25, ancho_campo=40, pady=(10,5))
    campo_cuit=campos.Campo(f_campos, texto_label="CUIT:", ancho_label=25, ancho_campo=13, pady=(10,5))
    f_botones=tk.Frame(v)
    b_cancelar=tk.Button(f_botones, text="Cancelar", command = lambda : v.destroy())
    b_aceptar=tk.Button(f_botones, text="Aceptar",
                        command = lambda : controladores.c_empleadores.agregar(
                            v, tview_empleador, campo_nombre.text, campo_cuit.text))

    #BINDEOS
    v.bind("<Escape>", lambda event: v.destroy())

    f_campos.pack(side=tk.TOP, padx=(10,10), pady=(10,0))
    campo_nombre.pack()
    campo_cuit.pack()
    f_botones.pack(side=tk.RIGHT, padx=(0,20), pady=(0,10))
    b_aceptar.pack(side=tk.RIGHT, padx=(10,0),anchor=tk.E)
    b_cancelar.pack(side=tk.RIGHT, padx=(10,0), anchor=tk.E)

    campo_nombre.focus_set()
