from Validaciones.validacionCiudades import validacionCiudades

listaValida = validacionCiudades()
gruposValidos = set()

def gruposValidados():

    for sublista in listaValida:

        gruposValidos.add(tuple(sublista[:2]))

    return gruposValidos