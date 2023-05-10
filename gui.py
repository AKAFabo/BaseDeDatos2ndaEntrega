#Importar libreria de GUI
from tkinter import messagebox as MessageBox
from tkinter import *


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

root = Tk()
root.geometry("1366x768")
root.title("Base de datos")

mantenimientoButtonFrame = Frame(root)
mantenimientoButtonFrame.place(x=0,y=0)
mantenimientoButton = Button(mantenimientoButtonFrame, text="Mantenimiento", command=lambda: openMantenimientoMenu())
mantenimientoButton.pack()

reportesButtonFrame = Frame(root)
reportesButtonFrame.place(x=350,y=0)
reportesButton = Button(reportesButtonFrame, text="Reportes", command=lambda: openReportesMenu())
reportesButton.pack()

facturacionButtonFrame = Frame(root)
facturacionButtonFrame.place(x=700,y=0)
facturacionButton = Button(facturacionButtonFrame, text="Facturacion", command=lambda: openFacturacionMenu())
facturacionButton.pack()

acercaDeFrame = Frame(root)
acercaDeFrame.place(x=1000,y=0)
acercaDeButton = Button(acercaDeFrame, text="Acerca de", command=lambda: openAcercaDeMenu())
acercaDeButton.pack()

agregarContactoFrame = Frame(root)
agregarContactoFrame.place(x=1000,y=250)

labelContacto = Label(root, text="Agregar informacion de contacto")
labelContacto.place(x=1000,y=230)

agregarNombre = Entry(agregarContactoFrame, width=200)
agregarNombre.insert(0,'Nombre')
agregarNombre.pack(pady=8)

agregarCorreo = Entry(agregarContactoFrame, width=200)
agregarCorreo.insert(0,'Correo')
agregarCorreo.pack(pady=8)

agregarTelefono = Entry(agregarContactoFrame, width=200)
agregarTelefono.insert(0,'Telefono')
agregarTelefono.pack(pady=8)
#MANTENIMIENTO

def openMantenimientoMenu():
        global mantenimientoContainer
        global añadirFrame

        #En mantenimiento container se almacena todo lo relacionado con las selecciones de mantenimiento
        mantenimientoContainer = Frame(root)
        mantenimientoContainer.place(x=0,y=28)
   
        mantenimientoFrame = Frame(mantenimientoContainer)
        mantenimientoFrame.pack(side='left')
        
        añadirButton = Button(mantenimientoFrame, text="Añadir",command=lambda: [openAñadirFrame(),añadirFrame.destroy])
        añadirButton.pack(pady=12,padx=10)

        modificarButton = Button(mantenimientoFrame, text="Modificar", command=lambda: openModificarFrame())
        modificarButton.pack(pady=12,padx=10)

        buscarButton = Button(mantenimientoFrame, text="Buscar", command=lambda: openBuscarFrame())
        buscarButton.pack(pady=12,padx=10)

        eliminarButton = Button(mantenimientoFrame, text="Eliminar", command=lambda: openEliminarFrame())
        eliminarButton.pack(pady=12,padx=10)

        cerrarVentana = Button(mantenimientoFrame, text="Cerrar ventana", command=mantenimientoContainer.destroy)
        cerrarVentana.pack(pady=12,padx=10)


