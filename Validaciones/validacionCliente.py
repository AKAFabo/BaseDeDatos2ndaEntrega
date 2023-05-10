from Validaciones.validacionCiudades import validacionCiudades as validacionCiudades
from LecturaDeArchivos.lecturaClientes import leerClientes as leerClientes
from Validaciones.setCiudadesPaisesValidos import gruposValidos



def validacionCliente():

    listaValida = validacionCiudades()
    gruposValidos = set()

    for sublista in listaValida:

        gruposValidos.add(tuple(sublista[:2]))


    clientList = leerClientes()
    SegundaValidacion = []
    temp = []
    temp2 = []
    posiciones = []
    validacionClientList = []

    #### Validacion de que pais y ciudad existan ####

    for sublista in clientList:

        if tuple(sublista[3:5]) in gruposValidos:

            SegundaValidacion.append(sublista)

    #### Validacion de que el codigo de cliente no se repita ####

    for i in range (len(SegundaValidacion)):
        temp += [int(SegundaValidacion[i][0])]
   
    for i in range (len(temp)):
        if temp[i] not in temp2:

            temp2 += [temp[i]]
            posiciones += [i]

  
    for i in range (len(SegundaValidacion)):

        if i < len(posiciones):
            validacionClientList.append(SegundaValidacion[int(posiciones[i])])

        else:
            break

    return validacionClientList



