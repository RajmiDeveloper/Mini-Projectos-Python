import tkinter as tk
from PIL import Image, ImageTk
import os

# Obtener la ruta absoluta de la carpeta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta de la carpeta 'Assets' y el nombre de la imagen
assets_dir = os.path.join(script_dir, 'Assets')
nombre_imagen = 'background.webp'  # Cambia esto al nombre de tu archivo de imagen

# Crear la ventana de Tkinter
window = tk.Tk()
window.title("Visualizador de Imagen desde Carpeta Assets")
window.geometry("320x340")

# Función para mostrar la imagen en la ventana de Tkinter
def mostrar_imagen_local():
    # Obtener la ruta completa de la imagen en la carpeta 'Assets'
    img_path = os.path.join(assets_dir, nombre_imagen)
    
    # Abrir la imagen usando PIL
    img = Image.open(img_path)
    
    # Ajustar el tamaño de la imagen (opcional)
    img = img.resize((300, 300))  # Cambiar tamaño según tus necesidades
    
    # Convertir la imagen a un formato que Tkinter pueda manejar
    img_tk = ImageTk.PhotoImage(img)

    # Crear un label para mostrar la imagen
    label = tk.Label(window, image=img_tk)
    label.image = img_tk  # Necesario para mantener la referencia
    label.pack()

# Mostrar la imagen local desde la carpeta 'Assets'
mostrar_imagen_local()

# Iniciar el loop de la ventana
window.mainloop()
