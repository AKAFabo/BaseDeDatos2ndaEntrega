from Validaciones.validacionPaises import validacionPais

def codePaises ():

    temp = validacionPais()
    listaCodigosPaises = []

    for i in range (len(temp)):

        listaCodigosPaises+= ([temp[i][0]])                             #LISTA DE CODIGO DE PAISES


    return listaCodigosPaises


def nombrePaises ():

    temp = validacionPais()
    listaNombresPaises = []

    for i in range (len(temp)):

        listaNombresPaises+= [temp[i][1]]                                   #LISTA DE NOMBRES DE PAISES


    return listaNombresPaises


from Validaciones.validacionCiudades import validacionCiudades

def codeCiudades ():

    temp = validacionCiudades()                                     #LISTA DE CODIGO DE CIUDADES
    listaCodigoCiudades = []

    for i in range (len(temp)):

        listaCodigoCiudades+= [temp[i][1]]

    return listaCodigoCiudades


def nombreCiudades ():

    temp = validacionCiudades()                                     #LISTA DE NOMBRES DE CIUDADES
    listaNombreCiudades = []

    for i in range (len(temp)):

        listaNombreCiudades+= [temp[i][2]]

    return listaNombreCiudades



from Validaciones.validacionCliente import validacionCliente

def codeClientes():

    temp = validacionCliente()
    listaCodigoClientes = []

    for i in range (len(temp)):                                             #LISTA DE CODIGO DE CLIENTES

        listaCodigoClientes+= [temp[i][0]]

    return listaCodigoClientes

    

from Validaciones.validacionMascotas import validacionMascota

def codeMascotas():

    temp = validacionMascota()
    listaCodigoMascotas = []
                                                                            #LISTA DE CODIGO DE MASCOTAS
    for i in range (len(temp)):

        listaCodigoMascotas+= [temp[i][1]]

    return listaCodigoMascotas


from Validaciones.validacionVisitas import validarVisitas

def codeVisitas():

    temp = validarVisitas()
    listaCodigoVisitas = []

    for i in range (len(temp)):                                            #LISTA DE CODIGO DE VISITAS

        listaCodigoVisitas+= [temp[i][0]]

    return listaCodigoVisitas


from Validaciones.validacionMedicacion import validarMedicacion

def codeMedicacion():

    temp = validarMedicacion()
    listaCodigoMedicacion = []

    for i in range (len(temp)):                                            #LISTA DE CODIGO DE MEDICACION

        listaCodigoMedicacion+= [temp[i][1]]

    return listaCodigoMedicacion


def medicaciones():

    temp = validarMedicacion()
    listaMedicaciones = []

    for i in range (len(temp)):                                            #LISTA DE CODIGO DE MEDICACION

        listaMedicaciones= [temp[i][0]]

    return listaMedicaciones
    


from Validaciones.validacionTratamientos import validarTratamientos

def codeTratamiento():

    temp = validarTratamientos()
    listaCodigoTratamientos = []

    for i in range (len(temp)):

        listaCodigoTratamientos+= [temp[i][0]]

    return listaCodigoTratamientos





 


