


def elegirOperacion():
    print("¿Que operación quiere realizar?\n0. Salir\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Libre")
    operacion = ""
    opcion = -1
    while opcion < 0 or opcion > 5:
        try:
            opcion = int(input())
        except:
            opcion = -1
        if opcion < 0 or opcion > 5:
            print("Elige una opción válida\n0. Salir\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\5. Libre")
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
    if opcion == 5: 
        operacion = "libre"
    return opcion, operacion

def suma(n1, n2):
    print(f"Resultado: ", (float(n1) + float(n2)) )

def resta(n1, n2):
    print(f"Resultado: ", (float(n1) - float(n2)) )

def mult(n1, n2):
    print(f"Resultado: ", (float(n2) * float(n2)) )

def div(n1, n2):
    num = 0
    error = False
    try:
        num = (float(n1) / float(n2))
    except:
        error = True
        print(f"Error Cálculo: No es posible dividir entre 0")
    if not error: print(f"Resultado: ", num )

def libre():
    print("En el modo libre puedes escribir los cuatro tipos de operaciones y darle al enter para obtener la respuesta.\nLos simbolos desponibles son '+', '-', '*', '/' y '%' \nPara salir escriba 'exit'.")
    salir = False
    while salir == False:
        try:
            respuesta = input()
            if respuesta == "exit" or respuesta == "Exit" or respuesta == "salir" or respuesta == "Salir":
                break
            print(eval(respuesta))
        except:
            print("Error Sintaxis")
    return

#MAIN
while True:
    opcion,operacion = elegirOperacion()
    if opcion!=5: 
        print(f"Introduzca dos numeros para la operación de " + operacion + ".")
        errorNum = False
        try:
            x = float(input())
            y = float(input())
        except:
            errorNum = True
        while errorNum == True:
            errorNum = False
            print("No se permiten caracteres que no sean números\nIntroduzca dos numeros para la " + operacion + ".")
            try:
                x = float(input())
                y = float(input())
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
    if opcion == 5:
        libre()