def openAñadirFrame():
    global añadirFrame

    # Crear el nuevo frame para el menú de añadir
    añadirFrame = Frame(mantenimientoContainer)
    añadirFrame.pack()

    #Abrir frame de añadir pais
    añadirPaisButton = Button(añadirFrame, text="Añadir un pais", command=lambda: añadirPais())
    añadirPaisButton.pack(pady=12,padx=10)

    def añadirPais():
         
        ventanaPaisNuevo = Tk()
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
         
    


    #Abrir frame de añadir ciudad
    añadirCiudadButton = Button(añadirFrame, text="Añadir una ciudad", command=lambda: añadirCiudad())
    añadirCiudadButton.pack(pady=12,padx=10)

    def añadirCiudad():

        ventanaCiudadNueva = Tk()
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
            

    #Abrir frame de añadir clientes
    añadirClienteButton = Button(añadirFrame, text="Añadir un cliente", command=lambda: añadirCliente())
    añadirClienteButton.pack(pady=12,padx=10)

    def añadirCliente():

        ventanaClienteNuevo = Tk()
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

    #Abrir frame de añadir mascotas
    añadirMascotasButton = Button(añadirFrame, text="Añadir una mascota", command=lambda: añadirMascota())
    añadirMascotasButton.pack(pady=12,padx=10)

    def añadirMascota():

        ventanaMascotaNueva = Tk()
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

    #Abrir frame de añadir visitas
    añadirVisitasButton = Button(añadirFrame, text="Añadir una visita", command=lambda: añadirVisitas())
    añadirVisitasButton.pack(pady=12,padx=10)

    def añadirVisitas():

        ventanaVisitaNueva = Tk()
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

    #Abrir frame de añadir tratamientos
    añadirTratamientosButton = Button(añadirFrame, text="Añadir un tratamiento", command=lambda: añadirTratamientos())
    añadirTratamientosButton.pack(pady=12,padx=10)

    def añadirTratamientos():

        ventanaTratamientoNuevo = Tk()
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
     

    #Abrir frame de añadir medicaciones
    añadirMedicacionButton = Button(añadirFrame, text="Añadir una medicacion", command=lambda: añadirMedicacion())
    añadirMedicacionButton.pack(pady=12,padx=10)

    def añadirMedicacion():

        ventanaMedicacionNueva = Tk()
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

        cerrarAñadirFrame = Button(añadirFrame, text='Cerrar ventana', command=añadirFrame.destroy)
        cerrarAñadirFrame.pack(pady=12, padx=10)

    cerrarAñadir = Button(añadirFrame,text="Cerrar ventana", command=añadirFrame.destroy)
    cerrarAñadir.pack(pady=8)

def openModificarFrame():
    # Crear el nuevo frame para el menú de modificar
    modificarFrame = Frame(mantenimientoContainer)
    modificarFrame.pack()

    modificarPaisButton = Button(modificarFrame, text="Modificar un pais")
    modificarPaisButton.pack(pady=8)

    modificarCiudadButton = Button(modificarFrame, text="Modificar una ciudad")
    modificarCiudadButton.pack(pady=8)

    modificarClienteButton = Button(modificarFrame, text="Modificar un cliente")
    modificarClienteButton.pack(pady=8)

    modificarMascotaButton = Button(modificarFrame, text="Modificar una mascota")
    modificarMascotaButton.pack(pady=8)

    modificarVisitaButton = Button(modificarFrame, text="Modificar una visita")
    modificarVisitaButton.pack(pady=8)

    modificarTratamientoButton = Button(modificarFrame, text="Modificar un tratamiento")
    modificarTratamientoButton.pack(pady=8)

    modificarMedicacionButton = Button(modificarFrame, text="Modificar una medicacion")
    modificarMedicacionButton.pack(pady=8)

    cerrarModificar = Button(modificarFrame, text="Cerrar ventana", command=modificarFrame.destroy)
    cerrarModificar.pack(pady=8)

def openBuscarFrame():
    # Crear el nuevo frame para el menú de buscar
    buscarFrame = Frame(mantenimientoContainer)
    buscarFrame.pack()

    buscarPaisButton = Button(buscarFrame, text="Buscar un pais")
    buscarPaisButton.pack(pady=8)

    buscarCiudadButton = Button(buscarFrame, text="Buscar una ciudad")
    buscarCiudadButton.pack(pady=8)

    buscarClienteButton = Button(buscarFrame, text="Buscar un cliente")
    buscarClienteButton.pack(pady=8)

    buscarMascotaButton = Button(buscarFrame, text="Buscar una mascota")
    buscarMascotaButton.pack(pady=8)

    buscarVisitaButton = Button(buscarFrame, text="Buscar una visita")
    buscarVisitaButton.pack(pady=8)

    buscarTratamientoButton = Button(buscarFrame, text="Buscar un tratamiento")
    buscarTratamientoButton.pack(pady=8)

    buscarMedicacionButton = Button(buscarFrame, text="Buscar una mediacion")
    buscarMedicacionButton.pack(pady=8)

    cerrarBuscarButton = Button(buscarFrame, text="Cerra ventana", command= buscarFrame.destroy)
    cerrarBuscarButton.pack(pady=8)

