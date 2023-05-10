from PIL import Image

import os

maxIteration = 85
iteration = 0

ruta_carpeta_save_images = "imagenesCRed"
ruta_absoluta = os.path.abspath(ruta_carpeta_save_images)
print(ruta_absoluta)

while iteration < maxIteration:
    ruta_archivo = os.path.join(os.path.dirname(
        __file__), 'imagesMinuim', str(iteration)+'.jpg')

    verifyIfFileExist = os.path.exists(
        ruta_archivo) and os.path.isfile(ruta_archivo)

    if verifyIfFileExist:
        print("entramos")
        imagen_original = Image.open(ruta_archivo)
        imagen_redimensionada = imagen_original.resize((1280, 720))
        rutaImagen = ruta_absoluta + str(iteration)+'.jpg'
        imagen_redimensionada.save(
            rutaImagen, format="JPEG")
    iteration = iteration + 1
