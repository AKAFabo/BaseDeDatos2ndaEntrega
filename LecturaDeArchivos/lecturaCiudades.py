
def leerCiudades():
    global cityList


    with open("txts/Ciudades.txt", "r") as listaCiudades:
        lineas = listaCiudades.readlines()

    lista_ciudades = [linea.strip() for linea in lineas if linea.strip()]
    cityList = [terminos.split(";") for terminos in lista_ciudades]

    return cityList







