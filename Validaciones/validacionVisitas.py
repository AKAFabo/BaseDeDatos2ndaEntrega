from LecturaDeArchivos.lecturaVisitas import leerVisitas

def validarVisitas():

    visitList = leerVisitas()
    
    codigosUsados= []

    validacionVisitList = []

    for i in range (len(visitList)):
        
        if int(visitList[i][0]) not in codigosUsados:

            validacionVisitList+= [visitList[i]]
            codigosUsados.append(int(visitList[i][0]))


    return validacionVisitList


    