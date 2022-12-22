def suma(n1, n2):
    print(f"Resultado: ", (int(n1) + int(n2)) )

def resta(n1, n2):
    print(f"Resultado: ", (int(n1) - int(n2)) )

def mult(n1, n2):
    print(f"Resultado: ", (int(n2) * int(n2)) )


print("¿Que operación quiere realizar?\n1. Suma\n2. Resta\n3. Multiplicación")
operacion = ""
opcion = 0
while opcion < 1 or opcion > 3:
    try:
        opcion = int(input())
    except:
        opcion = 0
    if opcion < 1 or opcion > 3:
        print("Elige una opción válida\n1. Suma\n2. Resta\n3. Multiplicación")
if opcion == 1: 
    operacion = "suma"
if opcion == 2: 
    operacion = "resta"
if opcion == 3: 
    operacion = "multiplicación"
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


if opcion == 1: 
    suma(x, y)
if opcion == 2: 
    resta(x, y)
if opcion == 3:
    mult(x,y)


