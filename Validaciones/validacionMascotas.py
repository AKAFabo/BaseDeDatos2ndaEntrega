from Validaciones.validacionCliente import validacionCliente
from LecturaDeArchivos.lecturaMascotas import leerMascotas


def validacionMascota ():

    clientList = validacionCliente()
    petList = leerMascotas()

    listCodeClientes = []
    listCodeMascotas = []
    PrimeraValidacion = []
   
    validacionPetList = []
    

    ### VALIDACION DE QUE CLIENTE EXISTA ###

    for i in range (len(clientList)):
        
        listCodeClientes.append(int(clientList[i][0]))

    for i in range (len(petList)):

        if int(petList[i][0]) in listCodeClientes:
            PrimeraValidacion.append(petList[i])

    ### VALIDACION DE CODIGOS DE MASCOTA ###

    for i in range(len(PrimeraValidacion)):
        listCodeMascotas.append(int(PrimeraValidacion[i][1]))
    
    for i in range (len(PrimeraValidacion)):

        if int(PrimeraValidacion[i][1]) in listCodeMascotas:
            validacionPetList.append(PrimeraValidacion[i])
   
    return validacionPetList

                    



