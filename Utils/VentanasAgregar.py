#Importar validaciones
from Validaciones.validacionPaises import validacionPais
from Validaciones.validacionCiudades import validacionCiudades
from Validaciones.validacionCliente import validacionCliente
from Validaciones.validacionMascotas import validacionMascota
from Validaciones.validacionVisitas import validarVisitas
from Validaciones.validacionTratamientos import validarTratamientos
from Validaciones.validacionMedicacion import validarMedicacion

#Importar listas con codigos
from listasConCodigos import codePaises
from listasConCodigos import nombrePaises
from listasConCodigos import codeCiudades
from listasConCodigos import codeClientes
from listasConCodigos import codeMascotas
from listasConCodigos import codeVisitas
from listasConCodigos import codeTratamiento
from listasConCodigos import codeMedicacion

#LISTAS EN MEMORIA

ListaDePaises = validacionPais()
ListaDeCiudades = validacionCiudades()
ListaDeClientes = validacionCliente()
ListaDeMascotas = validacionMascota()
ListaDeVisitas = validarVisitas()
ListaDeTratamientos = validarTratamientos()
ListaDeMedicacion = validarMedicacion()

codigosPaisesValidos = codePaises()
nombresPaisesValidos = nombrePaises()
codigosClientesValidos = codeClientes()  
codigosCiudadesValidos = codeCiudades()
codigosMascotasValidos = codeMascotas()
codigosVisitasValidos = codeVisitas()
codigosTratamientosValidos = codeTratamiento()
codigosMedicacionValidos = codeMedicacion()

from tkinter import *
from tkinter import messagebox as MessageBox

#Ventana de añadir pais

