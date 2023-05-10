from LecturaDeArchivos.lecturaMedicacion import leerMedicacion

def validarMedicacion():

    medList = leerMedicacion()

    validacionMedList = []
    duplicadas = set()

    for sublista in medList:

        if tuple(sublista[:5]) not in duplicadas:

            validacionMedList.append(sublista)
            duplicadas.add(tuple(sublista[:5]))

    return validacionMedList


    

    

    


