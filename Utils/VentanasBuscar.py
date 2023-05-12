from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from tkinter import *
from tkinter import messagebox as MessageBox

def buscarPais():

    global ListaDePaises
    global codigosPaisesValidos

    ventanaBuscarPais = Tk()
    ventanaBuscarPais.title("Buscar pais")
    ventanaBuscarPais.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarPais, width=200)
    buscarEntry.insert(0,"Digite el codigo de pais a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarPais, text="Buscar pais", command=lambda:searchCountry())
    buscarButton.pack(pady=8,padx=8)

    def searchCountry():

        codigo = buscarEntry.get()

        if codigo not in codigosPaisesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDePaises)):

                if ListaDePaises[i][0] == codigo:
                    MessageBox.showinfo("Buscar pais",f"El pais {codigo} es:\n {ListaDePaises[i]}")
                    break

    ventanaBuscarPais.mainloop()


def buscarCiudad():

    ventanaBuscarCiudad = Tk()
    ventanaBuscarCiudad.title("Buscar ciudad")
    ventanaBuscarCiudad.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarCiudad, width=200)
    buscarEntry.insert(0,"Digite el codigo de ciudad a buscar")
    buscarEntry.pack(pady=8,padx=8)

    buscarButton = Button(ventanaBuscarCiudad, text="Buscar ciudad", command=lambda:searchCity())
    buscarButton.pack(pady=8,padx=10)

    def searchCity():

        codigo = buscarEntry.get()

        if codigo not in codigosCiudadesValidos:
            MessageBox.showerror('Error',"El codigo ingresado no existe")
        else:

            for i in range (len(ListaDeCiudades)):

                if ListaDeCiudades[i][1] == codigo:
                    MessageBox.showinfo("Buscar ciudad",f"La ciudad {codigo} es:\n {ListaDeCiudades[i]}")
                    break

    ventanaBuscarCiudad.mainloop()

def buscarCliente():

    ventanaBuscarCliente = Tk()
    ventanaBuscarCliente.title("Buscar cliente")
    ventanaBuscarCliente.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarCliente, width=200)
    buscarEntry.insert(0,"Digite el codigo de cliente a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarCliente, text="Buscar cliente", command=lambda: searchClient())
    buscarButton.pack(pady=8,padx=10)

    def searchClient():

        codigo = buscarEntry.get()

        if codigo not in codigosClientesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:
                    MessageBox.showinfo("Buscar cliente",f"El cliente {codigo} es:\n {ListaDeClientes[i]}")
                    break

    ventanaBuscarCliente.mainloop()

def buscarMascota():

    ventanaBuscarMascota = Tk()
    ventanaBuscarMascota.title("Buscar mascota")
    ventanaBuscarMascota.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarMascota, width=200)
    buscarEntry.insert(0,"Digite el codigo de mascota a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarMascota, text="Buscar mascota", command=lambda: searchPet())
    buscarButton.pack(pady=8,padx=10)

    def searchPet():

        codigo = buscarEntry.get()

        if codigo not in codigosMascotasValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeMascotas)):

                if ListaDeMascotas[i][1] == codigo:
                    MessageBox.showinfo("Buscar mascota",f"La mascota {codigo} es:\n {ListaDeMascotas[i]}")
                    break

    ventanaBuscarMascota.mainloop()

def buscarVisita():

    ventanaBuscarVisita = Tk()
    ventanaBuscarVisita.title("Buscar visita")
    ventanaBuscarVisita.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarVisita, width=200)
    buscarEntry.insert(0,"Digite el codigo de visita a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarVisita, text="Buscar visita", command=lambda: searchVisit())
    buscarButton.pack(padx=10,pady=8)

    def searchVisit():

        codigo = buscarEntry.get()

        if codigo not in codigosVisitasValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeVisitas)):

                if ListaDeVisitas[i][0] == codigo:
                    MessageBox.showinfo('Buscar visita',f"La visita {codigo} es\n {ListaDeVisitas[i]}")
                    break

    ventanaBuscarVisita.mainloop()

def buscarTratamiento():

    ventanaBuscarTratamiento = Tk()
    ventanaBuscarTratamiento.title("Buscar tratamiento")
    ventanaBuscarTratamiento.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarTratamiento, width=200)
    buscarEntry.insert(0,"Digite el codigo de tratamiento a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarTratamiento, text="Buscar tratamiento", command=lambda:searchTreat())
    buscarButton.pack(pady=8,padx=10)

    def searchTreat():

        codigo = buscarEntry.get()

        if codigo not in codigosTratamientosValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")
        else:

            for i in range(len(ListaDeTratamientos)):

                if ListaDeTratamientos[i][0] == codigo:
                    MessageBox.showinfo("Buscar visita",f"El tratamiento {codigo} es\n {ListaDeTratamientos[i]}")
                    break

    ventanaBuscarTratamiento.mainloop()

def buscarMedicacion():

    ventanaBuscarMedicacion = Tk()
    ventanaBuscarMedicacion.title("Buscar medicacion")
    ventanaBuscarMedicacion.geometry("300x100")

    buscarEntry = Entry(ventanaBuscarMedicacion, width=200)
    buscarEntry.insert(0,"Digite el codigo de medicacion a buscar")
    buscarEntry.pack(pady=8,padx=10)

    buscarButton = Button(ventanaBuscarMedicacion, text="Buscar medicacion", command=lambda:searchMed())
    buscarButton.pack(pady=8,padx=10)

    def searchMed():

        codigo = buscarEntry.get()

        if codigo not in codigosMedicacionValidos:
            MessageBox.showerror("Error","El codigo ingresado")
        else:

            for i in range (len(ListaDeMedicacion)):

                if ListaDeMedicacion[i][1] == codigo:
                    MessageBox.showinfo("Buscar medicacion",f"La medicacion {codigo} es\n {ListaDeMedicacion[i]}")
                    break

    ventanaBuscarMedicacion.mainloop()

        