def añadirPais():
         
        ventanaPaisNuevo = Tk()
        ventanaPaisNuevo.title("Agregar pais")
        ventanaPaisNuevo.geometry("300x300")

        añadirCodigoEntry = Entry(ventanaPaisNuevo, width=200)
        añadirCodigoEntry.insert(0, 'Ingresar codigo del pais')
        añadirCodigoEntry.pack(pady=12, padx=10)
        añadirNombreEntry = Entry(ventanaPaisNuevo,  width=200)
        añadirNombreEntry.insert(0,'Ingresar nombre del pais')
        añadirNombreEntry.pack(pady=8, padx=10)

        añadirInformacionButton = Button(ventanaPaisNuevo,text="Añadir informacion",command=lambda:sendCountryInfo())
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
        ventanaCiudadNueva.geometry("300x300")

        añadirCodigoPaisEntry = Entry(ventanaCiudadNueva, width=200)
        añadirCodigoPaisEntry.insert(0,'Ingrese el codigo del pais')
        añadirCodigoPaisEntry.pack(pady=12, padx=10)
        añadirCodigoCiudadEntry = Entry(ventanaCiudadNueva, width=200)
        añadirCodigoCiudadEntry.insert(0,'Ingrese el codigo de ciudad')
        añadirCodigoCiudadEntry.pack(pady=8, padx=10)
        añadirNombreEntry = Entry(ventanaCiudadNueva, width=200)
        añadirNombreEntry.insert(0,'Ingrese el nombre de la ciudad')
        añadirNombreEntry.pack(pady=8, padx=10)
        añadirInformacionButton = Button(ventanaCiudadNueva, text="Añadir información",command=lambda:sendCityInfo())
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
        ventanaClienteNuevo.geometry("300x500")

        codeClienteEntry = Entry(ventanaClienteNuevo,width=200)
        codeClienteEntry.insert(0,'Inserte el codigo del cliente')
        codeClienteEntry.pack(pady=8,padx=10)
        nombreClienteEntry = Entry(ventanaClienteNuevo,width=200)    
        nombreClienteEntry.insert(0,'Ingrese el nombre del cliente')
        nombreClienteEntry.pack(pady=8,padx=10)
        direccionClienteEntry = Entry(ventanaClienteNuevo,width=200)
        direccionClienteEntry.insert(0,'Ingrese la direccion del cliente')
        direccionClienteEntry.pack(pady=8,padx=10)
        codigoPaisEntry = Entry(ventanaClienteNuevo,width=200)
        codigoPaisEntry.insert(0,'Ingrese el codigo de pais')
        codigoPaisEntry.pack(pady=8,padx=10)
        codigoCiudadEntry = Entry(ventanaClienteNuevo,width=200)
        codigoCiudadEntry.insert(0,'Ingrese el codigo de ciudad')
        codigoCiudadEntry.pack(pady=8,padx=10)
        telClienteEntry = Entry(ventanaClienteNuevo,width=200)
        telClienteEntry.insert(0,'Ingrese el telefono del ciente')
        telClienteEntry.pack(pady=8,padx=10)
        ultDiaVisita = Entry(ventanaClienteNuevo, width=200)
        ultDiaVisita.insert(0,'Ingrese el ultimo dia de visita')
        ultDiaVisita.pack(pady=8,padx=10)
        ultMesVisita = Entry(ventanaClienteNuevo, width=200)
        ultMesVisita.insert(0,'Ingrese el ultimo mes de visita')
        ultMesVisita.pack(pady=8,padx=10)
        ultAñoVisita = Entry(ventanaClienteNuevo,width=200)
        ultAñoVisita.insert(0,'Ingrese el ultimo año de visita')
        ultAñoVisita.pack(pady=8,padx=10)
        saldoClienteEntry =  Entry(ventanaClienteNuevo, width=200)  
        saldoClienteEntry.insert(0,'Ingrese el saldo del cliente')
        saldoClienteEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaClienteNuevo, text="Añadir informacion",command=lambda:sendClientInfo())
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
        ventanaMascotaNueva.geometry("300x500")

        codeClienteEntry = Entry(ventanaMascotaNueva,width=200)
        codeClienteEntry.insert(0,'Ingrese el codigo del cliente')
        codeClienteEntry.pack(pady=8)
        codeAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        codeAnimalEntry.insert(0,'Ingrese el codigo de la mascota')
        codeAnimalEntry.pack(pady=8)
        nombreAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        nombreAnimalEntry.insert(0,'Ingrese el nombre de la mascota')
        nombreAnimalEntry.pack(pady=8)
        tipoAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        tipoAnimalEntry.insert(0,'Ingrese el tipo de mascota')
        tipoAnimalEntry.pack(pady=8)
        razaAnimalEntry = Entry(ventanaMascotaNueva, width=200)
        razaAnimalEntry.insert(0,'Ingrese la raza de la mascota')
        razaAnimalEntry.pack(pady=8)
        diaNacimiento = Entry(ventanaMascotaNueva, width=200)
        diaNacimiento.insert(0,'Ingrese el dia de nacimiento')
        diaNacimiento.pack(pady=8)
        mesNacimiento = Entry(ventanaMascotaNueva,width=200)
        mesNacimiento.insert(0,'Ingrese el mes de nacimiento')
        mesNacimiento.pack(pady=8)
        añoNacimiento = Entry(ventanaMascotaNueva, width=200)
        añoNacimiento.insert(0,'Ingrese el año de nacimiento')
        añoNacimiento.pack(pady=8)
        sexoAnimalEntry = Entry(ventanaMascotaNueva,width=200)
        sexoAnimalEntry.insert(0,'Ingrese el sexo del animal')
        sexoAnimalEntry.pack(pady=8)
        colorMascotaEntry = Entry(ventanaMascotaNueva, width=200)   
        colorMascotaEntry.insert(0,'Ingrese el color de la mascota')
        colorMascotaEntry.pack(pady=8)
        castradoMascotaEntry = Entry(ventanaMascotaNueva,width=200)
        castradoMascotaEntry.insert(0,'Indique si la mascota esta castrada o no')
        castradoMascotaEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaMascotaNueva, text="Añadir informacion",command=lambda:sendPetInfo())
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
        ventanaVisitaNueva.geometry("300x400")

        codVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        codVisitaEntry.insert(0,'Ingrese el codigo de la visita')
        codVisitaEntry.pack(pady=8)
        codAnimalEntry = Entry(ventanaVisitaNueva,width=200)
        codAnimalEntry.insert(0,'Ingrese el codigo de  la mascota')
        codAnimalEntry.pack(pady=8)
        ultDiaVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultDiaVisitaEntry.insert(0,'Ingrese el ultimo dia de visita')
        ultDiaVisitaEntry.pack(pady=8)
        ultMesVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultMesVisitaEntry.insert(0,'Ingrese el ultimo mes de visita')
        ultMesVisitaEntry.pack(pady=8)
        ultAñoVisitaEntry = Entry(ventanaVisitaNueva,width=200)
        ultAñoVisitaEntry.insert(0,'Ingrese el ultimo año de visita')
        ultAñoVisitaEntry.pack(pady=8)
        totalFacturaEntry =Entry(ventanaVisitaNueva,width=200)
        totalFacturaEntry.insert(0,'Ingrese el total de la factura')
        totalFacturaEntry.pack(pady=8)
        formaPagoEntry = Entry(ventanaVisitaNueva,width=200)
        formaPagoEntry.insert(0,'Ingrese la forma de pago')
        formaPagoEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaVisitaNueva, text='Añadir informacion',command=lambda:sendVisitInfo())
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
                    ListaDeVisitas.APPEND(nuevaVisita)
                    codigosVisitasValidos.append(codVisita)
                    MessageBox.showinfo('Base de datos',"La visita ha sido agregada con exito")
        
        ventanaVisitaNueva.mainloop()

