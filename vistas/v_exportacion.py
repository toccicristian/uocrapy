import tkinter as tk


def guardar_como():
    ruta_archivo_registros=tk.filedialog.asksaveasfilename(mode='w', filetypes=[('Archivos TXT','*.txt')])
    return ruta_archivo_registros

