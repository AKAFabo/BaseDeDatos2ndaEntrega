

#IMPORTAR FUNCIONES DE VALIDACION

from Validaciones.validacionPaises import validacionPais
from Validaciones.validacionCiudades import validacionCiudades
from Validaciones.validacionCliente import validacionCliente
from Validaciones.validacionMascotas import validacionMascota
from Validaciones.validacionVisitas import validarVisitas
from Validaciones.validacionTratamientos import validarTratamientos
from Validaciones.validacionMedicacion import validarMedicacion

#IMPORTAR LISTAS CON CODIGOS Y DEMAS VARIABLES

from listasConCodigos import codePaises, codeCiudades, codeClientes,codeMascotas,codeVisitas,codeTratamiento, codeMedicacion

#LISTAS EN MEMORIA

ListaDePaises = validacionPais()
ListaDeCiudades = validacionCiudades()
ListaDeClientes = validacionCliente()
ListaDeMascotas = validacionMascota()
ListaDeVisitas = validarVisitas()
ListaDeTratamientos = validarTratamientos()
ListaDeMedicacion = validarMedicacion()

codigosPaisesValidos = codePaises()
codigosClientesValidos = codeClientes()  
codigosCiudadesValidos = codeCiudades()
codigosMascotasValidos = codeMascotas()
codigosVisitasValidos = codeVisitas()
codigosTratamientosValidos = codeTratamiento()
codigosMedicacionValidos = codeMedicacion()

