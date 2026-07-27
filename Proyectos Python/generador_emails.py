print("************* Generador de Emails *************")

nombre = input ("Cual es tu nombre?")
apellido = input ("Cuales son tus apellidos?")
empresa = input("Nombre De Tu Empresa? ")
extension_dominio = input("Extension Del Dominio De Tu Empresa? ")


#Normalizamos los valores recibidos
nombre = nombre.strip().lower().replace(" ",".")
apellido = apellido.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ", "")
extension_dominio = extension_dominio.strip().lower().replace(" ", "")


# Generar el email
email = f"{nombre}.{apellido}@{empresa}{extension_dominio}"


print(f"""
Tu nuevo email generado por el sistema es:
   {email}
   Felicidades¡¡""")



print("********** Generador de Emails2 **********")

nombree = input("Cual es tu nombre?")
apellidoo = input("Cuales son tus apellidos?")
empresaa = input("Nombre de tu empresa?")
extension_dominioo = input("Extension Del Dominio De Tu Empresa?")


nombree = nombree.strip().lower().replace(" ",".")
apellidoo = apellidoo.strip().lower().replace(" ", "")
empresaa = empresaa.strip().lower().replace(" ", "")
extension_dominioo = extension_dominioo.strip().lower().replace(" ",".")

email2 = f"{nombree}{apellidoo}@{empresaa}{extension_dominioo}"

print(f"""
Tu nuevo email generado por el sistema es:
{email2}
Felicidades¡¡¡""")

