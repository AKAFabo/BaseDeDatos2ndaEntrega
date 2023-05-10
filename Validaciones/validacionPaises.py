from LecturaDeArchivos.lecturaPaises import leerPaises as leerPaises


def validacionPais():
    global countryList

    countryList=leerPaises()

    temp = []
    temp2 = [] 
    posiciones = []
    validacionCountryList = []
    

    for i in range (len(countryList)):
        temp.append(int(countryList[i][0]))

        #print (temp)

    for i in range (len(temp)):
        if temp[i] not in temp2:

            temp2.append(temp[i])
            posiciones += [i]

    #print(posiciones)

    for i in range (len(countryList)):

        if i < len(posiciones):
            validacionCountryList.append(countryList[int(posiciones[i])])

        else:
            break

    return validacionCountryList
    




        
    


