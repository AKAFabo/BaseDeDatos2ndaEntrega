Todas las listas llevan el siguiente formato

cityList = [CodigoPais, CodigoCiudad, NombreCiudad] En esta lista se valida que CodigoPais sea valido, si las ciudades de un mismo CodigoPais se repiten se descarta la segunda aparicion

clientList = [NumCliente, Nombre, Direccion, CodigoPais, CodigoCiudad, Telefono, FechaUltimaVisita, Descuento,saldo] NumCliente no se puede repetir, si pasa se descarta la segunda aparicion

petList = [NumCliente, IDAnimal, Nombre, Tipo, Raza, FechaNacimiento, Sexo, Color, Castrado] Si NumCliente no existe no se carga la mascota y se pasa a la siguiente

medList = [IDAnimal, CodMedicacion, FechaUltimaVisita, Medicamentos, CostoUnitario, Cantidad, CostoTotal] No pueden existir medicaciones repetidas para una misma mascota para una misma fecha

countryList = [CodigoPais, Nombre] No pueden haber codigos repetidos

treatList = [CodTratamiento, Nombre, Precio, Cantidad] No pueden existir CodTratamiento repetidos

visitList = [CodVisita, IDAnimal, FechaUltimaVisita, TotalFactura, FormaDePago, ]

TODAS LAS ENTRADAS QUE TIENEN NUMERO PONERLAS COMO ENTEROS, DE LO CONTRARIO EL PROGRAMA PUEDE PARAR INESPERADAMENTE