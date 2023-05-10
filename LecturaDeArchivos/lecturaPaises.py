

def leerPaises():
    global countryList


    with open("Paises.txt", "r") as listaPaises:
        lineas = listaPaises.readlines()

    lista_paises = [linea.strip() for linea in lineas if linea.strip()]
    countryList = [terminos.split(";") for terminos in lista_paises]

    return countryList
