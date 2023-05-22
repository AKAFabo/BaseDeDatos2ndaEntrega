from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from tkinter import *
from tkinter import messagebox as MessageBox

def modificarPais (): #Se modifica nombre

    ventanaPaisModificado = Tk()
    ventanaPaisModificado.geometry("300x200")
    ventanaPaisModificado.title("Modificar pais")

    labelCodigo = Label(ventanaPaisModificado, text="Escriba el codigo del pais a modificar" )
    labelCodigo.pack(padx=10,pady=8)

    codigoEntry = Entry(ventanaPaisModificado, width=200)
    codigoEntry.pack(pady=8,padx=10) 

    labelNombre = Label(ventanaPaisModificado, text="Escriba el nuevo nombre del pais")
    labelNombre.pack(pady=8,padx=10)

    nombreEntry = Entry(ventanaPaisModificado, width=200)
    nombreEntry.pack(pady=8,padx=10)

    sendInfo = Button(ventanaPaisModificado, text="Modificar pais",command=lambda: [modPais(), ventanaPaisModificado.destroy()])
    sendInfo.pack(pady=8,padx=10) 

    def modPais():

        codigo = codigoEntry.get()

        if codigo not in codigosPaisesValidos:
            MessageBox.showerror('Error','El codigo ingresado no existe')
        else:

            nombre = nombreEntry.get()

            for i in range(len(ListaDePaises)):

                if ListaDePaises[i][0] == codigo:
                    ListaDePaises[i][1] = nombre
                    MessageBox.showinfo('Base de datos','El pais ha sido modificado con exito')
                    break

def modificarCiudad(): #Se modifica nombre

    ventanaCiudadModificado = Tk()
    ventanaCiudadModificado.geometry("300x200")
    ventanaCiudadModificado.title("Modificar ciudad")

    labelCodigo = Label(ventanaCiudadModificado, text="Escriba el codigo de la ciudad a modificar")
    labelCodigo.pack(pady=8,padx=10)

    codigoEntry = Entry(ventanaCiudadModificado, width=200)
    codigoEntry.pack(pady=8,padx=10)

    labelNombre = Label(ventanaCiudadModificado, text="Escriba el nuevo nombre de la ciudad")
    labelNombre.pack(padx=10,pady=8)

    nombreEntry = Entry(ventanaCiudadModificado, width=200)
    nombreEntry.pack(pady=8,padx=10)

    sendInfo = Button(ventanaCiudadModificado, text="Modificar ciudad", command=lambda:[modCity(),ventanaCiudadModificado.destroy()])
    sendInfo.pack(pady=8,padx=10)

    def modCity():

        codigo = codigoEntry.get()

        if codigo not in codigosCiudadesValidos:
            MessageBox.showerror('Error','El codigo ingresado no existe')
        else:

            for i in range (len(ListaDeCiudades)):

                if ListaDeCiudades[i][1] == codigo:
                    
                    nombre = nombreEntry.get()
                    ListaDeCiudades[i][2] = nombre
                    MessageBox.showinfo('Base de datos','La ciudad ha sido modificada con exito')
                    break

