print("*** Sistema De Descuentos Vip ***")

NM_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Cuantos productos compraste hoy?" ))
tiene_membresia = input("Tienes membresía de la tienda (si/no): ")

es_elegible_descuento = (cantidad_productos >= NM_PRODUCTOS_DESCUENTO
                         and tiene_membresia.strip().lower() == "si")

print(f"Tienes acceso al descuento VIP? {es_elegible_descuento}")


