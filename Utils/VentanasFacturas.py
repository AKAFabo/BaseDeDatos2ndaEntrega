from main import (ListaDePaises, ListaDeCiudades,ListaDeClientes,ListaDeMascotas,ListaDeVisitas,ListaDeTratamientos,ListaDeMedicacion
                 ,codigosPaisesValidos,codigosCiudadesValidos,codigosClientesValidos,codigosMascotasValidos,codigosMedicacionValidos,codigosTratamientosValidos,codigosVisitasValidos)

from tkinter import *
from tkinter import messagebox as MessageBox

facturados = []

def generarFactura():

    global ListaDeClientes
    global ListaDeMascotas
    global ListaDeTratamientos
    global ListaDeMedicacion

    ventanaGenerarFactura = Tk()
    ventanaGenerarFactura.title("Generar Factura")
    ventanaGenerarFactura.geometry("300x200")

    FacturaLabel = Label(ventanaGenerarFactura,text="Ingrese el codigo de cliente que desea")
    FacturaLabel.pack(padx=10,pady=8)
    FacturaEntry = Entry(ventanaGenerarFactura, width=200)
    FacturaEntry.pack(pady=8,padx=10)
    
    mascotaLabel = Label(ventanaGenerarFactura,text="Ingrese el codigo de mascota del cliente")
    mascotaLabel.pack(padx=10,pady=8)
    mascotaEntry = Entry(ventanaGenerarFactura,width=200)
    mascotaEntry.pack(padx=10, pady=8)

    FacturaButton = Button(ventanaGenerarFactura, text="Generar factura", command=lambda:[impresionFactura(),ventanaGenerarFactura.destroy()])
    FacturaButton.pack(pady=8,padx=8)

    def impresionFactura():

        global facturados

        Client = []
        Pet = []
        Medicacion = []
        Total = 0
        infoMedicacion = ""
        Descuento = ""
        DescuentoInt = 0
        codigo = FacturaEntry.get()
        mascota = mascotaEntry.get()
 
        if codigo not in codigosClientesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")

        else:
            facturados.append(codigo)

            for i in range(len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:
                    MessageBox.showinfo('Facturacion',"La factura ha sido generada con exito")
                    Client = ListaDeClientes[i]

                    break

        for i in range(len(ListaDeMascotas)):
            if mascota == ListaDeMascotas[i][1]:
                Pet = ListaDeMascotas[i]
                print(Pet)
                break
        
        for i in range(len(ListaDeMedicacion)):
            if Pet[1] == ListaDeMedicacion[i][0]:
                Medicacion += [ListaDeMedicacion[i]]
        
        for i in range(len(Medicacion)):
            Total = Total + int(Medicacion[i][8])
        
        for i in range(len(Medicacion)):
            infoMedicacion = infoMedicacion + F"Codigo de medicamento: {Medicacion[i][5]}  Precio Unitario: {Medicacion[i][6]}  Cantidad: {Medicacion[i][7]}  Precio Final: {Medicacion[i][8]}\n"
        
        while TRUE:
            if int(Client[9]) > 1 and int(Client[9]) < 9999:
                Descuento = "3%"
                DescuentoInt = 3
                break
        
            if int(Client[9]) == 100000:
                Descuento = "5%"
                DescuentoInt = 5
                break

            if int(Client[9]) > 100000 and int(Client[9]) < 150000:
                Descuento = "10%"
                DescuentoInt = 10
                break

            else:
                Descuento = "0%"
                break

        informacion = (F"'DATOS DEL CLIENTE'\nCodigo de cliente: {codigo}\nNombre del cliente: {Client[1]}\nCodigo de mascota: {Pet[1]}\nNombre de mascota: {Pet[2]}\n\n'MEDICAMENTOS'\n{infoMedicacion}\nTotal: {Total}\nDescuento: {Descuento}\nPrecio Final: {int(((int(Total))-((int(Total))*(DescuentoInt/100))))}\n\n\n\n")

        try:
            archivo = open(F"Factura {codigo},{Client[1]}.txt", 'a',)
            archivo.write(f"{informacion}")  
            archivo.close()

        except FileNotFoundError:

            archivo = open(F"Factura {codigo},{Client[1]}", 'w')
            archivo.write(informacion)
            archivo.close()

        except Exception as e:

            print("Ocurrió un error:", str(e))

        ventanaGenerarFactura.mainloop()

def consultarSaldo():

    global ListaDeClientes
    global ListaDeMascotas
    global ListaDeTratamientos
    global ListaDeMedicacion

    ventanaconsultarSaldo = Tk()
    ventanaconsultarSaldo.title("Consultar Saldo")
    ventanaconsultarSaldo.geometry("300x150")

    consultarSaldoLabel = Label(ventanaconsultarSaldo,text="Ingrese el codigo de cliente que desea")
    consultarSaldoLabel.pack(padx=10,pady=8)
    consultarSaldoEntry = Entry(ventanaconsultarSaldo, width=200)
    consultarSaldoEntry.pack(pady=8,padx=10)

    consultarSaldoButton = Button(ventanaconsultarSaldo, text="Consultar Saldo", command=lambda:[ConsultarSaldoCliente(),ventanaconsultarSaldo.destroy()])
    consultarSaldoButton.pack(pady=8,padx=8)

    def ConsultarSaldoCliente():
    
        codigo = consultarSaldoEntry.get()

        if codigo not in codigosClientesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")

        else:
            for i in range(len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:
                    MessageBox.showinfo("Consultar Saldo",f"El saldo de {codigo},{ListaDeClientes[i][1]} es:\n {ListaDeClientes[i][10]}")
                    break

def consultarDescuento():

    global ListaDeClientes
    global ListaDeMascotas
    global ListaDeTratamientos
    global ListaDeMedicacion

    ventanaconsultarDescuento = Tk()
    ventanaconsultarDescuento.title("Consultar Descuento")
    ventanaconsultarDescuento.geometry("300x150")

    consultarDescuentoLabel = Label(ventanaconsultarDescuento,text="Ingrese el codigo de cliente que desea")
    consultarDescuentoLabel.pack(padx=10,pady=8)
    consultarDescuentoEntry = Entry(ventanaconsultarDescuento, width=200)
    consultarDescuentoEntry.pack(pady=8,padx=10)

    consultarDescuentoButton = Button(ventanaconsultarDescuento, text="Consultar Descuento", command=lambda:[ConsultarDescuentoCliente(),ventanaconsultarDescuento.destroy()])
    consultarDescuentoButton.pack(pady=8,padx=8)

    def ConsultarDescuentoCliente():
    
        codigo = consultarDescuentoEntry.get()

        if codigo not in codigosClientesValidos:
            MessageBox.showerror("Error","El codigo ingresado no existe")

        else:
            for i in range(len(ListaDeClientes)):

                if ListaDeClientes[i][0] == codigo:
                    MessageBox.showinfo("Consultar Descuento",f"El Descuento de {codigo},{ListaDeClientes[i][1]} es:\n {ListaDeClientes[i][9]}")
                    break

