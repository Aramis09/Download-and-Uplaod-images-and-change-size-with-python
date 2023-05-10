import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
# cambie de cuenta porque me olvide de ecribir el bien el txt
cloudinary.config(
    cloud_name='dynnwv7md',
    api_key='461588566863238',
    api_secret='krdH2NPcRFX_Z6pNWc84xlr1f5o'
)


maxIteration = 900
iteration = 0

while iteration < maxIteration:
    ruta_archivo = os.path.join(os.path.dirname(
        __file__), 'imagesCarrouselLowResolution', "imagenesCRed"+str(iteration)+'.jpg')

    verifyIfFileExist = os.path.exists(
        ruta_archivo) and os.path.isfile(ruta_archivo)
    print(ruta_archivo)
    if verifyIfFileExist:
        print("entramos")
        resultado = cloudinary.uploader.upload(ruta_archivo)
        newUrl = resultado['secure_url']
        print(newUrl)
        with open("carrouselImages.txt", "a") as archivo:
            archivo.write(newUrl + "\n")
    iteration = iteration + 1