def openEliminarFrame():
    # Crear el nuevo frame para el menú de eliminar
    eliminarFrame = Frame(mantenimientoContainer)
    eliminarFrame.pack()

    eliminarPaisButton = Button(eliminarFrame, text="Eliminar un pais")
    eliminarPaisButton.pack(pady=8)

    eliminarCiudadButton = Button(eliminarFrame, text="Eliminar una ciudad")
    eliminarCiudadButton.pack(pady=8)

    eliminarClienteButton = Button(eliminarFrame, text="Eliminar un cliente")
    eliminarClienteButton.pack(pady=8)

    eliminarMascotaButton = Button(eliminarFrame, text="Eliminar una mascota")
    eliminarMascotaButton.pack(pady=8)

    eliminarVisitaButton = Button(eliminarFrame, text="Eliminar una visita")
    eliminarVisitaButton.pack(pady=8)

    eliminarTratamientoButton = Button(eliminarFrame, text="Eliminar un tratamiento")
    eliminarTratamientoButton.pack(pady=8)

    eliminarMedicacionButton = Button(eliminarFrame, text="Eliminar una medicacion")
    eliminarMedicacionButton.pack(pady=8)

    cerrarEliminar = Button(eliminarFrame, text="Cerrar ventana", command=eliminarFrame.destroy)
    cerrarEliminar.pack(pady=8)

#REPORTES

def openReportesMenu():
    global reportesContainer

    reportesContainer = Frame(root)
    reportesContainer.place(x=350, y=28)

    reportesFrame = Frame(reportesContainer)
    reportesFrame.pack()

    verReportesButton = Button(reportesFrame,text="Ver reportes solicitados")
    verReportesButton.pack(pady=8)

    solicitarReportesButton = Button(reportesFrame, text="Solicitar reportes")
    solicitarReportesButton.pack(pady=8)

    cerrarReportesContainer = Button(reportesFrame, text="Cerrar ventana",command=reportesFrame.destroy)
    cerrarReportesContainer.pack(pady=8)


#FACTURACION

def openFacturacionMenu():

    facturacionContainer = Frame(root)
    facturacionContainer.place(x=700, y=28)

    facturacionFrame = Frame(facturacionContainer)
    facturacionFrame.pack()

    saldosButton = Button(facturacionFrame, text="Ver saldos de clientes")
    saldosButton.pack(pady=8)

    descuentosButton = Button(facturacionFrame,text="Ver descuentos de clientes")
    descuentosButton.pack(pady=8)

    facturacionButton = Button(facturacionFrame, text="Ver facturacion de clientes")
    facturacionButton.pack(pady=8)

    cerrarFacturacion = Button(facturacionFrame, text="Cerrar ventana", command=facturacionFrame.destroy)
    cerrarFacturacion.pack(pady=8)

#ACERCA DE

def openAcercaDeMenu():

    acercaContainer = Frame(root)
    acercaContainer.place(x=1000, y=28)

    acercaFrame = Frame(acercaContainer)
    acercaFrame.pack(pady=8)

    fabricio = Label(acercaFrame, text="Cesar Fabricio Herrera")
    fabricio.pack(pady=8)

    david = Label(acercaFrame, text="David Lopez")
    david.pack(pady=8)

    cerrarAcerca = Button(acercaFrame, text="Cerrar ventana", command=acercaFrame.destroy)
    cerrarAcerca.pack(pady=8)
######## MENUS DE ICONOS#########

def openlugaresMenu():

    global lugaresContainer

    lugaresContainer = Frame(root)
    lugaresContainer.place(x=70,y=400)

    lugaresFrame = Frame(lugaresContainer)
    lugaresFrame.pack(side='left')

    PaisesButton = Button(lugaresFrame, text="Países",image=ImagenPaises,command=lambda:[openSubmenuPaisesMenu(),submenuCiudadesContainer.destroy()])
    PaisesButton.pack(pady=12,padx=10)

    CiudadesButton = Button(lugaresFrame, text="Ciudades",image=ImagenCiudades,command=lambda:[openSubmenuPaisesCiudadesMenu(),submenuPaisesContainer.destroy()])
    CiudadesButton.pack(pady=12,padx=10)

    lugaresCerrarButton = Button(lugaresFrame, text="Cerrar",image=ImagenX,command=lambda:[lugaresContainer.destroy(),submenuPaisesContainer.destroy(),submenuCiudadesContainer.destroy()])
    lugaresCerrarButton.pack(pady=12,padx=10)

