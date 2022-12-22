def elegirOperacion():
    print("¿Que operación quiere realizar?\n0. Salir\n1. Suma\n2. Resta\n3. Multiplicación\n4. División")
    operacion = ""
    opcion = -1
    while opcion < 0 or opcion > 4:
        try:
            opcion = int(input())
        except:
            opcion = -1
        if opcion < 0 or opcion > 4:
            print("Elige una opción válida\n0. Salir\n1. Suma\n2. Resta\n3. Multiplicación\n4. División")
    if opcion == 0:
        exit(0)
    if opcion == 1: 
        operacion = "suma"
    if opcion == 2: 
        operacion = "resta"
    if opcion == 3: 
        operacion = "multiplicación"
    if opcion == 4: 
        operacion = "división"
    return opcion, operacion

def suma(n1, n2):
    print(f"Resultado: ", (int(n1) + int(n2)) )

def resta(n1, n2):
    print(f"Resultado: ", (int(n1) - int(n2)) )

def mult(n1, n2):
    print(f"Resultado: ", (int(n2) * int(n2)) )

def div(n1, n2):
    num = 0
    error = False
    try:
        num = (int(n1) / int(n2))
    except:
        error = True
        print(f"Error Cálculo: No es posible dividir entre 0")
    if not error: print(f"Resultado: ", num )


opcion,operacion = elegirOperacion()
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
if opcion == 4:
    div(x,y)


