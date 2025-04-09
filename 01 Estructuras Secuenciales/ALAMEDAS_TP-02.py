#Ejercicio 1
#Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

#Ejercicio 2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * radio * radio
perimetro = 2 * 3.14 * radio
print(f"El area del circulo es de {area} y el perimetro es de {perimetro}")

#Ejercicio 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 60
print(f"{segundos} segundos equivalen a {horas} hora/s")

#Ejercicio 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un numero para obtener su tabla: "))

print(f"""{numero} x 1 = {numero * 1}
{numero} x 2 = {numero * 2}
{numero} x 3 = {numero * 3}
{numero} x 4 = {numero * 4}
{numero} x 5 = {numero * 5}
{numero} x 6 = {numero * 6}
{numero} x 7 = {numero * 7}
{numero} x 8 = {numero * 8}
{numero} x 9 = {numero * 9}
{numero} x 10 = {numero * 10}""")

#Ejercicio 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

nro1 = int(input("Ingrese un numero distinto al 0: "))
nro2 = int(input("Ingrese otro numero distinto al 0: "))

print(f"""{nro1} + {nro2} = {nro1 + nro2}
{nro1} - {nro2} = {nro1 - nro2}
{nro1} / {nro2} = {nro1 // nro2}
{nro1} * {nro2} = {nro1 * nro2}""")

#Ejercicio 8
#  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

altura = float(input("Ingrese su altura en metros: "))
peso = int(input("Ingrese su peso en KG: "))

IMC = peso // altura**2

print(f"Su indice de masa corporal es de: {IMC}")

#Ejercicio 9
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia

Celcius = float(input("Ingrese una temperatura en Celcius: "))
Farenheit = 9 / 5 * Celcius + 32
print(f"La temperatura en Farenheit es de: {Farenheit}")

#Ejercicio 10
#  Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

nro1 = int(input("Ingrese el primer numero: "))
nro2 = int(input("Ingrese el segundo numero: "))
nro3 = int(input("Ingrese el tercer numero: "))

promedio = (nro1 + nro2 + nro3) // 3
print(f"El promedio de los 3 numero es de {promedio}")