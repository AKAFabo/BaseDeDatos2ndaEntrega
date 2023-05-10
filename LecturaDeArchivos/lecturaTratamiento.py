

def leerTratamiento():
    global treatList
    

    with open("txts/Tratamiento.txt", "r") as listaTratamiento:
        lineas = listaTratamiento.readlines()

    lista_tratamiento = [linea.strip() for linea in lineas if linea.strip()]
    treatList = [terminos.split(";") for terminos in lista_tratamiento]

    return treatList





