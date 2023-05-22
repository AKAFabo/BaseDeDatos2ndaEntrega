from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from tkinter import *
from tkinter import messagebox as MessageBox

#Ventana de añadir pais

def añadirPais():
        
        ventanaPaisNuevo = Tk()
        ventanaPaisNuevo.title("Agregar pais")
        ventanaPaisNuevo.geometry("300x500")

        codigoLabel = Label(ventanaPaisNuevo, text="Indique el codigo de pais a agregar")
        codigoLabel.pack(padx=10,pady=8)
        añadirCodigoEntry = Entry(ventanaPaisNuevo, width=200)
        añadirCodigoEntry.pack(pady=12, padx=10)

        nombreLabel = Label(ventanaPaisNuevo, text="Indique el nombre del pais a agregar")
        nombreLabel.pack(padx=10,pady=8)
        añadirNombreEntry = Entry(ventanaPaisNuevo,  width=200)
        añadirNombreEntry.pack(pady=8, padx=10)

        añadirInformacionButton = Button(ventanaPaisNuevo,text="Añadir informacion",command=lambda:[sendCountryInfo(),ventanaPaisNuevo.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendCountryInfo():
             
            codigo = añadirCodigoEntry.get()
            pais = añadirNombreEntry.get()

            if codigo in codigosPaisesValidos:
                MessageBox.showerror("Error", "El codigo ingresado ya existe")
            else:
                nuevoPais = [codigo, pais]
                ListaDePaises.append(nuevoPais)
                codigosPaisesValidos.append(codigo)
                MessageBox.showinfo("Base de datos", "Se agrego el pais correctamente")
                 
        ventanaPaisNuevo.mainloop()

#Ventana de agregar ciudad

def añadirCiudad():

        ventanaCiudadNueva = Tk()
        ventanaCiudadNueva.title("Agregar ciudad")
        ventanaCiudadNueva.geometry("300x500")

        codigoPais = Label(ventanaCiudadNueva,text="Indique el codigo de pais")
        codigoPais.pack(padx=10,pady=8)
        añadirCodigoPaisEntry = Entry(ventanaCiudadNueva, width=200)
        añadirCodigoPaisEntry.pack(pady=12, padx=10)

        codigoCiudad = Label(ventanaCiudadNueva, text="Indique el codigo de ciudad a agregar")
        codigoCiudad.pack(padx=10,pady=8)
        añadirCodigoCiudadEntry = Entry(ventanaCiudadNueva, width=200)
        añadirCodigoCiudadEntry.pack(pady=8, padx=10)

        nombreLabel = Label(ventanaCiudadNueva, text="Indique el nombre la ciudad a agregar")
        nombreLabel.pack(padx=10,pady=8)
        añadirNombreEntry = Entry(ventanaCiudadNueva, width=200)
        añadirNombreEntry.pack(pady=8, padx=10)

        añadirInformacionButton = Button(ventanaCiudadNueva, text="Añadir información",command=lambda:[sendCityInfo(),ventanaCiudadNueva.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendCityInfo():

            codigoPais = añadirCodigoPaisEntry.get()
            codigoCiudad = añadirCodigoCiudadEntry.get()
            nombreCiudad = añadirNombreEntry.get()

            if codigoPais not in codigosPaisesValidos:
                MessageBox.showerror("Error", "El codigo de pais ingresado no existe")

            else:
                if codigoCiudad in codigosCiudadesValidos:
                    MessageBox.showerror("Error", "El codigo de ciudad ya existe")
                else:
                    nuevaCiudad = [codigoPais, codigoCiudad, nombreCiudad]
                    ListaDeCiudades.append(nuevaCiudad)
                    codigosCiudadesValidos.append(codigoCiudad)
                    MessageBox.showinfo("Base de datos", "La ciudad ha sido ingresada con exito")

        ventanaCiudadNueva.mainloop()

#Ventana de agregar cliente

def añadirCliente():

        ventanaClienteNuevo = Tk()
        ventanaClienteNuevo.title("Agregar cliente")
        ventanaClienteNuevo.geometry("300x800")

        codeClienteLabel = Label(ventanaClienteNuevo,text="Indique el codigo de cliente a agregar")
        codeClienteLabel.pack(padx=10,pady=8)
        codeClienteEntry = Entry(ventanaClienteNuevo,width=200)
        codeClienteEntry.pack(pady=8,padx=10)

        nombreLabel = Label(ventanaClienteNuevo,text="Indique el nombre del cliente a agregar")
        nombreLabel.pack(padx=10,pady=8)
        nombreClienteEntry = Entry(ventanaClienteNuevo,width=200)    
        nombreClienteEntry.pack(pady=8,padx=10)

        direccionLabel = Label(ventanaClienteNuevo, text="Indique la direccion del cliente a agregar")
        direccionLabel.pack(padx=10,pady=8)
        direccionClienteEntry = Entry(ventanaClienteNuevo,width=200)
        direccionClienteEntry.pack(pady=8,padx=10)

        codePaisLabel = Label(ventanaClienteNuevo,text="Indique el codigo de pais del cliente")
        codePaisLabel.pack(padx=10,pady=8)
        codigoPaisEntry = Entry(ventanaClienteNuevo,width=200)
        codigoPaisEntry.pack(pady=8,padx=10)

        codeCiudadLabel = Label(ventanaClienteNuevo,text="Indique el codigo de ciudad del cliente")
        codeCiudadLabel.pack(padx=10,pady=8)
        codigoCiudadEntry = Entry(ventanaClienteNuevo,width=200)
        codigoCiudadEntry.pack(pady=8,padx=10)

        telLable = Label(ventanaClienteNuevo, text="Indique el telefono del cliente a agregar")
        telLable.pack(padx=10,pady=8)
        telClienteEntry = Entry(ventanaClienteNuevo,width=200)
        telClienteEntry.pack(pady=8,padx=10)

        ultDia = Label(ventanaClienteNuevo,text="Indique el ultimo dia de visita del cliente")
        ultDia.pack(padx=10,pady=8)
        ultDiaVisita = Entry(ventanaClienteNuevo, width=200)
        ultDiaVisita.pack(pady=8,padx=10)

        ultMes = Label(ventanaClienteNuevo,text="Indique el ultimo mes de visita del cliente")
        ultMes.pack(padx=10,pady=8)
        ultMesVisita = Entry(ventanaClienteNuevo, width=200)
        ultMesVisita.pack(pady=8,padx=10)

        ultYear = Label(ventanaClienteNuevo,text="Indique el ultimo año de visita del cliente")
        ultYear.pack(padx=10,pady=8)
        ultAñoVisita = Entry(ventanaClienteNuevo,width=200)
        ultAñoVisita.pack(pady=8,padx=10)

        saldoLabel = Label(ventanaClienteNuevo,text="Indique el saldo del cliente a agregar")
        saldoLabel.pack(padx=10,pady=8)
        saldoClienteEntry =  Entry(ventanaClienteNuevo, width=200)  
        saldoClienteEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaClienteNuevo, text="Añadir informacion",command=lambda:[sendClientInfo(),ventanaClienteNuevo.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendClientInfo():

            codigoCliente = codeClienteEntry.get()
            nombreCliente = nombreClienteEntry.get()
            direccion = direccionClienteEntry.get()
            codigoPais = codigoPaisEntry.get()
            codigoCiudad = codigoCiudadEntry.get()
            telefono = telClienteEntry.get()
            diaVisita = ultDiaVisita.get()
            mesVisita = ultMesVisita.get()
            añoVisita = ultAñoVisita.get()
            saldo = int(saldoClienteEntry.get())
            descuento = 0

            if 1 <= saldo <=99999:
                descuento = 3
            elif saldo == 100000:
                descuento = 5
            elif 101000 <= saldo <= 150000:
                descuento = 10
            else:
                descuento = 0

            if codigoCliente in codigosClientesValidos:
                MessageBox.showerror("Error", "El codigo de cliente ya existe")
            else:
                if codigoPais not in codigosPaisesValidos:
                    MessageBox.showerror("Error","El codigo de pais es invalido")
                else:
                    if codigoCiudad not in codigosCiudadesValidos:
                        MessageBox.showerror("Error","El codigo de ciudad es invalido")
                    else:
                        nuevoCliente = [codigoCliente,nombreCliente,direccion,codigoPais,codigoCiudad,telefono,diaVisita,mesVisita,añoVisita,saldo,descuento]
                        ListaDeClientes.append(nuevoCliente)
                        codigosClientesValidos.append(codigoCliente)
                        MessageBox.showinfo("Base de datos","El cliente ha sido agregado con exito")

        ventanaClienteNuevo.mainloop()

#Ventana de agregar mascota

def añadirMascota():

        ventanaMascotaNueva = Tk()
        ventanaMascotaNueva.title("Agregar mascota")
        ventanaMascotaNueva.geometry("300x750")

        codeCliente = Label(ventanaMascotaNueva, text="Indique el codigo del cliente")
        codeCliente.pack(padx=10)
        codeClienteEntry = Entry(ventanaMascotaNueva,width=200)
        codeClienteEntry.pack(pady=8)

        codeAnimalLabel = Label(ventanaMascotaNueva,text="Indique el codigo de la mascota a agregar")
        codeAnimalLabel.pack(padx=10)
        codeAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        codeAnimalEntry.pack(pady=8)

        nombreLabel = Label(ventanaMascotaNueva, text="Indique el nombre de la mascota a agregar")
        nombreLabel.pack(padx=10)
        nombreAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        nombreAnimalEntry.pack(pady=8)

        tipoLabel = Label(ventanaMascotaNueva, text="Indique el tipo de la mascota a agregar")
        tipoLabel.pack(padx=10)
        tipoAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        tipoAnimalEntry.pack(pady=8)

        razaLabel = Label(ventanaMascotaNueva,text="Indique la raza de la mascota a agregar")
        razaLabel.pack(padx=10)
        razaAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        razaAnimalEntry.pack(pady=8)

        diaLabel = Label(ventanaMascotaNueva,text="Indique el dia de nacimiento")
        diaLabel.pack(padx=10)
        diaNacimiento = Entry(ventanaMascotaNueva, width=200)
        diaNacimiento.pack(pady=8)

        mesLabel = Label(ventanaMascotaNueva,text="Indique el mes de nacimiento de la mascota")
        mesLabel.pack(padx=10)
        mesNacimiento = Entry(ventanaMascotaNueva,width=200)
        mesNacimiento.pack(pady=8)

        yearLabel = Label(ventanaMascotaNueva,text="Indique el año de nacimiento de la mascota")
        yearLabel.pack(padx=10)
        añoNacimiento = Entry(ventanaMascotaNueva, width=200)
        añoNacimiento.pack(pady=8)

        sexoLabel = Label(ventanaMascotaNueva,text="Indique el sexo de la mascota a agregar")
        sexoLabel.pack(padx=10)
        sexoAnimalEntry = Entry(ventanaMascotaNueva,width=200)
        sexoAnimalEntry.pack(pady=8)

        colorLabel = Label(ventanaMascotaNueva,text="Indique el color de la mascota a agregar")
        colorLabel.pack(padx=10)
        colorMascotaEntry = Entry(ventanaMascotaNueva, width=200)   
        colorMascotaEntry.pack(pady=8)

        castradoLabel = Label(ventanaMascotaNueva,text="Indique si la mascota esta castrada o no")
        castradoLabel.pack(padx=10)
        castradoMascotaEntry = Entry(ventanaMascotaNueva,width=200)
        castradoMascotaEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaMascotaNueva, text="Añadir informacion",command=lambda:[sendPetInfo(),ventanaMascotaNueva.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendPetInfo():

            cliente = codeClienteEntry.get()
            codeMascota = codeAnimalEntry.get()
            nombre = nombreAnimalEntry.get()
            tipo = tipoAnimalEntry.get()
            raza = razaAnimalEntry.get()
            dia = diaNacimiento.get()
            mes = mesNacimiento.get()
            año = añoNacimiento.get()
            sexo = sexoAnimalEntry.get()
            color = colorMascotaEntry.get()
            castrado = castradoMascotaEntry.get()

            if cliente not in codigosClientesValidos:
                MessageBox.showerror("Error", "El codigo de cliente es invalido")
            else:
                if codeMascota in codigosMascotasValidos:
                    MessageBox.showerror("Error","El codigo de mascota ya existe")
                else:
                    nuevaMascota = [cliente,codeMascota,nombre,tipo,raza,dia,mes,año,sexo,color,castrado]
                    ListaDeMascotas.append(nuevaMascota)
                    codigosMascotasValidos.append(codeMascota)
                    MessageBox.showinfo("Base de datos","La mascota ha sido agregada con exito")

        ventanaMascotaNueva.mainloop()

#Ventana de agregar visitas

def añadirVisitas():

        ventanaVisitaNueva = Tk()
        ventanaVisitaNueva.title("Agregar visita")
        ventanaVisitaNueva.geometry("300x600")

        visitaLabel = Label(ventanaVisitaNueva,text="Indique el codigo de visita a agregar")
        visitaLabel.pack(padx=10,pady=8)
        codVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        codVisitaEntry.pack(pady=8)

        animalLabel = Label(ventanaVisitaNueva,text="Indique el codigo de la mascota")
        animalLabel.pack(padx=10,pady=8)
        codAnimalEntry = Entry(ventanaVisitaNueva,width=200)
        codAnimalEntry.pack(pady=8)

        diaLabel = Label(ventanaVisitaNueva,text="Indique el ultimo dia de visita")
        diaLabel.pack(padx=10,pady=8)
        ultDiaVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultDiaVisitaEntry.pack(pady=8)

        mesLabel = Label(ventanaVisitaNueva,text="Indique el ultimo mes de visita")
        mesLabel.pack(padx=10,pady=8)
        ultMesVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultMesVisitaEntry.pack(pady=8)

        ultAño = Label(ventanaVisitaNueva,text="Indique el ultimo año de visita")
        ultAño.pack(padx=10,pady=8)
        ultAñoVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultAñoVisitaEntry.pack(pady=8)

        totalEntry = Label(ventanaVisitaNueva,text="Indique el total de la factura")
        totalEntry.pack(padx=10,pady=8)
        totalFacturaEntry =Entry(ventanaVisitaNueva,width=200)
        totalFacturaEntry.pack(pady=8)

        pagoLabel = Label(ventanaVisitaNueva,text="Indique la forma de pago")
        pagoLabel.pack(padx=10,pady=8)
        formaPagoEntry = Entry(ventanaVisitaNueva,width=200)
        formaPagoEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaVisitaNueva, text='Añadir informacion',command=lambda:[sendVisitInfo(),ventanaVisitaNueva.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendVisitInfo():

            codVisita = codVisitaEntry.get()
            codAnimal = codAnimalEntry.get()
            ultDia = ultDiaVisitaEntry.get()
            ultMes = ultMesVisitaEntry.get()
            ultAño = ultAñoVisitaEntry.get()
            totalFactura = totalFacturaEntry.get()
            formaPago = formaPagoEntry.get()

            if codVisita in codigosVisitasValidos:
                MessageBox.showerror('Error',"El codigo de visita ya existe")
            else:
                if codAnimal not in codigosMascotasValidos:
                    MessageBox.showerror('Error',"El codigo de mascota no existe")
                else:
                    nuevaVisita = [codVisita,codAnimal,ultDia,ultMes,ultAño,totalFactura,formaPago]
                    ListaDeVisitas.append(nuevaVisita)
                    codigosVisitasValidos.append(codVisita)
                    MessageBox.showinfo('Base de datos',"La visita ha sido agregada con exito")
        
        ventanaVisitaNueva.mainloop()

#Ventana de agregar tratamientos


def añadirTratamientos():

    ventanaTratamientoNuevo = Tk()
    ventanaTratamientoNuevo.title("Agregar tratamiento")
    ventanaTratamientoNuevo.geometry("300x500")

    codLabel = Label(ventanaTratamientoNuevo,text="Indique el codigo de tratamiento a agregar")
    codLabel.pack(padx=10,pady=8)
    codTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    codTratamientoEntry.pack(pady=8)

    nombreLabel = Label(ventanaTratamientoNuevo,text="Indique el nombre del tratamiento")
    nombreLabel.pack(padx=10,pady=8)
    nombreTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    nombreTratamientoEntry.pack(pady=8)

    precioLabel = Label(ventanaTratamientoNuevo,text="Indique el precio del tratamiento")
    precioLabel.pack(padx=10,pady=8)
    precioTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    precioTratamientoEntry.pack(pady=8)

    cantidadLabel = Label(ventanaTratamientoNuevo,text="Inddique la cantidad de tratamiento disponible")
    cantidadLabel.pack(padx=10,pady=8)
    cantidadTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    cantidadTratamientoEntry.pack(pady=8)

    añadirInformacionButton = Button(ventanaTratamientoNuevo, text='Añadir informacion',command=lambda:[sendTreatInfo(),ventanaTratamientoNuevo.destroy()])
    añadirInformacionButton.pack(pady=8)

    def sendTreatInfo():

        codTratamiento = codTratamientoEntry.get()
        nombreTratamiento = nombreTratamientoEntry.get()
        precioTratamiento = precioTratamientoEntry.get()
        cantidad = cantidadTratamientoEntry.get()

        if codTratamiento in codigosTratamientosValidos:
            MessageBox.showerror("Error","El codigo de tratamiento ya existe")
        else:
            nuevoTratamiento = [codTratamiento, nombreTratamiento, precioTratamiento, cantidad]
            ListaDeTratamientos.append(nuevoTratamiento)
            codigosTratamientosValidos.append(codTratamiento)
            MessageBox.showinfo('Base de datos',"El tratamiento ha sido agregado con exito")

    ventanaTratamientoNuevo.mainloop()

#Ventana de agregar medicacion

def añadirMedicacion():

        ventanaMedicacionNueva = Tk()
        ventanaMedicacionNueva.title("Agregar mediacion")
        ventanaMedicacionNueva.geometry("300x700")

        codAnimal = Label(ventanaMedicacionNueva,text="Indique el codigo de la mascota")
        codAnimal.pack(padx=10,pady=8)
        codAnimalEntry = Entry(ventanaMedicacionNueva,width=200)
        codAnimalEntry.pack(pady=8)

        codMedicacion = Label(ventanaMedicacionNueva,text="Indique el codigo de medicacion a agregar")
        codMedicacion.pack(padx=10,pady=8)
        codMedicacionEntry = Entry(ventanaMedicacionNueva,width=200)
        codMedicacionEntry.pack(pady=8)

        ultDia = Label(ventanaMedicacionNueva,text="Ingrese el ultimo dia de visita")
        ultDia.pack(padx=10,pady=8)
        ultDiaVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultDiaVisitaEntry.pack(pady=8)

        ultMes = Label(ventanaMedicacionNueva,text="Indique el ultimo mes de visita")
        ultMes.pack(padx=10,pady=8)
        ultMesVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultMesVisitaEntry.pack(pady=8)

        ultYear = Label(ventanaMedicacionNueva,text="Indique el ultimo año de visita")
        ultYear.pack(padx=10,pady=8)
        ultAñoVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultAñoVisitaEntry.pack(pady=8)

        medicamentosLabel = Label(ventanaMedicacionNueva, text="Idique los medicamentos a agregar")
        medicamentosLabel.pack(padx=10,pady=8)
        medicamentosEntry = Entry(ventanaMedicacionNueva,width=200)
        medicamentosEntry.pack(pady=8)

        costoUnitarioLabel = Label(ventanaMedicacionNueva,text="Indique el costo unitario del tratamiento")
        costoUnitarioLabel.pack(padx=10,pady=8)
        costoUnitarioEntry = Entry(ventanaMedicacionNueva,width=200)
        costoUnitarioEntry.pack(pady=8)

        cantidadLabel = Label(ventanaMedicacionNueva,text="Indique la cantidad de tratamiento utilizada")
        cantidadLabel.pack(padx=10,pady=8)
        cantidadEntry = Entry(ventanaMedicacionNueva,width=200)
        cantidadEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaMedicacionNueva, text="Añadir informacion",command=lambda:[sendMedInfo(), ventanaMedicacionNueva.destroy()])
        añadirInformacionButton.pack(pady=8)

        def sendMedInfo():

            codAnimal = codAnimalEntry.get()
            codMedicacion = codMedicacionEntry.get()
            dia = ultDiaVisitaEntry.get()
            mes = ultMesVisitaEntry.get()
            año = ultAñoVisitaEntry.get()
            medicamentos = medicamentosEntry.get()
            costoUnitario = int(costoUnitarioEntry.get())
            cantidad = int(cantidadEntry.get())
            costoTotal = costoUnitario * cantidad

            if codAnimal not in codigosMascotasValidos:
                MessageBox.showerror('Error',"El codigo de mascota no existe")
            else:
                if codMedicacion in codigosMedicacionValidos:
                    MessageBox.showerror('Error',"El codigo de medicacion ya existe")
                else:
                    nuevaMedicacion = [codAnimal,codMedicacion,dia,mes,año,medicamentos,costoUnitario,cantidad,costoTotal]
                    ListaDeMedicacion.append(nuevaMedicacion)
                    codigosMedicacionValidos.append(codMedicacion)
                    MessageBox.showinfo('Base de datos',"La medicacion ha sido agregada con exito")

        ventanaMedicacionNueva.mainloop()