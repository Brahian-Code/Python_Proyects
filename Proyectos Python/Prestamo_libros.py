print("*** Sistema De Prestamos De Libros ***")


DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input("Cuentas con la credencial de estudiantes (si/no): ")
distancia_biblioteca_km =int(input(f"A cuantos km vives de la biblioteca? "))

es_elegible_prestamo = (tiene_credencial.strip().lower() == "si"
                         or  distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)
print(f"Eres elegible para el prestamo de libros? {es_elegible_prestamo}")





