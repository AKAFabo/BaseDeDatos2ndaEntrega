from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from tkinter import *
from tkinter import messagebox as MessageBox


#Ventana de eliminar pais

def eliminarPais():

    ventanaPaisEliminado = Tk()
    ventanaPaisEliminado.title("Eliminar pais")
    ventanaPaisEliminado.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaPaisEliminado,text="Indique el codigo de pais a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarCodigoEntry = Entry(ventanaPaisEliminado, width=200)
    eliminarCodigoEntry.pack(pady=8, padx=10)

    eliminarCodigoButton = Button(ventanaPaisEliminado, text="Eliminar pais", command=lambda:[deleteCountry(),ventanaPaisEliminado.destroy()])
    eliminarCodigoButton.pack(pady=8,padx=10)

    def deleteCountry():

        codigo = eliminarCodigoEntry.get()

        if codigo not in codigosPaisesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range (len(ListaDePaises)):

                if ListaDePaises[i][0] == codigo:
                    ListaDePaises.pop(i)
                    break

            for i in range (len(codigosPaisesValidos)):

                if codigosPaisesValidos[i] == codigo:
                    codigosPaisesValidos.pop(i)
                    MessageBox.showinfo("Base de datos","El pais ha sido eliminado con exito")
                    break

    ventanaPaisEliminado.mainloop()


#Ventana de eliminar ciudad

def eliminarCiudad():

    ventanaCiudadEliminada = Tk()
    ventanaCiudadEliminada.title("Eliminar ciudad")
    ventanaCiudadEliminada.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaCiudadEliminada,text="Indique el codigo de ciudad a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarCodigoEntry = Entry(ventanaCiudadEliminada, width=200)
    eliminarCodigoEntry.pack(pady=8,padx=10)

    eliminarCodigoButton = Button(ventanaCiudadEliminada, text="Eliminar ciudad", command=lambda:[deleteCity(),ventanaCiudadEliminada.destroy()])
    eliminarCodigoButton.pack(pady=8,padx=10)

    def deleteCity():

        codigo = eliminarCodigoEntry.get()

        if codigo not in codigosCiudadesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:
            
            for i in range(len(ListaDeCiudades)):

                if ListaDeCiudades[i][1] == codigo:
                    ListaDeCiudades.pop(i)
                    break

            for i in range (len(codigosCiudadesValidos)):

                if codigosCiudadesValidos[i] == codigo:
                    codigosCiudadesValidos.pop(i)
                    MessageBox.showinfo("Base de datos","La ciudad ha sido eliminada con exito")
                    break

    ventanaCiudadEliminada.mainloop()

#Ventana de eliminar cliente

def eliminarCliente():

    ventanaClienteEliminado = Tk()
    ventanaClienteEliminado.title("Eliminar cliente")
    ventanaClienteEliminado.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaClienteEliminado,text="Indique el codigo de cliente a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarCodigoEntry = Entry(ventanaClienteEliminado, width=200)
    eliminarCodigoEntry.pack(pady=8,padx=8)

    eliminarCodigoButton = Button(ventanaClienteEliminado, text="Eliminar cliente", command=lambda:[deleteClient(),ventanaClienteEliminado.destroy()])
    eliminarCodigoButton.pack(pady=8,padx=10)

    def deleteClient():

        codigo = eliminarCodigoEntry.get()

        if codigo not in codigosClientesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range (len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:
                    ListaDeClientes.pop(i)
                    break

            for i in range (len(codigosClientesValidos)):
                
                if codigosClientesValidos[i] == codigo:
                    codigosClientesValidos.pop(i)
                    MessageBox.showinfo("Base de datos","El cliente ha sido eliminado con exito")
                    break

    ventanaClienteEliminado.mainloop()

#Ventana de eliminar mascota

def eliminarMascota():

    ventanaMascotaEliminada = Tk()
    ventanaMascotaEliminada.title("Eliminar mascota")
    ventanaMascotaEliminada.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaMascotaEliminada,text="Indique el codigo de mascota a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarMascotaEntry = Entry(ventanaMascotaEliminada, width=200)
    eliminarMascotaEntry.pack(pady=8,padx=10)

    eliminarMascotaButton = Button(ventanaMascotaEliminada, text="Eliminar mascota", command=lambda:[deletePet(),ventanaMascotaEliminada.destroy()])
    eliminarMascotaButton.pack(padx=10,pady=8)

    def deletePet():

        codigo = eliminarMascotaEntry.get()

        if codigo not in codigosMascotasValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeMascotas)):

                if ListaDeMascotas[i][1] == codigo:
                    ListaDeMascotas.pop(i)
                    break
            
            for i in range (len(codigosMascotasValidos)):

                if codigosMascotasValidos[i] == codigo:
                    codigosMascotasValidos.pop(i)
                    MessageBox.showinfo("Base de datos","La mascota ha sido eliminada con exito")
                    break

    ventanaMascotaEliminada.mainloop()

