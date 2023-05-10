import urllib
import requests
import os
productsJson = requests.get(
    "https://apisgames-production-06fc.up.railway.app/products")
productArray = productsJson.json()
counter = 1
if True:
    for productObj in productArray:
        counter2 = 1
        for image in productObj["images"]:
            counter2 = counter2 + 1
            url = image
            name = str(counter) + str(counter2) + ".jpg"
            print(name)
            image = open(name, "wb")
            image.write(requests.get(url).content)
            image.close()
        counter = counter + 1
