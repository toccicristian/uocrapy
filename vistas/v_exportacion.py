import tkinter as tk
import tkinter.filedialog
import os.path
import constantes.rutas as rutas

def guardar_como(initd=os.path.normpath(os.path.expanduser(rutas.EXPORT_DIR))):
    ruta_archivo_registros=tk.filedialog.asksaveasfilename(
        confirmoverwrite=True,
        initialdir=initd if os.path.isdir(initd) else os.path.normpath('.'),
        filetypes=[('Archivos TXT','*.txt')])
    return ruta_archivo_registros

