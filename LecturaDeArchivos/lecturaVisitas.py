

def leerVisitas():
    global visitList
    


    with open("Visitas.txt", "r") as listaVisitas:
        lineas = listaVisitas.readlines()

    lista_visitas = [linea.strip() for linea in lineas if linea.strip()]
    visitList = [terminos.split(";") for terminos in lista_visitas]

    return visitList