#Ventana de eliminar visita

def eliminarVisita():

    ventanaEliminarVisita = Tk()
    ventanaEliminarVisita.title("Eliminar visita")
    ventanaEliminarVisita.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaEliminarVisita,text="Indique el codigo de visita a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarVisitaEntry = Entry(ventanaEliminarVisita, width=200)
    eliminarVisitaEntry.pack(pady=8,padx=10)

    eliminarVisitaButton = Button(ventanaEliminarVisita, text="Eliminar visita", command=lambda:[deleteVisit(),ventanaEliminarVisita.destroy()])
    eliminarVisitaButton.pack(pady=8,padx=10)

    def deleteVisit():

        codigo = eliminarVisitaEntry.get()

        if codigo not in codigosVisitasValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeVisitas)):

                if ListaDeVisitas[i][0] == codigo:
                    ListaDeVisitas.pop(i)
                    break

            for i in range (len(codigosVisitasValidos)):

                if codigosVisitasValidos[i] == codigo:
                    codigosVisitasValidos.pop(i)
                    MessageBox.showinfo("Base de datos","La visita ha sido eliminada con exito")
                    break

    ventanaEliminarVisita.mainloop()

#Ventana de eliminar tratamiento

def eliminarTratamiento():

    ventanaEliminarTratamiento = Tk()
    ventanaEliminarTratamiento.title("Eliminar tratamiento")
    ventanaEliminarTratamiento.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaEliminarTratamiento,text="Indique el codigo de tratamiento a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarTratamientoEntry = Entry(ventanaEliminarTratamiento, width=200)
    eliminarTratamientoEntry.pack(pady=8,padx=10)

    eliminarTratamientoButton = Button(ventanaEliminarTratamiento, text="Eliminar tratamiento", command=lambda:[deleteTreat(),ventanaEliminarTratamiento.destroy()])
    eliminarTratamientoButton.pack(pady=8,padx=10)

    def deleteTreat():

        codigo = eliminarTratamientoEntry.get()

        if codigo not in codigosTratamientosValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeTratamientos)):

                if ListaDeTratamientos[i][0] == codigo:
                    ListaDeTratamientos.pop(i)
                    break

            for i in range(len(codigosTratamientosValidos)):

                if codigosTratamientosValidos[i] == codigo:
                    codigosTratamientosValidos.pop(i)
                    MessageBox.showinfo('Base de datos',"El tratamiento ha sido eliminado con exito")
                    break

    ventanaEliminarTratamiento.mainloop()

#Ventana de eliminar medicacion

def eliminarMedicacion():

    ventanaEliminarMedicacion = Tk()
    ventanaEliminarMedicacion.title("Eliminar medicacion")
    ventanaEliminarMedicacion.geometry("300x150")

    eliminarCodigoLabel = Label(ventanaEliminarMedicacion,text="Indique el codigo de medicacion a eliminar")
    eliminarCodigoLabel.pack(padx=10,pady=8)
    eliminarMedicacionEntry = Entry(ventanaEliminarMedicacion, width=200)
    eliminarMedicacionEntry.pack(padx=10,pady=8)

    eliminarMedicacionButton = Button(ventanaEliminarMedicacion, text="Eliminar medicacion", command=lambda:[deleteMed(),ventanaEliminarMedicacion.destroy()])
    eliminarMedicacionButton.pack(pady=8,padx=10)

    def deleteMed():

        codigo = eliminarMedicacionEntry.get()

        if codigo not in codigosMedicacionValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeMedicacion)):

                if ListaDeMedicacion[i][1] == codigo:
                    ListaDeMedicacion.pop(i)
                    break

            for i in range(len(codigosMedicacionValidos)):

                if codigosMedicacionValidos[i] == codigo:
                    codigosMedicacionValidos.pop(i)
                    MessageBox.showinfo("Base de datos","La medicacion ha sido eliminada con exito")
                    break
