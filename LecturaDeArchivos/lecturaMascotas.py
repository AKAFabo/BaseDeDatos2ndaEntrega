

def leerMascotas():
    global petList
    


    with open("txts/Mascotas.txt", "r") as listaMascotas:
        lineas = listaMascotas.readlines()

    lista_mascotas = [linea.strip() for linea in lineas if linea.strip()]
    petList = [terminos.split(";") for terminos in lista_mascotas]

    return petList