def openclientesMenu(): 
    global clientesContainer
    
    clientesContainer = Frame(root)
    clientesContainer.place(x=430,y=400)

    clientesFrame = Frame(clientesContainer)
    clientesFrame.pack(side='left')

    clientesButton = Button(clientesFrame, text="Clientes",image=ImagenClientesSub,command=lambda:[openSubmenuClientesMenu(),submenuMascotasContainer.destroy(),submenuVisitasContainer.destroy()])
    clientesButton.pack(pady=12,padx=10)

    mascotasButton = Button(clientesFrame, text="Mascotas",image=ImagenMascotas,command=lambda:[openSubmenuMascotasMenu(),submenuClientesContainer.destroy(),submenuVisitasContainer.destroy()])
    mascotasButton.pack(pady=12,padx=10)

    VisitasButton = Button(clientesFrame, text="Visitas",image=ImagenVisitas,command=lambda:[openSubmenuVisitasMenu(),submenuClientesContainer.destroy(),submenuMascotasContainer.destroy()])
    VisitasButton.pack(pady=12,padx=10)

    clientesCerrarButton = Button(clientesFrame, text="Cerrar",image=ImagenX,command=lambda:[clientesContainer.destroy(),submenuClientesContainer.destroy(),submenuMascotasContainer.destroy(),submenuVisitasContainer.destroy()])
    clientesCerrarButton.pack(pady=12,padx=10)

def openclinicaMenu():
    global clinicaContainer

    clinicaContainer = Frame(root)
    clinicaContainer.place(x=770,y=400)

    clinicaFrame = Frame(clinicaContainer)
    clinicaFrame.pack(side='left')

    tratamientosButton = Button(clinicaFrame, text="Tratamientos",image=ImagenTratamientos,command=lambda:[openSubmenuTratamientosMenu(),submenuMedicamentosContainer.destroy()])
    tratamientosButton.pack(pady=12,padx=10)

    medicamentosButton = Button(clinicaFrame, text="Medicamentos",image=ImagenMedicamentos,command=lambda:[openSubmenuMedicamentosMenu(),submenuTratamientosContainer.destroy()])
    medicamentosButton.pack(pady=12,padx=10)

    clinicaCerrarButton = Button(clinicaFrame, text="Cerrar",image=ImagenX,command=lambda:[clinicaContainer.destroy(),submenuTratamientosContainer.destroy(),submenuMedicamentosContainer.destroy()])
    clinicaCerrarButton.pack(pady=12,padx=10)

def openfacturacionMenu():
    global facturacionContainer

    facturacionContainer = Frame(root)
    facturacionContainer.place(x=1070,y=400)

    facturacionFrame = Frame(facturacionContainer)
    facturacionFrame.pack(side='left')

    facturacionButton = Button(facturacionFrame, text="Facturación",image=ImagenFacturacionSub,command=lambda:[openSubmenuFacturacionMenu(),submenuDescuentosContainer.destroy(),submenuSaldoContainer.destroy()])
    facturacionButton.pack(pady=12,padx=10)

    descuentoButton = Button(facturacionFrame, text="Descuento",image=ImagenDescuentos,command=lambda:[openSubmenuDescuentosMenu(),submenuFacturacionContainer.destroy(),submenuSaldoContainer.destroy()])
    descuentoButton.pack(pady=12,padx=10)

    saldoButton = Button(facturacionFrame, text="Saldo",image=ImagenSaldo,command=lambda:[openSubmenuSaldoMenu(),submenuFacturacionContainer.destroy(),submenuDescuentosContainer.destroy()])
    saldoButton.pack(pady=12,padx=10)

    facturacionCerrarButton = Button(facturacionFrame, text="Cerrar",image=ImagenX,command=lambda:[facturacionContainer.destroy(),submenuFacturacionContainer.destroy(),submenuDescuentosContainer.destroy(),submenuSaldoContainer.destroy()])
    facturacionCerrarButton.pack(pady=12,padx=10)


#########   SUBMENUS    #########

#Lugares

