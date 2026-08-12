print("*** Sistema Fuera De Rango ***")

Valor_Minimo = 0
Valor_Maximo = 5

# Solicitamos un valor entre 0 y 5

dato = int(input(f'Proporcione un valor entre {Valor_Minimo} y {Valor_Maximo}: '))

# Verificamos si el dato se encuentra dentro de rango
#esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO

esta_dentro_rango  = Valor_Minimo <= dato <= Valor_Maximo

print(f"valor esta dentro de rango? {esta_dentro_rango}")