'''#MENUS VAN ACA#

def menuLeer ():

    while True:

        print ("Seleccione la opcion a leer")
        print ("1 = Paises")
        print ("2 = Ciudades")
        print ("3 = Clientes")
        print ("4 = Mascotas")
        print ("5 = Visitas")
        print ("6 = Medicacion")
        print ("7 = Tratamientos")
        print ("X = Salir al menu principal")

        opcion = input("Ingrese el numero de la opcion a leer: ")

        if opcion == "1":
            print (ListaDePaises)

        if opcion == "2":
            print (ListaDeCiudades)

        if opcion == "3":
            print (ListaDeClientes)

        if opcion == "4":
            print (ListaDeMascotas)

        if opcion == "5":
            print (ListaDeVisitas)

        if opcion == "6":
            print (ListaDeMedicacion)

        if opcion == "7":
            print (ListaDeTratamientos)

        if opcion == "X" or "x":
            break



def menuInsertar(): 

    global codigosPaisesValidos
    global codigosClientesValidos
    global codigosMascotasValidos
    global codigosCiudadesValidos
    global codigosMedicacionValidos
    global codigosVisitasValidos
    global codigosTratamientosValidos   

    print("Selecciona la opcion a insertar un dato")
    print("1 = Insertar un pais nuevo")
    print("2 = Insertar una ciudad nueva a un pais")
    print("3 = Insertar un nuevo cliente")
    print("4 = Insertar una nueva mascota")
    print("5 = Insertar una nueva visita")
    print("6 = Insertar un nuevo tratamiento")
    print("7 = Insertar una nueva medicacion a una mascota")
    print("X = Volver al menu principal")

    opcion = input("Ingrese el numero de la opcion: ")

    if opcion == "1":

        codigo = input("Ingrese el codigo de pais a ingresar: ")
        nombre = input("Ingrese el nombre del pais a ingresar: ")     

        if codigo not in codigosPaisesValidos and nombre not in nombresPaisesValidos:
            nuevoPais = [codigo, nombre]
            ListaDePaises.append(nuevoPais)
            codigosPaisesValidos+=[codigo]

            print("El pais ha sido añadido")

        else:
            print("El codigo o nombre del pais ingresado ya existe")


    if opcion == "2":

        codigoPais = input("Ingrese el codigo de pais a ingresar una ciudad: ")

        if codigoPais not in codigosPaisesValidos:
            print("El pais ingresado no existe")

        else:
            codigo = input("Ingrese el codigo de ciudad a ingresar: ")
            nombre = input("Ingrese el nombre de la ciudad a ingresar: ")

            if codigo not in codigosCiudadesValidos:
                nuevaCiudad = [codigoPais, codigo, nombre]
                ListaDeCiudades.append(nuevaCiudad)
                codigosCiudadesValidos+=[codigo]
                print("La ciudad ha sido añadida")

            else:
                print("El codigo de ciudad ingresado ya existe")

        
    if opcion == "3":

        codigoPais = input("Ingrese el codigo de pais del cliente: ")
        codigoCiudad = input("Ingrese el codigo de ciudad del cliente: ")

        if codigoPais not in codigosPaisesValidos or codigoCiudad not in codigosCiudadesValidos:
            print("El codigo de pais o de ciudad no existe")

        else:
            IDCliente = input("Ingrese la ID del cliente a ingresar: ")

            if IDCliente not in codigosClientesValidos:
                nombreCliente = input("Ingrese el nombre del cliente a ingresar: ")
                direccion = input("Ingrese la direccion del cliente a ingresar: ")
                telefono = int(input("Ingrese el numero de telefono del cliente a ingresar: "))
                ultimoDiaVisita = int(input("Ingrese el ultimo dia de visita: "))
                ultimoMesVisita = int(input("Ingrese el ultimo mes de visita: "))
                ultimoAñoVisita = int(input("Ingrese el ultimo año de visita: "))
                saldo = int(input("Ingresa el saldo correspondiente al cliente: "))
                descuento = 0

                if 1 <= saldo <=99999:
                    descuento = 3

                elif saldo == 100000:
                    descuento = 5

                elif 101000 <= saldo <= 150000:
                    descuento = 10

                else:
                    descuento = 0
            
                nuevoCliente = [IDCliente, nombreCliente, direccion, codigoPais, codigoCiudad, telefono, ultimoDiaVisita, ultimoMesVisita, ultimoAñoVisita, descuento, saldo]
                ListaDeClientes.append(nuevoCliente)
                codigosClientesValidos+=[IDCliente]
                
                print("El cliente ha sido añadido")

            else:
                print("El codigo de cliente ingresado ya existe")


    if opcion == "4":

        IDCliente = input("Ingrese el ID del cliente dueño de la mascota: ")

        if IDCliente  not in codigosClientesValidos:
            print("El cliente no existe")

        else:

            IDAnimal = input("Ingrese el ID de la mascota a ingresar: ")

            if IDAnimal not in codigosMascotasValidos:

                nombre = input("Ingrese el nombre de la mascota a ingresar: ") 
                tipo = input("Ingrese el tipo de mascota a ingresar (canino, felino, etc...): ")
                raza = input("Ingrese la raza de la mascota: ")
                diaDeNacimiento = int(input("Ingrese el dia de nacimiento de la mascota: "))
                mesDeNacimiento = int(input("Ingrese el mes de nacimiento de la mascota: "))
                añoDeNacimiento = int(input("Ingrese el año de nacimiento de la mascota: "))
                sexo = input("Ingrese el sexo de la mascota: ")
                color = input("Ingrese el color de la mascota: ")
                castrado = input("Indique si la mascota esta castrada (Si/No): ")
                ultimoDiaVisita = int(input("Indique el ultimo dia de visita: "))
                ultimoMesVisita = int(input("Indique el ultimo mes de visita: "))
                ultimoAñoVisita = int(input("Indique el ultimo año de visita: "))

                
                nuevaMascota = [IDCliente, IDAnimal, nombre, tipo, raza, diaDeNacimiento, mesDeNacimiento,añoDeNacimiento, sexo, color, castrado, ultimoDiaVisita, ultimoMesVisita, ultimoAñoVisita]
                ListaDeMascotas.append(nuevaMascota)
                codigosMascotasValidos.append(IDAnimal)
                print("La mascota ha sido añadida")

            else:
                print("El ID del animal ya existe")


    if opcion == "5":

        IDVisita = input("Ingrese el ID de la visita a ingresar: ")

        if IDVisita in codigosVisitasValidos:
            print ("El ID de visita ya existe")

        else:
            IDAnimal = input("ingrese el ID de la mascota a ingresar: ")

            if IDAnimal in codigosMascotasValidos:

                ultimoDiaVisita = int(input("Ingrese el ultimo dia de visita: "))
                ultimoMesVisita = int(input("Ingrese el ultimo mes de visita: "))
                ultimoAñoVisita = int(input("Ingrese el ultimo año de visita: "))
                totalFactura = int(input("Ingrese el monto total de la factura: "))
                formaDePago = input("Ingrese la forma de pago (01 = Contado, 02 = Credito): ")

                nuevaVisita = [IDVisita, IDAnimal, ultimoDiaVisita, ultimoMesVisita, ultimoAñoVisita, totalFactura, formaDePago]
                ListaDeVisitas.append(nuevaVisita)
                codigosVisitasValidos.append(IDVisita)
                print("La visita ha sido añadida")

            else:
                print("No hay ninguna mascota con el ID ingresado")


    if opcion =="6":

        IDTratamiento = input("Ingrese el codigo de tratamiento a ingresar: ")

        if IDTratamiento in codigosTratamientosValidos:
            print("El codigo de tratamiento ya existe ")

        else:
            nombreTratamiento = input("Ingrese el nombre del tratamiento: ")
            precioUnitario = int(input("Ingrese el precio unitario del tratamiento: "))

            nuevoTratamiento = [IDTratamiento, nombreTratamiento, precioUnitario]
            ListaDeTratamientos.append(nuevoTratamiento)
            codigosTratamientosValidos.append(IDTratamiento)
            print("El tratamiento ha sido añadido")


    if opcion =="7":

        IDAnimal = input("Ingrese el ID de la mascota: ")

        if IDAnimal in codigosMascotasValidos:
            
            IDMedicacion = input("Ingrese el codigo de medicacion: ")
            ultimoDiaVisita = int(input("Ingrese el ultimo dia de visita: "))
            ultimoMesVisita = int(input("Ingrese el ultimo mes de visita: "))
            ultimoAñoVisita = int(input("Ingrese el ultimo año de visita: "))

            Flag = False

            for i in range (len(ListaDeMedicacion)):
                    
                    if IDMedicacion == ListaDeMedicacion[i][1] and ultimoDiaVisita == int(ListaDeMedicacion[i][2]) and ultimoMesVisita == int(ListaDeMedicacion[i][3]) and ultimoAñoVisita == int(ListaDeMedicacion[i][4]) and IDAnimal == ListaDeMedicacion[i][0]:
                        Flag = True
                        break

            if Flag == True:
                print("Ya existe una medicacion para esta mascota, en esta fecha")

            else:

                diaDeNacimiento = int(input("Ingrese el dia de nacimiento de la mascota: "))
                mesDeNacimiento = int(input("Ingrese el mes de nacimiento de la mascota: "))
                añoDeNacimiento = int(input("Ingrese el año de nacimiento de la mascota: "))

                if ultimoMesVisita == mesDeNacimiento and ultimoAñoVisita < añoDeNacimiento:
                    print("Las fechas de la ultima visita son invalidas")
                       

                elif ultimoMesVisita < mesDeNacimiento and ultimoAñoVisita == añoDeNacimiento:
                    print("Las fechas de la ultima visita son invalidas")
                            

                elif ultimoMesVisita < mesDeNacimiento and ultimoAñoVisita < añoDeNacimiento:
                    print("Las fechas de la ultima visita son invalidas")

                elif ultimoDiaVisita < diaDeNacimiento and ultimoMesVisita == mesDeNacimiento and ultimoAñoVisita == añoDeNacimiento:
                    print("Las fechas de la ultima visita son invalidas")

                else:

                    listaDeMedicamentos = input("Ingrese el medicamento: ")
                    costoUnitario = int(input("Ingrese el costo unitario del medicamento: "))
                    cantidad = int(input("Ingrese la cantidad del medicamento: "))

                    costoTotal = costoUnitario * cantidad

                    nuevaMedicacion = [IDAnimal, IDMedicacion, ultimoDiaVisita, ultimoMesVisita, ultimoAñoVisita, listaDeMedicamentos, costoUnitario, cantidad, costoTotal]
                    ListaDeMedicacion.append(nuevaMedicacion)
                    print("La medicacion ha sido añadida")
                    
        else:
            print ("El ID del animal no existe")


def menuConsultar ():

    while True:
         
        print ("Seleccione la busqueda que desea realizar:")
        print("1 = Paises")
        print("2 = Ciudades")
        print("3 = Clientes")
        print("4 = Mascotas")
        print("5 = Visitas")
        print("6 = Medicaciones")
        print("7 = Tratamientos")
        print("X = Volver al menu principal")

        opcion = input("Ingrese la opcion a buscar: ")

        if opcion == "1":
            codigoDePais = input("Escriba el codigo de pais a buscar: ")

            if codigoDePais in codigosPaisesValidos:
                for i in range(len(ListaDePaises)):
                    
                    if ListaDePaises[i][0] == codigoDePais:
                        print (ListaDePaises[i])
                        break
            else:
                print("El codigo de pais ingresado no existe")

        if opcion == "2":
            codigoDeCiudad = input("Escriba el codigo de ciudad a buscar: ")

            if codigoDeCiudad in codigosCiudadesValidos:
                for i in range(len(ListaDeCiudades)):

                    if ListaDeCiudades[i][1] == codigoDeCiudad:
                        print(ListaDeCiudades[i])
                        break
            else:
                print("El codigo de ciudad no existe")

        if opcion == "3":
            codigoDeCliente = input("Escriba el codigo de cliente a buscar: ")

            if codigoDeCliente in codigosClientesValidos:
                for i in range(len(ListaDeClientes)):

                    if ListaDeClientes[i][0] == codigoDeCliente:
                        print(ListaDeClientes[i])
                        break
            else:
                print("El codigo de cliente no existe")

        if opcion == "4":
            codigoDeMascota = input("Escriba el codigo de mascota a buscar: ")

            if codigoDeMascota in codigosMascotasValidos:
                for i in range(len(ListaDeMascotas)):

                    if ListaDeMascotas[i][1] == codigoDeMascota:
                        print(ListaDeMascotas[i])
                        break
            else:
                print("El codigo de mascota no existe")

        if opcion == "5":
            codigoDeVisita = input("Escriba el codigo de visita a buscar: ")

            if codigoDeVisita in codigosVisitasValidos:
                for i in range(len(ListaDeVisitas)):

                    if ListaDeVisitas[i][0] == codigoDeVisita:
                        print(ListaDeVisitas[i])
                        break
            else:
                print("El codigo de visita no existe")

        if opcion == "6":
            codigoDeMascota = input("Escriba el codigo de la mascota a buscar: ")

            if codigoDeMascota not in codigosMascotasValidos:
                print ("El codigo de mascota no existe")
            else:
                codigoDeMedicacion = input("Escriba el codigo de medicacion a buscar: ")

                if codigoDeMedicacion in codigosMedicacionValidos:
                    for i in range (len(ListaDeMedicacion)):

                        if ListaDeMedicacion[i][1] == codigoDeMedicacion:
                            print(ListaDeMedicacion[i])
                            break
                else:
                    print("El codigo de medicacion no existe")

        if opcion == "7":
            codigoDeTratamiento = input("Escriba el codigo de tratamiento a buscar: ")

            if codigoDeTratamiento in codigosTratamientosValidos:
                for i in range(len(ListaDeTratamientos)):

                    if ListaDeTratamientos[i][0] == codigoDeTratamiento:
                        print(ListaDeTratamientos[i])
                        break
            else:
                print("El codigo de tratamiento no existe")

        if opcion == "X" or "x":
            break


def menuModificar(): 

    global codigosPaisesValidos
    global codigosClientesValidos
    global codigosMascotasValidos
    global codigosCiudadesValidos
    global codigosMedicacionValidos
    global codigosVisitasValidos
    global codigosTratamientosValidos   


    while True:
        print("Selecciona la opcion a modificar:")
        print("1 = Modificar un pais")
        print("2 = Modificar una ciudad")
        print("3 = Modificar un cliente")
        print("4 = Modificar una mascota")
        print("5 = Modificar una visita")
        print("6 = Modificar un tratamiento")
        print("7 = Modificar una medicacion")
        print("X = Volver al menu principal\n")
        opcion = input("Ingrese el numero de la opcion de menu que desea modificar: ")      
    
        if opcion == "1":

            print("\nHa seleccionado modificar un pais\n")

            while True:     
                
                print("X = Para salir")
                flag = False
                codigo = input("Ingrese el codigo del pais que desea modificar: ")
    
                i = 0 

                if codigo == "X" or codigo == "x":
                    break
    
                for i in range (0,len(ListaDePaises)):

                    if int(codigo) == int(ListaDePaises[i][0]):
                        print(F"Ha seleccionado: {ListaDePaises[i]}\n")
                        flag = False
                        break

                    else:
                        flag = True
                         
                if flag == True:
                    print (F"El codigo del pais ingresado no es valido\n")
    

                if flag == False:
                    temp = i
                    nombre = input("Ingrese el nuevo nombre del pais selecionado: ")        
                    ListaDePaises[temp][1] = nombre 
                    print (F"Pais modificado: {ListaDePaises[temp]}\n")  
                    break
    
        if opcion == "2":

            print("\nHa seleccionado modificar una ciudad\n")

            while True:     
                
                print("X = Para salir")
                flag = False
                codigoPais = input("Ingrese el codigo del pais de la ciudad que desea modificar: ")

                i = 0
                
                if codigoPais == "X" or codigoPais == "x":
                    break
    
                for i in range (0,len(ListaDePaises)):

                    if int(codigoPais) == int(ListaDePaises[i][0]):
                        print(F"Ha seleccionado el pais: {ListaDePaises[i]}\n")
                        flag = False
                        break

                    else:
                        flag = True
                         
                if flag == True:
                    print (F"El codigo del pais ingresado no es valido\n")
                    
                if flag == False:
                    codigoCiudad = input("Ingrese el codigo de la ciudad que desea modificar: ")

                    i = 0

                    for i in range (0,len(ListaDeCiudades)):

                        if int(codigoPais) == int(ListaDeCiudades[i][0]) and int(codigoCiudad) == int(ListaDeCiudades[i][1]):
                            print(F"Ha seleccionado la ciudad: {ListaDeCiudades[i]}\n")
                            flag = False
                            break

                        else:
                            flag = True
                         
                if flag == True:
                    print (F"El codigo de ciudad ingresado no es valido\n")

                if flag == False:

                        temp = i

                        nombre = input("Ingrese el nuevo nombre de la ciudad selecionada: ")        
                        ListaDeCiudades[temp][2] = nombre 
                        print (F"La ciudad modificada: {ListaDeCiudades[temp]}\n")  
                        break
    
        if opcion == "3":
              
              print("\nHa seleccionado modificar un cliente\n")

              while True:     

                print("X = Para salir")
                flag = False
                codigo = input("Ingrese el codigo del cliente que desea modificar: ")
    
                if codigo == "X" or codigo == "x":
                    break

                i = 0 
    
                for i in range (0,len(ListaDeClientes)):

                    if int(codigo) == int(ListaDeClientes[i][0]):
                        print(F"Ha seleccionado: {ListaDeClientes[i]}\n")
                        flag = False
                        break

                    else:
                        flag = True
             
                if flag == True:
                    print (F"El codigo del cliente ingresado no es valido\n")
        
                if flag == False:
                    
                    temp = i

                    print("Selecciona el dato que desea modificar:")
                    print("1 = Modificar nombre")
                    print("2 = Modificar direccion")
                    print("3 = Modificar codigo de pais")
                    print("4 = Modificar codigo de ciudad")
                    print("5 = Modificar telefono")

                    while True:

                        print ("X = Para salir")
                        opcioncliente = input("Ingrese el numero de la opcion del cliente que desea modificar: ")    

                        if opcioncliente  == "1": 

                            nombre = input("Ingrese el nuevo nombre del cliente selecionado: ")        
                            ListaDeClientes[temp][1] = nombre 

                        if opcioncliente  == "2": 

                            direccion = input("Ingrese la nueva direccion del cliente selecionado: ") 

                            ListaDeClientes[temp][2] = direccion 

                        if opcioncliente  == "3": 

                            while True:

                                codpais =  input("Ingrese el nuevo codigo de pais del cliente selecionado: ") 

                                if codpais == "X" or codpais == "x":
                                    break

                                if codpais in codigosPaisesValidos:
                                    ListaDeClientes[temp][3] = codpais 
                                    break

                                else: 
                                    print(F"El codigo de pais ingresado no es valido")
                                    print("X = Para salir")

                        if opcioncliente  == "4": 

                             while True:

                                codciudad =  input("Ingrese el nuevo codigo de ciudad del cliente selecionado: ") 

                                if codciudad == "X" or codciudad == "x":
                                    break

                                if codciudad in codigosCiudadesValidos:
                                    ListaDeClientes[temp][3] = codciudad 
                                    break

                                else: 
                                    print(F"El codigo de ciudad ingresado no es valido")
                                    print("X = Para salir")

                        if opcioncliente  == "5": 

                            telefono = input("Ingrese el nuevo telefono del cliente selecionado: ")        
                            ListaDeClientes[temp][5] = telefono 

                        if opcioncliente  == "X" or opcioncliente  == "x": 

                            print(F"Los nuevos datos del cliente modificado: {ListaDeClientes[temp]}\n")
                            break

                    break
              
        if opcion == "4":
            
            print("\nHa seleccionado modificar una mascota\n")

            while True:

                flag = False
                numCliente = input("Ingrese el codigo del cliente de la mascota que desea modificar: ")

                i = 0

                if numCliente == "X" or numCliente == "x":
                    break


                for i in range (0,len(ListaDeClientes)):

                    if int(numCliente) == int(ListaDeClientes[i][0]):
                        print(F"Ha seleccionado el cliente: {ListaDeClientes[i]}\n")
                        flag = False
                        break
                    
                    else:
                        flag = True
                    
                if flag == True:
                    print (F"El numero de cliente ingresado no es valido\n")

                if flag == False:
                
                    flag == False
                    i = 0
                    idAnimal = input("Ingrese el codigo de la mascota que desea modificar: ")

                    for i in range (0,len(ListaDeMascotas)):

                        if int(numCliente) == int(ListaDeMascotas[i][0]) and int(idAnimal) == int(ListaDeMascotas[i][1]):
                            print(F"Ha seleccionado la mascota: {ListaDeMascotas[i]}\n")
                            flag == False
                            break
                        
                        else:
                            flag = True
           
                    temp = i

                    if flag == True:
                        print (F"El codigo de mascota ingresado no es valido o no pertenece a este cliente\n")

                    if flag == False:
                    
                        print("Selecciona el valor que desea modificar:")
                        print("1 = Modificar nombre")
                        print("2 = Modificar castrado(si/no)")

                        while True: 

                            print ("X = Para salir")
                            opcionmascota = input("Ingrese el numero de la opcion de mascota que desea modificar: ")    

                            if opcionmascota == "1":

                                nombreMascota = input("Ingrese el nuevo nombre de la mascota selecionada: ")        
                                ListaDeMascotas[temp][2] = nombreMascota 

                            if opcionmascota == "2":

                                while True:

                                    estadoMascota = input("Estado de castrado de la mascota selecionada (si/no): ")     

                                    if nombreMascota == "si" or nombreMascota == "Si":
                                        ListaDeMascotas[temp][10] = estadoMascota 
                                        break
                                    
                                    if nombreMascota == "no" or nombreMascota == "no":
                                        ListaDeMascotas[temp][10] = estadoMascota 
                                        break

                                    else:
                                        print("Por favor ingresar 'si' o 'no'")

                            if opcionmascota == "X" or opcionmascota == "x":
                                break
    
                        print(F"Los nuevos datos de la mascota modificados: {ListaDeMascotas[temp]}\n")
                        break
          
        if opcion == "5":

            print("\nHa seleccionado modificar una visita\n")    

            while True:

                flag = False
                idAnimal = input("Ingrese el codigo del animal que desea modificar: ")
                codVisita = input("Ingrese el codigo de visita que desea modificar: ")
                
                i = 0

                for i in range (0,len(ListaDeVisitas)):

                    if int(codVisita) == int(ListaDeVisitas[i][0]) and int(idAnimal) == int(ListaDeVisitas[i][1]) and idAnimal in codigosMascotasValidos:
                        print(F"Ha seleccionado la visita: {ListaDeVisitas[i]}\n")
                        flag = False
                        break
                    
                    else:
                        flag = True
        
                if  flag == True:
                    print (F"La visita ingresada no es valida\n")
                    
                if flag == False:
                    
                    temp = i

                    print("Modifique la nueva forma de pago")
                    print("01 = Contado")
                    print("02 = Credito")

                    while True:

                                metodoPago = input("Ingrese el nuevo metodo de pago: ")     

                                if metodoPago == "01":
                                    ListaDeVisitas[temp][6] = metodoPago 
                                    break
                                
                                if metodoPago == "02":
                                    ListaDeVisitas[temp][6] = metodoPago 
                                    break

                                else:
                                    print("Por favor ingresar '01' o '02'")

                    print (F"Visita modificada: {ListaDeVisitas[temp]}\n")  
                    break
                
        if opcion == "6":
             
            print("\nHa seleccionado modificar un tratamiento\n")

            while True:     
            
                flag = False
                codigoTratamiento = input("Ingrese el codigo del tratamiento que desea modificar: ")
    
                i = 0 
    
                for i in range (0,len(ListaDeTratamientos)):

                    if int(codigoTratamiento) == int(ListaDeTratamientos[i][0]):
                        print(F"Ha seleccionado: {ListaDeTratamientos[i]}\n")
                        flag = False
                        break

                    else:
                        flag = True
              
                if flag == True:
                    print (F"El codigo del tratamiento ingresado no es valido\n")

                if flag == False:
                    temp = i
                    precio = input("Ingrese el nuevo precio del tratamiento selecionado: ")        
                    ListaDeTratamientos[temp][2] = precio 
                    print (F"Tratamiento modificado: {ListaDeTratamientos[temp]}\n")  
                    break

        if opcion == "7":
        
            print("\nHa seleccionado modificar una medicacion\n")

            while True:     
            
                flag = False

                idAnimal = input("Ingrese el codigo de la mascota que desea modificar: ")
                codMedicacion = input("Ingrese el codigo de la medicacion que desea modificar: ")
              
                i = 0 
    
                for i in range (0,len(ListaDeMedicacion)):

                    if int(codMedicacion) == int(ListaDeMedicacion[i][1]) and int(idAnimal) == int(ListaDeMedicacion[i][0]) and idAnimal in codigosMascotasValidos:
        
                        print(F"Ha seleccionado: {ListaDeMedicacion[i]}\n")
                        flag = False
                        break

                    else:
                        flag = True

                temp = i

                if flag == True:
                        print (F"El codigo de medicacion o codigo de la mascota ingresado no es valido\n")                    
        
                if flag == False:
                    
                    print("Ingrese el numero del dato que desea modificar:")
                    print("1 = Cantidad")
                    print("2 = Precio")
                    print("3 = Coste total")

                    while True:

                        print ("X = Para salir")
                        opcionmedicacion = input("Ingrese el numero de la opcion de medicacion que desea modificar: ")

                        if opcionmedicacion == "1":

                            cantidad = input("Ingrese la nueva cantidad del medicamento: ")
                            ListaDeMedicacion[temp][7] = cantidad

                        if opcionmedicacion == "2":

                            Precio = input("Ingrese el nuevo precio del medicamento: ")
                            ListaDeMedicacion[temp][6] = Precio

                        if opcionmedicacion == "3":

                            costeTotal = input("Ingrese el nuevo precio del medicamento: ")
                            ListaDeMedicacion[temp][8] = costeTotal

                        if opcionmedicacion == "X" or opcionmedicacion == "x":
                            break
                    
                    print (F"Medicacion modificada: {ListaDeMedicacion[temp]}\n")  
                    break
    
        if opcion == "X" or opcion == "x":
            break

def menuEliminar ():

    while True:

        print("Seleccione el dato a eliminar")
        print("1 = Eliminar un pais")
        print("2 = Eliminar una ciudad")
        print("3 = Eliminar un cliente")
        print("4 = Eliminar una mascota")
        print("5 = Eliminar una visita")
        print("6 = Eliminar un tratamiento")

        opcion = input("Escriba la opcion a eliminar: ")

        if opcion == "1":

            paisEliminar = input("Escriba el codigo del pais a eliminar: ")

            if paisEliminar not in codigosPaisesValidos:
                print ("El codigo de pais ingresado no existe")
            else:
                for i in range(len(ListaDePaises)):
                    if ListaDePaises[i][0] == paisEliminar:
                        ListaDePaises.pop(i)
                        break

                for i in range (len(codigosPaisesValidos)):
                    if codigosPaisesValidos[i] == paisEliminar:
                        codigosPaisesValidos.pop(i)
                        break
                print("El pais ha sido eliminado con exito")

        if opcion == "2":

            ciudadEliminar = input('Escriba el codigo de la ciudad a eliminar: ')
            ciudadesEditar = []

            if ciudadEliminar not in codigosCiudadesValidos:
                print("El codigo de pais ingresado no existe")
            else:
                for i in range(len(ListaDeCiudades)):
                    if ListaDeCiudades[i][1] == ciudadEliminar:
                        ListaDeCiudades.pop(i)
                        break
                
                for i in range (len(ListaDeClientes)):
                    if ListaDeClientes[i][4] == ciudadEliminar:
                        ciudadesEditar.append(ListaDeClientes[i])

                for i in range (len(ciudadesEditar)):
                    print(f"{ciudadesEditar[i]} pertenece a la ciudad eliminada")
                    ciudadEditada = input("Escriba el codigo de la ciudad a remplazar: ")

                    if ciudadEditada in codigosCiudadesValidos:
                        ListaDeClientes[i][4] = ciudadEditada
                        print ("La ciudad ha sido remplazada con exito")
                
                for i in range (len(codigosCiudadesValidos)):
                    if codigosCiudadesValidos[i] == ciudadEliminar:
                        codigosCiudadesValidos.pop(i)
                        break

        if opcion == "3":

            clienteEliminar = input("Escriba el ID del cliente a eliminar: ")

            if clienteEliminar not in codigosClientesValidos:
                print("El ID de cliente ingresado no existe")
            else:
                for i in range (len(ListaDeClientes)):
                    if ListaDeClientes[i][0] == clienteEliminar:
                        ListaDeClientes.pop(i)
                        break

                for i in range (len(codigosClientesValidos)):
                    if codigosClientesValidos[i] == clienteEliminar:
                        codigosClientesValidos.pop(i)
                        break
                print("El cliente ha sido eliminado con exito")

        if opcion == "4":

            mascotaEliminar = input("Ingrese el ID de la mascota a eliminar: ")

            if mascotaEliminar not in codigosMascotasValidos:
                print("El ID de mascota ingresado no existe")
            else:
                for i in range(len(ListaDeMascotas)):
                    if ListaDeMascotas[i][1] == mascotaEliminar:
                        ListaDeMascotas.pop(i)
                        break

                for i in range(len(codigosMascotasValidos)):
                    if codigosMascotasValidos[i] == mascotaEliminar:
                        codigosMascotasValidos.pop(i)
                        break
                print("La mascota ha sido eliminada con exito")

        if opcion == "5":

            visitaEliminar = input("Ingrese el codigo de visita a eliminar: ")

            if visitaEliminar not in codigosVisitasValidos:
                print("El codigo de visita ingresado no existe")
            else:
                for i in range(len(ListaDeVisitas)):
                    if ListaDeVisitas[i][0] == visitaEliminar:
                        ListaDeVisitas.pop(i)
                        break

                for i in range(len(codigosVisitasValidos)):
                    if codigosVisitasValidos[i] == visitaEliminar:
                        codigosVisitasValidos.pop(i)
                        break
                print ("La visita ha sido eliminada con exito")

        if opcion == "6":

            tratamientoEliminar = input("Ingrese el codigo de tratamiento a eliminar: ")

            if tratamientoEliminar not in codigosTratamientosValidos:
                print ("El codigo de tratamiento ingresado no existe")
            else:
                for i in range(len(ListaDeTratamientos)):
                    if ListaDeTratamientos[i][0] == tratamientoEliminar:
                        ListaDeTratamientos.pop(i)
                        break
                
                for i in range(len(codigosTratamientosValidos)):
                    if codigosTratamientosValidos[i] == tratamientoEliminar:
                        codigosTratamientosValidos.pop(i)
                        break
                print("El tratamiento ha sido eliminado con exito")
                    
        if opcion == "X" or "x":
            break
        

def menuReportes():

    archivo = open("Reportes.txt", "x")
    archivo.write(F"Reportes solicitados:")

    while True:

        print("Selecciona la opcion que desea agregar al reporte:\n")

        print("1 = Reporte paises")
        print("2 = Reporte ciudades de un pais")
        print("3 = Reporte clientes")
        print("4 = Reporte mascotas de un cliente")
        print("5 = Reporte visitas de una mascota")
        print("6 = Reporte tratamientos")
        print("7 = Reporte ultima medicacion de una mascota")
        print("8 = Reporte cliente con mas saldo")
        print("9 = Reporte clientes de credito")
        print("10 = Reporte clientes con mas descuento")
        print("11 = Reporte ultimo tratamiento")
        print("12 = Reporte tratamiento mas utilizado")
        print("X = Volver al menu principal\n")

        opcion = input("Ingrese el numero de la opcion de menu que desea agregar al reporte: ")      
    
        if opcion == "1":

            archivo = open("Reportes.txt", "a")

            i = 0

            print("\n'Se ha añadido la lista de paises al reporte'\n")

            archivo.write(F"\n\n'Reporte: Lista de paises'\n\n")

            for i in range(0,len(ListaDePaises)):
                archivo.write(F"{ListaDePaises[i]}\n")
            
            archivo.close()

        if opcion == "2":

            archivo = open("Reportes.txt", "a")
            
            while True:

                print("X = Para salir")
                i = 0
                flag = False

                codigoPais = input("Ingrese el codigo de pais de las ciudad que desea añadir al reporte: ")

                if codigoPais == "X" or codigoPais == "x":
                    archivo.close()
                    break
    
                for i in range(0,len(ListaDePaises)):
                    
                    if int(codigoPais) == int(ListaDePaises[i][0]):

                        print(F"\n'Se han añadido las ciudades de ({str(ListaDePaises[i][0])},{str(ListaDePaises[i][1])}) al reporte'\n")
                        flag = False
                        break

                    else:
                        flag = True
                
                if flag == True:
                    print (F"El codigo del pais ingresado no es valido\n")

                if flag == False:

                    archivo.write(F"\n\n'Reporte: Lista de ciudades de ({str(ListaDePaises[i][0])},{str(ListaDePaises[i][1])})'\n\n")

                    for i in range(0,len(ListaDeCiudades)):
                        
                        if int(codigoPais) == int(ListaDeCiudades[i][0]):
                            archivo.write(F"{ListaDeCiudades[i]}\n")
                    
                    archivo.close()
                    break
        
        if opcion == "3":

            archivo = open("Reportes.txt", "a")

            i = 0

            print("\n'Se ha añadido la lista de clientes al reporte'\n")

            archivo.write(F"\n\n'Reporte: Lista de clientes'\n\n")

            for i in range(0,len(ListaDeClientes)):
                archivo.write(F"{ListaDeClientes[i]}\n")
            
            archivo.close()

        if opcion == "4":

            archivo = open("Reportes.txt", "a")
            
            while True:

                print("X = Para salir")
                i = 0
                flag = False

                codigCliente = input("Ingrese el codigo del cliente de las mascotas que desea añadir al reporte: ")

                if codigCliente == "X" or codigCliente == "x":
                    archivo.close()
                    break
    
                for i in range(0,len(ListaDeClientes)):
                    
                    if int(codigCliente) == int(ListaDeClientes[i][0]):

                        print(F"\n'Se han añadido las mascotas de ({str(ListaDeClientes[i][0])},{str(ListaDeClientes[i][1])}) al reporte'\n")
                        flag = False
                        break

                    else:
                        flag = True
                
                if flag == True:
                    print (F"El codigo de cliente ingresado no es valido\n")

                if flag == False:

                    archivo.write(F"\n\n'Reporte: Lista de mascotas de ({str(ListaDeClientes[i][0])},{str(ListaDeClientes[i][1])})'\n\n")

                    for i in range(0,len(ListaDeMascotas)):
                        
                        if int(codigCliente) == int(ListaDeMascotas[i][0]):
                            archivo.write(F"{ListaDeMascotas[i]}\n")
                    
                    archivo.close()
                    break

        if opcion == "5":
            
            archivo = open("Reportes.txt", "a")
            
            while True:

                print("X = Para salir")
                i = 0
                flag = False

                codigoMascota = input("Ingrese el codigo de la mascota de las visitas que desea añadir al reporte: ")

                if codigoMascota == "X" or codigoMascota == "x":
                    archivo.close()
                    break
    
                for i in range(0,len(ListaDeMascotas)):
                    
                    if int(codigoMascota) == int(ListaDeMascotas[i][1]):

                        print(F"\n'Se han añadido las visitas de ({str(ListaDeMascotas[i][1])},{str(ListaDeMascotas[i][2])}) al reporte'\n")
                        flag = False
                        break

                    else:
                        flag = True
                
                if flag == True:
                    print (F"El codigo de mascota ingresado no es valido\n")

                if flag == False:

                    archivo.write(F"\n\n'Reporte: Lista de visitas de ({str(ListaDeMascotas[i][1])},{str(ListaDeMascotas[i][2])})'\n\n")

                    for i in range(0,len(ListaDeVisitas)):
                        
                        if int(codigoMascota) == int(ListaDeVisitas[i][1]):
                            archivo.write(F"{ListaDeVisitas[i]}\n")
                    
                    archivo.close()
                    break
        
        if opcion == "6":

            archivo = open("Reportes.txt", "a")

            i = 0

            print("\n'Se ha añadido la lista de tratamientos al reporte'\n")

            archivo.write(F"\n\n'Reporte: Lista de tratamientos'\n\n")

            for i in range(0,len(ListaDeTratamientos)):
                archivo.write(F"{ListaDeTratamientos[i]}\n")
            
            archivo.close()

        if opcion == "7":

            archivo = open("Reportes.txt", "a")

            while True:
            
                print("X = Para salir")
                listTemp = []
                listFechas = []
                posicionReciente = 0
                i = 0
                temp = 0
                flag = False

                codigoMascota = input("Ingrese el codigo de la mascota de las visitas que desea añadir al reporte: ")

                if codigoMascota == "X" or codigoMascota == "x":
                    archivo.close()
                    break
                
                for i in range(0,len(ListaDeMascotas)):

                    if int(codigoMascota) == int(ListaDeMascotas[i][1]):
                    
                        print(F"\n'Se han añadido la ultima medicacion de ({str(ListaDeMascotas[i][1])},{str(ListaDeMascotas[i][2])}) al reporte'\n")
                        flag = False
                        break
                    
                    else:
                        flag = True

                if flag == True:
                    print (F"El codigo de mascota ingresado no es valido\n")

                if flag == False:

                    archivo.write(F"\n\n'Reporte: Ultima medicacion de ({str(ListaDeMascotas[i][1])},{str(ListaDeMascotas[i][2])})'\n\n")

                    for i in range(0,len(ListaDeMedicacion)):

                        if int(codigoMascota) == int(ListaDeMedicacion[i][0]):
                            listTemp += [ListaDeMedicacion[i]]

                    for i in range(0,len(listTemp)):
                    
                        listFechas += [listTemp[i][4] + listTemp[i][3] + listTemp[i][2]]

                    for i in range(0,len(listFechas)):

                        if int(listFechas[i]) > temp:
                            temp = int(listFechas[i])
                            posicionReciente = i 

                    archivo.write(F"{listTemp[posicionReciente]}\n")

                    archivo.close()
                    break

        if opcion == "8":

            archivo = open("Reportes.txt", "a")

            i = 0
            temp = 0
            posicionMayor = i 
            listSaldo = []
            listMascota = []

            print("\n'Se ha añadido el cliente con mas saldo al reporte'\n")

            archivo.write(F"\n\n'Reporte: Cliente con mas saldo'\n")

            for i in range(0,len(ListaDeMedicacion)):
            
                if int(ListaDeMedicacion[i][8]) > temp:
                    posicionMayor = i 
                    temp = int(ListaDeMedicacion[i][8])

            listSaldo += ListaDeMedicacion[posicionMayor]

            for i in range(0,len(ListaDeMascotas)):
            
                if int(listSaldo[0]) == int(ListaDeMascotas[i][1]):
                    listMascota += ListaDeMascotas[i]
   
            for i in range(0,len(ListaDeClientes)):
            
                if int(listMascota[0]) == int(ListaDeClientes[i][0]):
                    archivo.write(F"{ListaDeClientes[i]}\n")
       
            archivo.close()

        if opcion == "9":

            archivo = open("Reportes.txt", "a")

            i = 0
            listIdAnimal = []
            listNumCliente = []
            ListClientesCred = []

            print("\n'Se ha añadido la lista de clientes de credito al reporte'\n")

            archivo.write(F"\n\n'Reporte: Lista de clientes de credito'\n\n")

            for i in range(0,len(ListaDeVisitas)):
            
                credito = int(ListaDeVisitas[i][1])

                if ListaDeVisitas[i][6] == "02" and credito not in listIdAnimal:
                    listIdAnimal += [int(ListaDeVisitas[i][1])]

            for i in range(0,len(ListaDeMascotas)):
            
                for j in range(0,len(listIdAnimal)):
                
                    if int(listIdAnimal[j]) == int(ListaDeMascotas[i][1]):
                    
                        NumCliente = int(ListaDeMascotas[i][0])

                        if NumCliente not in listNumCliente:
                            listNumCliente += [int(ListaDeMascotas[i][0])]

            for i in range(0,len(ListaDeClientes)):
            
                for j in range(0,len(listNumCliente)):
                
                    if int(listNumCliente[j]) == int(ListaDeClientes[i][0]):
                    
                            ListClientesCred += [ListaDeClientes[i]]

            for i in range(0,len(ListClientesCred)):
                archivo.write(F"{ListClientesCred[i]}\n")

            archivo.close()

        if opcion == "10":

            archivo = open("Reportes.txt", "a")

            i = 0
            posicionMayor = 0
            temp = 0

            print("\n'Se ha añadido el cliente con mas descuento al reporte'\n")

            archivo.write(F"\n\n'Reporte: Cliente con mas descuento'\n\n")

            for i in range(0,len(ListaDeClientes)):
                
                if int(ListaDeClientes[i][10]) > temp:
                    posicionMayor = i 
                    temp = int(ListaDeClientes[i][10])

            archivo.write(F"{ListaDeClientes[posicionMayor]}\n")
            
            archivo.close()

        if opcion == "11":

            archivo = open("Reportes.txt", "a")

            listTemp = []
            listFechas = []
            posicionReciente = 0
            i = 0
            temp = 0

            print("\n'Se ha añadido el ultimo tratamiento al reporte'\n")

            archivo.write(F"\n\n'Reporte: Ultimo tratamiento'\n\n")

            for i in range(0,len(ListaDeMedicacion)):
            
                listTemp += [ListaDeMedicacion[i]]

            for i in range(0,len(listTemp)):

                listFechas += [listTemp[i][4] + listTemp[i][3] + listTemp[i][2]]

            for i in range(0,len(listFechas)):
            
                if int(listFechas[i]) > temp:
                    temp = int(listFechas[i])
                    posicionReciente = i 

            for i in range(0,len(ListaDeTratamientos)):
            
                if int(ListaDeTratamientos[i][0]) == int(listTemp[posicionReciente][5]):
                    archivo.write(F"{listTemp[posicionReciente]}, se aplico {ListaDeTratamientos[i]}\n")
                    break

            archivo.close()

        if opcion == "12":


            i = 0
            j = 0
            listTemp = [[]]
            temp = 0


            archivo = open("Reportes.txt", "a")

            print("\n'Se ha añadido el tratamiento mas utilizado al reporte'\n")

            archivo.write(F"\n\n'Reporte: Tratamiento mas utilizado'\n\n")

            for i in range(0,len(ListaDeMedicacion)):

                for j in range(0,len(listTemp)):

                    flag = True

                    if int(ListaDeMedicacion[i][5]) not in listTemp[j]:
                        flag = False
                    
                    if int(ListaDeMedicacion[i][5]) in listTemp[j]:
                        listTemp[j].append(int(ListaDeMedicacion[i][5]))
                        break

                    if flag == False:
                        listTemp += ([[int(ListaDeMedicacion[i][5])]])


            for i in range(1,len(listTemp)):
                            
                            if len(listTemp[i]) > temp:
                                posicionMayor = i 
                                temp = len(listTemp[i])

            masUtilizado = int(listTemp[posicionMayor][0])

            for i in range(0,len(ListaDeTratamientos)):
            
                if masUtilizado == int(ListaDeTratamientos[i][0]):
                    archivo.write(F"{ListaDeTratamientos[i]}\n")

            archivo.close()

        if opcion == "X" or opcion == "x":
            archivo.close()
            break

        
def mainMenu ():

    while True:

        print ("Bienvenido a la base de datos")
        print ("Seleccione la opción que desee")
        print ("1 = Leer archivos")
        print ("2 = Consultar datos")
        print ("3 = Modificar datos")
        print ("4 = Insertar datos")
        print ("5 = Eliminar datos")
        print ("6 = Escribir reportes")
        print ("X = Salir del programa")

        opcion = input("Ingrese el numero de la opcion: ")

        if opcion == "1":
            menuLeer()

        elif opcion == "2":
            menuConsultar()

        elif opcion == "3":
            menuModificar()

        elif opcion == "4":
            menuInsertar()

        elif opcion == "5":
            menuEliminar()

        elif opcion == "6":
            menuReportes()

        elif opcion == "X" or "x" :
            break

        else:
            print("Seleccione una opcion valida")

mainMenu()'''