def openSubmenuPaisesMenu():

    global submenuPaisesContainer

    submenuPaisesContainer = Frame(root)
    submenuPaisesContainer.place(x=180,y=370)

    modificarPaisesFrame = Frame(submenuPaisesContainer)
    modificarPaisesFrame.pack(side='left')

    modificarPaisesLabel = Label(modificarPaisesFrame,image=ImagenPaises,text='')
    modificarPaisesLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarPaisesFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarPaisesFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarPaisesFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarPaisesFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarPaisesFrame, text="Cerrar",command=submenuPaisesContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuPaisesCiudadesMenu():

    global submenuCiudadesContainer

    submenuCiudadesContainer = Frame(root)
    submenuCiudadesContainer.place(x=180,y=370)

    modificarCiudadesFrame = Frame(submenuCiudadesContainer)
    modificarCiudadesFrame.pack(side='left')

    modificarCiudadesLabel = Label(modificarCiudadesFrame,image=ImagenCiudades,text='')
    modificarCiudadesLabel.pack(pady=12,padx=10)

    insercionCiudadButton = Button(modificarCiudadesFrame, text="Inserción")
    insercionCiudadButton.pack(pady=12,padx=10)

    ModificacionCiudadButton = Button(modificarCiudadesFrame, text="Modificación")
    ModificacionCiudadButton.pack(pady=12,padx=10)

    BusquedaCiudadButton = Button(modificarCiudadesFrame, text="Busqueda")
    BusquedaCiudadButton.pack(pady=12,padx=10)

    EliminacionCiudadButton =  Button(modificarCiudadesFrame, text="Eliminación")
    EliminacionCiudadButton.pack(pady=12,padx=10)

    CiudadCerrarButton = Button(modificarCiudadesFrame, text="Cerrar",command=submenuCiudadesContainer.destroy)
    CiudadCerrarButton.pack(pady=12,padx=10)

#Cliente

def openSubmenuClientesMenu():

    global submenuClientesContainer

    submenuClientesContainer = Frame(root)
    submenuClientesContainer.place(x=500,y=370)

    modificarClientesFrame = Frame(submenuClientesContainer)
    modificarClientesFrame.pack(side='left')

    modificarClientesLabel = Label(modificarClientesFrame,image=ImagenClientesSub, text='')
    modificarClientesLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarClientesFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarClientesFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarClientesFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarClientesFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarClientesFrame, text="Cerrar",command=submenuClientesContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuMascotasMenu():

    global submenuMascotasContainer

    submenuMascotasContainer = Frame(root)
    submenuMascotasContainer.place(x=500,y=370)

    modificarMascotasFrame = Frame(submenuMascotasContainer)
    modificarMascotasFrame.pack(side='left')

    modificarMascotasLabel = Label(modificarMascotasFrame,image=ImagenMascotas, text='')
    modificarMascotasLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarMascotasFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarMascotasFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarMascotasFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarMascotasFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarMascotasFrame, text="Cerrar",command=submenuMascotasContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuVisitasMenu():

    global submenuVisitasContainer

    submenuVisitasContainer = Frame(root)
    submenuVisitasContainer.place(x=500,y=370)

    modificarVisitasFrame = Frame(submenuVisitasContainer)
    modificarVisitasFrame.pack(side='left')

    modificarVisitasLabel = Label(modificarVisitasFrame,image=ImagenVisitas,text='')
    modificarVisitasLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarVisitasFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarVisitasFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarVisitasFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarVisitasFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarVisitasFrame, text="Cerrar",command=submenuVisitasContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

#Clinica

def openSubmenuTratamientosMenu():
      
    global submenuTratamientosContainer

    submenuTratamientosContainer = Frame(root)
    submenuTratamientosContainer.place(x=850,y=370)

    modificarTratamientosFrame = Frame(submenuTratamientosContainer)
    modificarTratamientosFrame.pack(side='left')

    modificarTratamientosLabel = Label(modificarTratamientosFrame,image=ImagenTratamientos, text='')
    modificarTratamientosLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarTratamientosFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarTratamientosFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarTratamientosFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarTratamientosFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarTratamientosFrame, text="Cerrar",command=submenuTratamientosContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuMedicamentosMenu():
      
    global submenuMedicamentosContainer

    submenuMedicamentosContainer = Frame(root)
    submenuMedicamentosContainer.place(x=850,y=370)

    modificarMedicamentosFrame = Frame(submenuMedicamentosContainer)
    modificarMedicamentosFrame.pack(side='left')

    modificarMedicamentosLabel = Label(modificarMedicamentosFrame,image=ImagenMedicamentos ,text='')
    modificarMedicamentosLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarMedicamentosFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarMedicamentosFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarMedicamentosFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarMedicamentosFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarMedicamentosFrame, text="Cerrar",command=submenuMedicamentosContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

#Facturacion

