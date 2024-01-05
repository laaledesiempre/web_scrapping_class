import requests
from bs4 import BeautifulSoup as bs

def sacar_link_de_imagen(link_de_pinterest):
    respuesta = requests.get(link_de_pinterest)
    sopa = bs(respuesta.text,'html.parser') # Documento HTML convertido para que lo usemos
    return sopa.find_all("img")[0]["src"]

def guardar_imagen(link_de_imagen,nombre_para_archivo):
    binario_de_imagen = requests.get(link_de_imagen)
    open(nombre_para_archivo+".jpg", 'wb').write(binario_de_imagen.content)

print("Bienvenido a mi aplicacion para descargar imagenes de pinterest")
while True:
    print("""
    Podes descargar una imagen o salir
          1) Descargar imagen
          S) salir
          """)
    respueta_de_usuario = input("Opcion: ")
    if respueta_de_usuario == "1":
        print("Pone el link de pinterest: ")
        while True:
            try:
                link_de_pinterest = input("Link: ")
                link_de_imagen = sacar_link_de_imagen(link_de_pinterest)
                break
            except:
                print("Disculpa, este link no sirve")
                continue

        nombre_para_archivo = input("Nombre para el archivo")
        guardar_imagen(link_de_imagen,nombre_para_archivo)
        input("TU IMAGEN SE AH GUARDADO, PRECIONA ENTER PARA CONTINUAR")
    elif respueta_de_usuario.upper() == "S":
        break
    else:
        print("Esa no es una opcion")
        input("APRETA ENTER PARA CONTINUAR")
