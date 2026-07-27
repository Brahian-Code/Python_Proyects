from random import randint

print("******** Sistema Generador de id Unico ********")

nombre = input("Cual es tu nombre? ")
apellido = input("Cual es su apellido? ")
anio_nacimiento = input("Cual es su año de nacimiento (YYYY)?") # Years

#Normalizar valores
nombre = nombre.strip().upper()[0:2]
apellido = apellido.strip().upper()[0:2]
anio_nacimiento = anio_nacimiento.strip()[2:4]

# Generar el valor aleatorio
aleatorio = randint(1000,9999)

# Generamos el valor de id unico
Id_unico = f"{nombre}{apellido}{anio_nacimiento}{aleatorio}"
print(f"""\nHola {nombre},
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {Id_unico}
    Felicidades¡""")



from random import randint

print("********** Sistema Generador de id Unico2 ********")
nombree = input("Cual es tu nombre? ")
apellidoo = input("Cual es su apellido? ")
anio_nacimientoo = input("cual es tu año de nacimiento (YYYY)? ")


nombree = nombree.strip().upper()[0:4]
apellidoo= apellidoo.strip().upper()[0:4]
anio_nacimientoo = anio_nacimientoo.strip()[0:4]

aleatorio = randint(1000,9999)

Id_unicoo = f"{nombree}{apellidoo}{anio_nacimientoo}{aleatorio}"
print(f"""\nHola {nombree},
          Tu nuevo numero de identificacion (ID) Generado por el sistema es:
        {Id_unicoo} 
         Felicidades¡¡¡""")






from random import randint
print("********** Sistema Generador de id Unico3 ********")


nombre3 = input("Cual es tu nombre?")
apellido3 = input ("Cual es tu apellido?")
anio_nacimiento3 = input ("Cual es tu año de nacimiento (YYYY)?")

nombre3 = nombre3.strip().upper()[0:6]
apellido3 = apellido3.strip().upper()[0:3]
anio_naciomiento3 = anio_nacimiento3.strip()[0:3]

aleatorio3 = randint(2000,9999)


Id_unico3 = f"{nombre3}{apellido3}{anio_nacimiento3}{aleatorio3}"

print(f"""\nHola {nombre3},
Tu nuevo numero de identificacion (ID) Generado por el sistema es:
{Id_unico3} 
Felicidades¡¡""")