def openSubmenuFacturacionMenu():

    global submenuFacturacionContainer

    submenuFacturacionContainer =Frame(root)
    submenuFacturacionContainer.place(x=1170,y=370)

    modificarFacturacionFrame =Frame(submenuFacturacionContainer)
    modificarFacturacionFrame.pack(side='left')

    modificarFacturacionLabel = Label(modificarFacturacionFrame,image=ImagenFacturacionSub, text='')
    modificarFacturacionLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarFacturacionFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarFacturacionFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarFacturacionFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarFacturacionFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarFacturacionFrame, text="Cerrar",command=submenuFacturacionContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuDescuentosMenu():

    global submenuDescuentosContainer

    submenuDescuentosContainer = Frame(root)
    submenuDescuentosContainer.place(x=1170,y=370)

    modificarDescuentosFrame = Frame(submenuDescuentosContainer)
    modificarDescuentosFrame.pack(side='left')

    modificarDescuentosLabel = Label(modificarDescuentosFrame,image=ImagenDescuentos, text='')
    modificarDescuentosLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarDescuentosFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarDescuentosFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarDescuentosFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarDescuentosFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarDescuentosFrame, text="Cerrar",command=submenuDescuentosContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)

def openSubmenuSaldoMenu():

    global submenuSaldoContainer

    submenuSaldoContainer = Frame(root)
    submenuSaldoContainer.place(x=1170,y=370)

    modificarSaldoFrame = Frame(submenuSaldoContainer)
    modificarSaldoFrame.pack(side='left')

    modificarSaldoLabel = Label(modificarSaldoFrame,image=ImagenSaldo, text='')
    modificarSaldoLabel.pack(pady=12,padx=10)

    insercionPaisButton = Button(modificarSaldoFrame, text="Inserción")
    insercionPaisButton.pack(pady=12,padx=10)

    ModificacionPaisButton = Button(modificarSaldoFrame, text="Modificación")
    ModificacionPaisButton.pack(pady=12,padx=10)

    BusquedaPaisButton = Button(modificarSaldoFrame, text="Busqueda")
    BusquedaPaisButton.pack(pady=12,padx=10)

    EliminacionPaisButton =  Button(modificarSaldoFrame, text="Eliminación")
    EliminacionPaisButton.pack(pady=12,padx=10)

    PaisCerrarButton = Button(modificarSaldoFrame, text="Cerrar",command=submenuSaldoContainer.destroy)
    PaisCerrarButton.pack(pady=12,padx=10)



#########   IMAGENES    #########

#IMAGENES MENU

ImagenLugares = PhotoImage(file='img/Lugares.png')

ImagenClinica = PhotoImage(file="img/Clinica.png")

ImagenClientes = PhotoImage(file="img/Clientes.png")

ImagenFacturacion = PhotoImage(file="img/Facturacion.png")

ImagenX = PhotoImage(file="img/X.png")


#IMAGENES SUBMENUS

ImagenPaises = PhotoImage(file="img/Paises.png")

ImagenCiudades = PhotoImage(file="img/Ciudades.png")

ImagenClientesSub = PhotoImage(file="img/Clientes_SubMenu.png")

ImagenMascotas = PhotoImage(file="img/Mascotas.png")

ImagenVisitas = PhotoImage(file="img/Visitas.png")

ImagenTratamientos = PhotoImage(file="img/Tratamientos.png")

ImagenMedicamentos = PhotoImage(file="img/Medicamentos.png")

ImagenFacturacionSub = PhotoImage(file="img/Facturacion_SubMenu.png")

ImagenDescuentos = PhotoImage(file="img/Descuentos.png")

ImagenSaldo = PhotoImage(file="img/Saldo.png")


#########   BOTONES MENUS    #########
# LUGARES
lugaresButtomFrame = Frame(root)
lugaresButtomFrame.place(x=0,y=450)
lugaresButtom = Button(lugaresButtomFrame, text="Lugares",image=ImagenLugares, command=openlugaresMenu)
lugaresButtom.pack()

# CLIENTES
clientesButtomFrame = Frame(root)
clientesButtomFrame.place(x=350,y=450)
clienteButtom = Button(clientesButtomFrame, text="Clientes",image=ImagenClientes, command=openclientesMenu)
clienteButtom.pack()

# CLINICA
clinicaButtomFrame = Frame(root)
clinicaButtomFrame.place(x=700,y=450)
clinicaButtom = Button(clinicaButtomFrame, text="Clínica",image=ImagenClinica, command=openclinicaMenu)
clinicaButtom.pack()

#FACTURACION
facturacionButtomFrame = Frame(root)
facturacionButtomFrame.place(x=1000,y=450)
facturacionButtom = Button(facturacionButtomFrame, text="Facturación",image=ImagenFacturacion, command=openfacturacionMenu)
facturacionButtom.pack()


root.mainloop()
