# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0, 101, 1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = (input("Ingrese un numero entero: "))

contador = 0
for i in range(len(numero)):
    contador +=1
print(contador)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero_uno = int(input("Ingrese el primer valor: "))
numero_dos = int(input("Ingrese el segundo valor: "))

suma = 0

if numero_uno > numero_dos:
    for i in range(numero_dos + 1, numero_uno):
        suma += i
else:
    for i in range(numero_uno + 1, numero_dos):
        suma += i

print("La suma es:", suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
bandera = True

while bandera == True:
    numero = int(input("Ingrese un numero (0 para terminar bucle): "))
    if numero == 0:
        bandera = False
    else:
        suma += numero

print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_correcto = 5
intentos = 0
numero_usuario = 0

while numero_usuario != numero_correcto:
    numero_usuario = int(input("Adivine el numero entr el 0 y el 9: "))
    intentos += 1
    
print(f"Intentos necesarios para divinar el numero: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma += i

print("La suma es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

contador = 0
contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

while contador < 100:
    numero = int(input(f"Ingrese un numero, faltan {100-contador}: "))
    if numero >= 0 and numero % 2 == 0:
        contador_pares += 1
        contador_positivos += 1
    elif numero >= 0 and numero % 2 != 0:
        contador_impares += 1
        contador_positivos += 1
    elif numero < 0 and numero % 2 == 0:
        contador_pares += 1
        contador_negativos += 1
    else:
        contador_impares += 1
        contador_negativos += 1

    contador += 1

print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0

while contador < 100:
    numero = int(input(f"Ingrese un numero, faltan {100-contador}: "))
    suma += numero
    contador += 1

media = suma / contador 
print(f"La media es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ") 
numero_invertido = ""

for i in range(len(numero) - 1, -1, -1):
    numero_invertido += numero[i]

print(f"Numero invertido: {numero_invertido}")

