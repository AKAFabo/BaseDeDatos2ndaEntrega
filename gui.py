#Importar libreria de GUI
from tkinter import messagebox as MessageBox
from tkinter import *

#Importar ventanas

from Utils.VentanasAgregar import añadirPais, añadirCiudad, añadirCliente, añadirVisitas, añadirMascota, añadirMedicacion, añadirTratamientos


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

    #Abrir frame de añadir ciudad
    añadirCiudadButton = Button(añadirFrame, text="Añadir una ciudad", command=lambda: añadirCiudad())
    añadirCiudadButton.pack(pady=12,padx=10)        

    #Abrir frame de añadir clientes
    añadirClienteButton = Button(añadirFrame, text="Añadir un cliente", command=lambda: añadirCliente())
    añadirClienteButton.pack(pady=12,padx=10)

    #Abrir frame de añadir mascotas
    añadirMascotasButton = Button(añadirFrame, text="Añadir una mascota", command=lambda: añadirMascota())
    añadirMascotasButton.pack(pady=12,padx=10)

    #Abrir frame de añadir visitas
    añadirVisitasButton = Button(añadirFrame, text="Añadir una visita", command=lambda: añadirVisitas())
    añadirVisitasButton.pack(pady=12,padx=10)

    #Abrir frame de añadir tratamientos
    añadirTratamientosButton = Button(añadirFrame, text="Añadir un tratamiento", command=lambda: añadirTratamientos())
    añadirTratamientosButton.pack(pady=12,padx=10)

    #Abrir frame de añadir medicaciones
    añadirMedicacionButton = Button(añadirFrame, text="Añadir una medicacion", command=lambda: añadirMedicacion())
    añadirMedicacionButton.pack(pady=12,padx=10)

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

    insercionPaisButton = Button(modificarPaisesFrame, text="Inserción",command=lambda: añadirPais() )
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

    insercionCiudadButton = Button(modificarCiudadesFrame, text="Inserción",command=lambda: añadirCiudad())
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

    insercionPaisButton = Button(modificarClientesFrame, text="Inserción", command=lambda:añadirCliente())
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

    insercionPaisButton = Button(modificarMascotasFrame, text="Inserción", command=lambda:añadirMascota())
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

    insercionPaisButton = Button(modificarVisitasFrame, text="Inserción",command=lambda: añadirVisitas())
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

    insercionPaisButton = Button(modificarTratamientosFrame, text="Inserción",command=lambda:añadirTratamientos())
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

    insercionPaisButton = Button(modificarMedicamentosFrame, text="Inserción",command=lambda:añadirMedicacion())
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
