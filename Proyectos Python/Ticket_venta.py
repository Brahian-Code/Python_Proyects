print("*** Generacion Ticket De Venta ***")

precio_leche = float(input("Precio de Leche: "))
precio_pan = float(input("Precio de Pan: "))
precio_lechuga = float(input("Precio de Lechuga: "))
precio_platanos = float(input("Precio de Platanos: "))
descuento_vip = int(input(f"Desea aplicar algun descuento (%)?  "))
# Cálculo del subtotal (sin impuestos)

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * descuento_vip/100

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo con impuestos (16%)

impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)

costo_total_compra_final= subtotal + impuesto - descuento
descuento = costo_total_compra_final * descuento_vip/100
total_final = costo_total_compra_final - descuento

print(f"""
subtotal = ${subtotal_con_descuento:.2f}
impuesto (16%)= ${impuesto:.2f}
subtotal con descuentpo = ${subtotal_con_descuento}
descuento = ${descuento} ({descuento_vip:.2f})
Costo total de la compra = ${costo_total_compra_final:.2f}""")
