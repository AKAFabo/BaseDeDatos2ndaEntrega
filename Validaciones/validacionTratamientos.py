from LecturaDeArchivos.lecturaTratamiento import leerTratamiento

def validarTratamientos():

    treatList = leerTratamiento()
    
    codigosUsados = []
    validacionTreatList = []

    for i in range (len(treatList)):
            
            if int(treatList[i][0]) not in codigosUsados:

                validacionTreatList.append(treatList[i])
                codigosUsados.append(int(treatList[i][0]))

    return validacionTreatList