#Ventana de agregar tratamientos


def añadirTratamientos():

    ventanaTratamientoNuevo = Tk()
    ventanaTratamientoNuevo.title("Agregar tratamiento")
    ventanaTratamientoNuevo.geometry("300x300")

    codTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    codTratamientoEntry.insert(0,'Ingrese el codigo del tratamiento')
    codTratamientoEntry.pack(pady=8)
    nombreTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    nombreTratamientoEntry.insert(0,'Ingrese el nombre del tratamiento')
    nombreTratamientoEntry.pack(pady=8)
    precioTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    precioTratamientoEntry.insert(0,'Ingrese el precio del tratamiento')
    precioTratamientoEntry.pack(pady=8)
    cantidadTratamientoEntry = Entry(ventanaTratamientoNuevo,width=200)
    cantidadTratamientoEntry.insert(0,'Ingrese la cantidad disponible')
    cantidadTratamientoEntry.pack(pady=8)

    añadirInformacionButton = Button(ventanaTratamientoNuevo, text='Añadir informacion',command=lambda:sendTreatInfo())
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
        ventanaMedicacionNueva.geometry("300x500")

        codAnimalEntry = Entry(ventanaMedicacionNueva,width=200)
        codAnimalEntry.insert(0,"Ingrese el codigo de la mascota")
        codAnimalEntry.pack(pady=8)
        codMedicacionEntry = Entry(ventanaMedicacionNueva,width=200)
        codMedicacionEntry.insert(0,'Ingrese el codigo de medicacion')
        codMedicacionEntry.pack(pady=8)
        ultDiaVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultDiaVisitaEntry.insert(0,'Ingrese el ultimo dia de visita')
        ultDiaVisitaEntry.pack(pady=8)
        ultMesVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultMesVisitaEntry.insert(0, 'Ingrese el ultimo mes de visita')
        ultMesVisitaEntry.pack(pady=8)
        ultAñoVisitaEntry = Entry(ventanaMedicacionNueva,width=200)
        ultAñoVisitaEntry.insert(0,"Ingrese el ultimo año de visita")
        medicamentosEntry = Entry(ventanaMedicacionNueva,width=200)
        medicamentosEntry.insert(0,'Ingrese el medicamento')
        medicamentosEntry.pack(pady=8)
        costoUnitarioEntry = Entry(ventanaMedicacionNueva,width=200)
        costoUnitarioEntry.insert(0,'Ingrese el costo unitario del medicamento')
        costoUnitarioEntry.pack(pady=8)
        cantidadEntry = Entry(ventanaMedicacionNueva,width=200)
        cantidadEntry.insert(0,'Ingrese la cantidad de medicamento')
        cantidadEntry.pack(pady=8)

        añadirInformacionButton = Button(ventanaMedicacionNueva, text="Añadir informacion",command=lambda:sendMedInfo())
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