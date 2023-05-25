from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from Utils.VentanasFacturas import facturados

from tkinter import *
from tkinter import messagebox as MessageBox

reportesSolicitados = []

'''print("Selecciona la opcion que desea agregar al reporte:\n")

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
        print("12 = Reporte tratamiento mas utilizado")'''

def menuReportes():

    ventanaGeneral = Tk()
    ventanaGeneral.title("Reportes")
    ventanaGeneral.geometry("300x700")

    princLabel = Label(ventanaGeneral,text="Seleccione la opcion que desea agregar al reporte")
    princLabel.pack(padx=10)

    paises = Button(ventanaGeneral, text="Paises",command=lambda:[reportePaises(),ventanaGeneral.destroy()])
    paises.pack(padx=10,pady=8)

    ciudades = Button(ventanaGeneral, text="Ciudades de un pais",command=lambda:[reporteCiudades()])
    ciudades.pack(padx=10, pady=8)

    clientes = Button(ventanaGeneral,text="Clientes",command=lambda:[reporteClientes(),ventanaGeneral.destroy()])
    clientes.pack(padx=10,pady=8)

    mascotas = Button(ventanaGeneral,text="Mascotas de un cliente",command=lambda:[reporteMascotasCliente()])
    mascotas.pack(padx=10,pady=8)

    visitas = Button(ventanaGeneral, text="Visitas de una mascota",command=lambda:[reporteVisitas()])
    visitas.pack(padx=10,pady=8)

    tratamientos = Button(ventanaGeneral, text="Tratamientos",command=lambda:[reporteTratamientos(),ventanaGeneral.destroy()])
    tratamientos.pack(padx=10,pady=8)

    ultMed = Button(ventanaGeneral,text='Ultima medicacion de una mascota',command=lambda:[reporteTratamientosMascota(),ventanaGeneral.destroy()])
    ultMed.pack(padx=10,pady=8)

    saldo = Button(ventanaGeneral,text="Cliente con mas saldo",command=lambda:[reporteSaldo(),ventanaGeneral.destroy()])
    saldo.pack(padx=10,pady=8)

    credito = Button (ventanaGeneral,text="Clientes con credito",command=lambda:[reporteCredito(),ventanaGeneral.destroy()])
    credito.pack(padx=10,pady=8)

    descuento = Button(ventanaGeneral,text="Clientes con mas descuento",command=lambda:[reporteDescuento(),ventanaGeneral.destroy()])
    descuento.pack(padx=10,pady=8)

    ultTreat = Button(ventanaGeneral,text="Ultimo tratamiento usado",command=lambda:[reporteUltimoTratamiento(),ventanaGeneral.destroy()])
    ultTreat.pack(padx=10,pady=8)

    mostTreat = Button(ventanaGeneral,text="Tratamiento mas utilizado",command=lambda:[reporteTratamientoUsado(),ventanaGeneral.destroy()])
    mostTreat.pack(padx=10,pady=8)

    masFacturado = Button(ventanaGeneral,text="Cliente que mas facturó",command=lambda:[reporteFacturas(),ventanaGeneral.destroy()])
    masFacturado.pack(padx=10,pady=8)

    def reportePaises():

        MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")

        archivo = open("Reportes.txt", "a")

        archivo.write(F"\n\nReporte: Lista de paises\n\n")

        for i in range(0,len(ListaDePaises)):
            archivo.write(F"{ListaDePaises[i]}\n")
            
        archivo.close()

        reportesSolicitados.append('Reportes de paises')

    def reporteCiudades():

        archivo = open("Reportes.txt", "a")
            
        ventanaCiudades = Tk()
        ventanaCiudades.title("Reportes de ciudades")
        ventanaCiudades.geometry("300x300")

        label = Label(ventanaCiudades,text="Ingrese el codigo de pais para generar el reporte")
        label.pack(padx=10)
        entry = Entry(ventanaCiudades, width=200)
        entry.pack(padx=10,pady=10)
        sendCode = Button(ventanaCiudades,text="Generar reporte",command=lambda:[reporteCiudadGenerado(),ventanaCiudades.destroy()])
        sendCode.pack(padx=10,pady=8)

        def reporteCiudadGenerado():

                codigoPais = entry.get()

                if codigoPais not in codigosPaisesValidos:
                    MessageBox.showerror('Error',"El codigo de pais ingresado no existe")
                else:
                    
                    for i in range(len(ListaDePaises)):

                        if ListaDePaises[i][0] == codigoPais:
                            archivo.write(f"\nReporte de ciudades del pais {ListaDePaises[i]}:\n\n")
                            break
                
                    for i in range(len(ListaDeCiudades)):
                             
                        if ListaDeCiudades[i][0] == codigoPais:
                            archivo.write(f"{ListaDeCiudades[i]}\n")

                    MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")
                    archivo.close()
                    reportesSolicitados.append(f"Reporte de ciudades del pais codigo {codigoPais}")

    def reporteClientes(): #Escribir toda la lista de clientes

        archivo = open("Reportes.txt", "a")

        MessageBox.showinfo("Reportes",'El reporte ha sido generado')

        archivo.write(F"\n\nReporte: Lista de clientes:\n\n")

        for i in range(len(ListaDeClientes)):
            archivo.write(f"{ListaDeClientes[i]}\n")

        archivo.close()
        reportesSolicitados.append('Reporte de clientes')

    def reporteMascotasCliente(): #Escribir las mascotas de un cliente

        archivo = open("Reportes.txt", "a")

        ventana = Tk()
        ventana.title("Reportes")
        ventana.geometry("300x300")

        label = Label(ventana, text="Ingrese el codigo de cliente para generar el reporte")
        label.pack(padx=10)
        entry = Entry(ventana, width=200)
        entry.pack(padx=10,pady=8)
        sendInfo = Button(ventana,text="Generar reporte",command=lambda:[reporteMascClientGenerado(),ventana.destroy()])
        sendInfo.pack(padx=10,pady=8)

        def reporteMascClientGenerado():

            codigoCliente = entry.get()

            if codigoCliente not in codigosClientesValidos:
                MessageBox.showerror('Error',"El codigo de cliente ingresado no existe")
            else:

                for i in range(len(ListaDeClientes)):

                    if ListaDeClientes[i][0] == codigoCliente:
                        archivo.write(f"\nReporte de mascotas del cliente {ListaDeClientes[i][1]}:\n")
                        break

                for i in range (len(ListaDeMascotas)):

                    if ListaDeMascotas[i][0] == codigoCliente:
                        archivo.write(f"{ListaDeMascotas[i]}\n")

                MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")
                archivo.close()
                reportesSolicitados.append(f'Reporte de mascotas del cliente codigo {codigoCliente}')

    def reporteVisitas():

        archivo = open("Reportes.txt", "a")

        ventana = Tk()
        ventana.title('Reporte de visitas')
        ventana.geometry("300x300")

        label = Label(ventana, text="Ingrese el codigo de mascota para generar el reporte")
        label.pack(padx=10,pady=8)
        entry = Entry(ventana,width=200)
        entry.pack(padx=10,pady=8)
        sendInfo = Button(ventana,text="Generar reporte",command=lambda:[reporteVisitasGenerado(),ventana.destroy()])
        sendInfo.pack(padx=10,pady=8)

        def reporteVisitasGenerado():

            codigoMascota = entry.get()

            if codigoMascota not in codigosMascotasValidos:
                MessageBox.showerror('Error','El codigo ingresado no existe')
            else:

                archivo.write(f"\n\nReporte de visitas de la mascota codigo: {codigoMascota}\n\n")

                for i in range(len(ListaDeVisitas)):

                    if ListaDeVisitas[i][1] == codigoMascota:

                        archivo.write(f"{ListaDeVisitas[i]}\n")

                MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")
                archivo.close()
                reportesSolicitados.append(f'Reporte de las visitas de la mascota codigo {codigoMascota}')
 
    def reporteTratamientos():

        MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")

        archivo = open("Reportes.txt", "a")


        archivo.write(F"\n\nReporte: Lista de tratamientos\n\n")

        for i in range(0,len(ListaDeTratamientos)):
            archivo.write(F"{ListaDeTratamientos[i]}\n")
            
        archivo.close()
        reportesSolicitados.append("Reporte de tratamientos")

    def reporteTratamientosMascota():

        ventana = Tk()
        ventana.title("Reportes")
        ventana.geometry("300x300")

        label = Label(ventana,text="Ingrese el codigo de mascota para generar el reporte")
        label.pack(padx=10)
        entry = Entry(ventana,width=200)
        entry.pack(padx=10,pady=8)
        sendInfo = Button(ventana,text="Generar reporte",command=lambda:[reporteTratamientoMascotaGenerado(),ventana.destroy()])
        sendInfo.pack(padx=10,pady=8)

        def reporteTratamientoMascotaGenerado():

            archivo = open("Reportes.txt", "a")

            codigoMascota = entry.get()

            if codigoMascota not in codigosMascotasValidos:
                MessageBox.showerror("Error","El codigo ingresado no existe")
            else:

                while True:
            
                    listTemp = []
                    listFechas = []
                    posicionReciente = 0
                    i = 0
                    temp = 0
                    flag = False
                 
                    for i in range(0,len(ListaDeMascotas)):

                        if (codigoMascota) == (ListaDeMascotas[i][1]):
                        
                            MessageBox.showinfo("Reportes",F"\n'Se han añadido la ultima medicacion de ({str(ListaDeMascotas[i][1])},{str(ListaDeMascotas[i][2])}) al reporte'\n")
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
                        reportesSolicitados.append(f"Reporte de tratamientos de la mascota codigo {codigoMascota}")
                        break

    def reporteSaldo(): #Escribir cliente con mas saldo

        MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")

        archivo = open("Reportes.txt", "a")

        archivo.write(f"\n\nCliente con mas saldo: ")
        
        maxSaldo = []
        maxCliente = []

        for i in range(len(ListaDeClientes)):

            if maxSaldo == [] and maxCliente == []:

                maxSaldo = ListaDeClientes[i][10]
                maxCliente = ListaDeClientes[i][0]

                print(maxSaldo, maxCliente)

            else:
                maxComparacion = int(maxSaldo)
                currentSaldo = int(ListaDeClientes[i][10])

                if maxComparacion < currentSaldo:

                    maxSaldo = ListaDeClientes[i][10]
                    maxCliente = ListaDeClientes[i][0]

        archivo.write(f"El cliente con mas saldo es el cliente codigo {maxCliente}, con un saldo total de: {maxSaldo}")
        reportesSolicitados.append("Reporte de cliente con mas saldo")

    def reporteCredito(): #Escribir clientes que paguen con credito (ListaDeVisitas 02)

        archivo = open("Reportes.txt", "a")

        i = 0
        listIdAnimal = []
        listNumCliente = []
        ListClientesCred = []

        MessageBox.showinfo("Reportes","'Se ha añadido la lista de clientes de credito al reporte'")

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
        reportesSolicitados.append("Reporte de clientes de credito")

    def reporteDescuento():

        archivo = open("Reportes.txt", "a")
        mayorDescuento = 0

        MessageBox.showinfo('Reportes',"Se ha añadido el cliente con mas descuento al reporte")

        archivo.write(F"\n\n'Reporte: Clientes con mas descuento'\n\n")

        for i in range (len(ListaDeClientes)):

            if mayorDescuento == 0:
                mayorDescuento = ListaDeClientes[i][9]

            else:
                comparable = ListaDeClientes[i][9]

                if int(mayorDescuento) < int(comparable):
                    mayorDescuento = int(ListaDeClientes[i][9])


        for i in range(0,len(ListaDeClientes)):
                
            if (ListaDeClientes[i][9]) == mayorDescuento:

                archivo.write(f"{ListaDeClientes[i]}\n")

        archivo.close()
        reportesSolicitados.append("Reporte de clientes con mas descuento")
        
    def reporteUltimoTratamiento():

        archivo = open("Reportes.txt", "a")

        listTemp = []
        listFechas = []
        posicionReciente = 0
        temp = 0

        MessageBox.showinfo('Reportes',"Se ha añadido el ultimo tratamiento al reporte")

        archivo.write(F"\n\nReporte: Ultimo tratamiento\n\n")

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
        reportesSolicitados.append("Reporte del ultimo tratamiento usado")

    def reporteTratamientoUsado():


        listTemp = [[]]
        temp = 0
        archivo = open("Reportes.txt", "a")

        MessageBox.showinfo('Reportes',"Se ha añadido el tratamiento mas utilizado al reporte\n")

        archivo.write(F"\nReporte: Tratamiento mas utilizado\n\n")

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
                archivo.write(F"{ListaDeTratamientos[i]}\n\n")

        archivo.close()
        reportesSolicitados.append("Reporte del tratamiento mas usado")

    def reporteFacturas():

        global facturados
        frecuencias = {}

        MessageBox.showinfo('Reportes',"El reporte ha sido generado con exito")

        archivo = open("Reportes.txt", "a")

        archivo.write(F"\nReporte: Cliente que mas facturo:\n\n")

        for elemento in facturados:
            if elemento in frecuencias:
                frecuencias[elemento] += 1
            else:
                frecuencias[elemento] = 1

                elemento_mas_repetido = None
                max_repeticiones = 0
                for elemento, repeticiones in frecuencias.items():
                    if repeticiones > max_repeticiones:
                        max_repeticiones = repeticiones
                        elemento_mas_repetido = elemento

                archivo.write(f"El cliente que mas facturo es el cliente codigo: {elemento_mas_repetido}")
                reportesSolicitados.append("Reporte del cliente que mas facturó")
                break
            
        archivo.close()

    ventanaGeneral.mainloop()

def verReportesSolicitados():

    MessageBox.showinfo('Reportes solicitados',f"Los reportes solicitados son\n{reportesSolicitados}")