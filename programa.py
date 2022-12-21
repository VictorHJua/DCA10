def suma(n1, n2):
    print(f"Resultado: ", (int(n1) + int(n2)) )

def resta(n1, n2):
    print(f"Resultado: ", (int(n1) - int(n2)) )


print("¿Que operación quiere realizar?\n1. Suma\n2. Resta")
opcion = input()
operacion = ""
if opcion == "1": 
    operacion = "suma"
else:
     operacion = "resta"
print(f"Introduzca dos numeros para la operación de " + operacion + ".")
x = input()
y = input()

if opcion == "1": 
    suma(x, y)
else:
    resta(x, y)
