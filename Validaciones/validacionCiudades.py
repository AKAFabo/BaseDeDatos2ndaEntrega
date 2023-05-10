from LecturaDeArchivos.lecturaCiudades import leerCiudades as leerCiudades
from Validaciones.validacionPaises import validacionPais



def validacionCiudades():

    cityList = leerCiudades()
    listaPaises = validacionPais()

    listCodePaises = []
    PrimeraValidacion = []
    temp = []
    temp2 = []
    posiciones = []
    SegundaValidacion = []
    validacionCityList = []

    duplicados = set()

    #### Validacion de pais exista ####

    for i in range(len(listaPaises)):

        listCodePaises.append(listaPaises[i][0])

    for i in range(0,len(cityList)):

        if (cityList[i][0]) in listCodePaises:
            PrimeraValidacion.append(cityList[i])
   
    #### Validacion de ciudad no sea repetida ####

    for i in range (len(PrimeraValidacion)):
        temp.append(PrimeraValidacion[i][1])
   
    for i in range (0,len(temp)):
        if temp[i] not in temp2:

            temp2.append(temp[i])
            posiciones += [i]
  

    for i in range (len(PrimeraValidacion)):

        if i < len(posiciones):
            SegundaValidacion.append(PrimeraValidacion[posiciones[i]])

        else:
            break
    

    for sublista in SegundaValidacion:

        if tuple(sublista[:2]) not in duplicados:

            validacionCityList.append(sublista)
            duplicados.add(tuple(sublista[:2]))

 
    return validacionCityList




