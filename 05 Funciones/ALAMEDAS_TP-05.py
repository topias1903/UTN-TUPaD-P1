# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Definir funcion
def imprimir_hola_mundo():
    return "Hola mundo"

# Main
mensaje = imprimir_hola_mundo()
print(mensaje)

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario

#Definir funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}"

#Main
nombre = input("Ingrese su nombre: ")
mensaje = saludar_usuario(nombre)
print(mensaje)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

def calcular_area_circulo(radio):
    area = 3.14 * (radio * radio)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

##### Main ####

radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area} y el perimetro es {perimetro}.")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas

### main ###

segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos_a_horas(segundos)
print(f"{segundos} Segundo/s equivalen a {horas} hora/s")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    contador = 1
    tabla = ""

    while contador <= 10:
        resultado = numero * contador
        tabla += f"La tabla del {contador} del numero {numero} = {resultado}\n"
        contador += 1

    return tabla

# Main
num = int(input("Ingrese un número: "))
print(tabla_multiplicar(num))

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    return (suma, resta, multiplicacion, division)

###main###

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

resultado = operaciones_basicas(a, b)

print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[0]}")
print(f"Multiplicacion: {resultado[0]}")
print(f"Division: {resultado[0]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

### main ###

peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su indice de masa corporal es: {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

### main ###

celsius = float(input("Ingrese una temperatura en Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(F"{celsius} grados celsius son {fahrenheit} grados fahrenheit")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

### main ###

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

promedio = calcular_promedio(a, b, c)
print(F"El promedio entre {a}, {b} y {c} es de: {promedio}")
