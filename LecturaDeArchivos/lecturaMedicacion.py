

def leerMedicacion():
    global medList
    


    with open("Medicacion.txt", "r") as listaMedicacion:
        lineas = listaMedicacion.readlines()

    lista_medicacion = [linea.strip() for linea in lineas if linea.strip()]
    medList = [terminos.split(";") for terminos in lista_medicacion]

    return medList