def modificarCliente(): #Se modifica nombre, dirección, codpais, codciudad o Telefono

    ventanaClienteModificado = Tk()
    ventanaClienteModificado.geometry("300x500")
    ventanaClienteModificado.title("Modificar cliente")

    labelCodigoCliente = Label(ventanaClienteModificado,text="Escriba el codigo del cliente a modificar")
    labelCodigoCliente.pack(padx=10,pady=8)
    codigoClienteEntry = Entry(ventanaClienteModificado, width=200)
    codigoClienteEntry.pack(padx=10,pady=8)

    labelNombre = Label(ventanaClienteModificado, text="Indique el nombre a modificar del cliente")
    labelNombre.pack(padx=10,pady=8)
    nombreEntry = Entry(ventanaClienteModificado, width=200)
    nombreEntry.pack(pady=8,padx=10)

    labelDireccion = Label(ventanaClienteModificado,text="Indique la direccion a modificar")
    labelDireccion.pack(pady=8,padx=10)
    direccionEntry = Entry(ventanaClienteModificado,width=200)
    direccionEntry.pack(padx=10,pady=8)

    labelCodigoPais = Label(ventanaClienteModificado,text="Indique el nuevo codigo de pais")
    labelCodigoPais.pack(pady=8,padx=10)
    codigoPaisEntry = Entry(ventanaClienteModificado,width=200)
    codigoPaisEntry.pack(pady=8,padx=10)

    labelCodigoCiudad = Label(ventanaClienteModificado,text="Indique el nuevo codigo de ciudad")
    labelCodigoCiudad.pack(pady=8,padx=10)
    codigoCiudadEntry = Entry(ventanaClienteModificado,width=200)
    codigoCiudadEntry.pack(padx=10,pady=8)

    labelTelefono = Label(ventanaClienteModificado,text="Indique el nuevo numero de telefono")
    labelTelefono.pack(padx=10,pady=8)
    telefonoEntry = Entry(ventanaClienteModificado,width=200)
    telefonoEntry.pack(pady=8,padx=10)

    sendInfo = Button(ventanaClienteModificado,text="Modificar cliente",command=lambda:[modClient(),ventanaClienteModificado.destroy()])
    sendInfo.pack(padx=10,pady=8)

    def modClient():

        codigo = codigoClienteEntry.get()

        if codigo not in codigosClientesValidos:
            MessageBox.showerror('Error',"El codigo de cliente ingresado no existe")
        else:

            nombre = nombreEntry.get()
            direccion = direccionEntry.get()
            pais = codigoPaisEntry.get()
            ciudad = codigoCiudadEntry.get()
            telefono =  telefonoEntry.get()

            for i in range(len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:

                    ListaDeClientes[i][1] = nombre
                    ListaDeClientes[i][2] = direccion
                    ListaDeClientes[i][3] = pais
                    ListaDeClientes[i][4] = ciudad
                    ListaDeClientes[i][5] = telefono
                    MessageBox.showinfo('Base de datos','El cliente fue modificado con exito')
                    break

def modificarMascota():#Se modifica nombre y castrado

    ventana = Tk()
    ventana.title("Modificar mascota")
    ventana.geometry("300x350")

    labelCodigoCliente = Label(ventana, text="Indique el codigo del cliente")
    labelCodigoCliente.pack(pady=8,padx=10)
    codigoClienteEntry = Entry(ventana, width=200)
    codigoClienteEntry.pack(padx=10,pady=8)

    labelCodigoMascota = Label(ventana, text="Indique el codigo de la mascota")
    labelCodigoMascota.pack(pady=8,padx=10)
    codigoMascotaEntry= Entry(ventana, width=200)
    codigoMascotaEntry.pack(padx=10,pady=8)

    labelNombre = Label(ventana,text="Indique el nuevo nombre de la mascota")
    labelNombre.pack(pady=8,padx=10)
    nombreEntry = Entry(ventana,width=200)
    nombreEntry.pack(padx=10,pady=8)

    labelCastrado = Label(ventana,text="Indique si la mascota esta castrada")
    labelCastrado.pack(pady=8,padx=10)
    castradoEntry = Entry(ventana,width=200)
    castradoEntry.pack(pady=8,padx=10)

    sendInfo = Button(ventana,text="Modificar mascota",command=lambda:[modPet(),ventana.destroy()])
    sendInfo.pack(padx=10,pady=8)

    def modPet():

        cliente = codigoClienteEntry.get()
        
        if cliente not in codigosClientesValidos:
            MessageBox.showerror('Error',"El codigo de cliente ingresado no existe")
        else:
            mascota = codigoMascotaEntry.get()

            if mascota not in codigosMascotasValidos:
                MessageBox.showerror('Error',"El codigo de mascota ingresado no existe")
            else:

                nombre = nombreEntry.get()
                castrado = castradoEntry.get()

                for i in range(len(ListaDeMascotas)):

                    if ListaDeMascotas[i][1] == mascota:
                        
                        ListaDeMascotas[i][2] = nombre
                        ListaDeMascotas[i][10] = castrado
                        MessageBox.showinfo('Base de datos','La mascota ha sido modificada con exito')
                        break

def modificarVisita():

    ventana = Tk()
    ventana.geometry("300x300")
    ventana.title("Modificar visita")

    labelCodigoVisita = Label(ventana,text="Indique el codigo de visita")
    labelCodigoVisita.pack(pady=8,padx=10)
    codigoVisitaEntry = Entry(ventana,width=200)
    codigoVisitaEntry.pack(pady=8,padx=10)

    labelCodAnimal = Label(ventana, text="Indique el codigo de mascota")
    labelCodAnimal.pack(padx=10,pady=8)
    codAnimalEntry = Entry(ventana,width=200)
    codAnimalEntry.pack(pady=8,padx=10)

    labelPago = Label(ventana,text="Indique la nueva forma de pago")
    labelPago.pack(padx=10,pady=8)
    pagoEntry = Entry(ventana,width=200)
    pagoEntry.pack(padx=10,pady=8)

    sendInfo = Button(ventana,text="Modificar visita",command=lambda:[modVisit(),ventana.destroy()])
    sendInfo.pack(padx=10,pady=8)

    def modVisit():

        visita = codigoVisitaEntry.get()

        if visita not in codigosVisitasValidos:
            MessageBox.showerror('Error',"El codigo de visita no existe")
        else:

            mascota = codAnimalEntry.get()
            if mascota not in codigosMascotasValidos:
                MessageBox.showerror('Error','El codigo de mascota no existe')
            else:

                pago = pagoEntry.get()

                for i in range (len(ListaDeVisitas)):

                    if ListaDeVisitas[i][0] == visita:

                        ListaDeVisitas[i][6] = pago
                        MessageBox.showinfo('Base de datos',"La visita ha sido modificada con exito")
                        break

def modificarTratamiento():

    ventana = Tk()
    ventana.geometry("300x300")
    ventana.title("Modificar tratamiento")

    codLabel = Label(ventana,text="Indique el codigo del tratamiento")
    codLabel.pack(pady=8,padx=10)
    codEntry = Entry(ventana,width=200)
    codEntry.pack(pady=8,padx=10)

    precioLabel = Label(ventana,text="Indique el nuevo precio del tratamiento")
    precioLabel.pack(pady=8,padx=10)
    precioEntry = Entry(ventana,width=200)
    precioEntry.pack(padx=10,pady=8)

    sendInfo = Button(ventana,text="Modificar tratamiento", command=lambda:[modTreat(),ventana.destroy()])
    sendInfo.pack(padx=10,pady=8)

    def modTreat():

        codigo = codEntry.get()

        if codigo not in codigosTratamientosValidos:
            MessageBox.showerror('Error',"El codigo ingresado no existe")
        else:

            precio = int(precioEntry.get())

            for i in range(len(ListaDeTratamientos)):

                if ListaDeTratamientos[i][0] == codigo:

                    ListaDeTratamientos[i][2] = precio
                    MessageBox.showinfo('Base de datos',"El tratamiento ha sido modificado con exito")
                    break

def modificarMedicacion():

    ventana = Tk()
    ventana.geometry("300x500")
    ventana.title("Modificar medicacion")

    codMedLabel = Label(ventana,text="Indique el codigo de medicacion")
    codMedLabel.pack(padx=10,pady=8)
    codMedEntry = Entry(ventana, width=200)
    codMedEntry.pack(pady=8,padx=10)

    codMascLabel = Label(ventana,text="Indique el codigo de la mascota")
    codMascLabel.pack(padx=10,pady=8)
    codMascEntry = Entry(ventana,width=200)
    codMascEntry.pack(padx=10,pady=8)

    cantLabel = Label(ventana,text="Ingrese la nueva cantidad")
    cantLabel.pack(padx=10,pady=8)
    cantEntry = Entry(ventana,width=200)
    cantEntry.pack(padx=10,pady=8)

    precioLabel = Label(ventana, text="Ingrese el nuevo precio")
    precioLabel.pack(padx=10,pady=8)
    precioEntry = Entry(ventana,width=200)
    precioEntry.pack(padx=10,pady=8)

    costoLabel = Label(ventana, text="Ingrese el nuevo costo total")
    costoLabel.pack(padx=10,pady=8)
    costoEntry = Entry(ventana,width=200)
    costoEntry.pack(padx=10,pady=8)

    sendInfo = Button(ventana,text="Modificar medicacion",command=lambda:[modMed(),ventana.destroy()])
    sendInfo.pack(padx=10,pady=8)

    def modMed():

        medicacion = codMedEntry.get()

        if medicacion not in codigosMedicacionValidos:
            MessageBox.showerror('Error',"El codigo de medicacion ingresado no existe")
        else:

            mascota = codMascEntry.get()

            if mascota not in codigosMascotasValidos:
                MessageBox.showerror('Error',"El codigo de mascota ingresado no existe")
            else:

                cantidad = int(cantEntry.get())
                precio = int(precioEntry.get())
                costoTotal = int(costoEntry.get())

                for i in range(len(ListaDeMedicacion)):

                    if ListaDeMedicacion[i][1] == medicacion:
                        costoValidado = cantidad*precio

                        if costoValidado == costoTotal:
                            ListaDeMedicacion[i][6] = precio
                            ListaDeMedicacion[i][7] = cantidad
                            ListaDeMedicacion[i][8] = costoTotal
                            MessageBox.showinfo('Base de datos',"La medicacion se ha modificado con exito")
                            break
                        else:
                            MessageBox.showerror('Error',"El costo total no coincide con la cantidad")
                            break
                    
                        





