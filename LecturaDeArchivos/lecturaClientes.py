
def leerClientes():

    with open("Clientes.txt", "r") as listaClientes:
        lineas = listaClientes.readlines()

    lista_clientes = [linea.strip() for linea in lineas if linea.strip()]
    clientList = [terminos.split(";") for terminos in lista_clientes]

    return clientList



