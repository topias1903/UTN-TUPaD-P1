# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
### MAIN ###

num = int(input("Ingrese un numero: "))
for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
    
### MAIN ###

num = int(input("Ingresa una posicion de la serie de Fibonacci: "))

for i in range(num + 1):
    print(fibonacci(i))

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛
# (𝑚−1)
# . Prueba esta función en un
# algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)

### MAIN ###
base = int(input("Ingresa un numero: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

### MAIN ###

num = int(input("Ingresa un numero: "))

binario = decimal_a_binario(num)
print(f"El numero {num} en binario es {binario}")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
### main ###

numero = int(input("Ingresa un numero: "))

resultado = suma_digitos(numero)
print(f"La suma de los digitos de {numero} es {resultado}")

# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if (numero % 10) == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
### MAIN ###

num = int(input("Ingresa un numero: "))
dig = int(input("Ingresa el digito a buscar: "))

cantidad = contar_digito(num, dig)
print(f"El digito {dig} aparece {cantidad} veces.")



