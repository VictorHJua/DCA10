def suma(n1, n2):
    print(f"Resultado: ", (int(n1) + int(n2)) )

def resta(n1, n2):
    print(f"Resultado: ", (int(n1) - int(n2)) )


print("¿Que operación quiere realizar?\n1. Suma\n2. Resta")
operacion = ""
opcion = ""
while opcion!= "1" and opcion!="2":
    opcion = input()
    if opcion!= "1" and opcion!="2":
        print("Elige una opción válida\n1. Suma\n2. Resta")
if opcion == "1": 
    operacion = "suma"
else:
     operacion = "resta"
print(f"Introduzca dos numeros para la operación de " + operacion + ".")

errorNum = False
try:
    x = int(input())
    y = int(input())
except:
    errorNum = True
while errorNum == True:
    errorNum = False
    print("No se permiten caracteres que no sean números\nIntroduzca dos numeros para la " + operacion + ".")
    try:
        x = int(input())
        y = int(input())
    except:
        errorNum = True


if opcion == "1": 
    suma(x, y)
if opcion == "2": 
    resta(x, y)

