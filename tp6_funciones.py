# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: "Hola Mundo!". Llamar a esta función desde el
# programa principal.
def hola_mundo():
    print("Hola Mundo!")


hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.

# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: "Hola Marcos!". Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    return f"Hola {nombre}!"


print(saludar_usuario("Marcos"))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: "Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]". Pedir los datos al usuario y llamar a esta función con los valores ingresados.


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio)
# que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math


def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input("Ingrese el radio del círculo: "))
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.


def segundos_a_horas(segundos):
    return segundos / 3600


segundos = float(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los
# resultados de forma clara.


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la
# función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    return peso / (altura**2)


peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")
