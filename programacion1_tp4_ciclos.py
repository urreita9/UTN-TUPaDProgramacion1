# Actividades
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 100 + 1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))

cantidad_digitos = len(str(numero))

print(f"El número tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
max = 0
min = 0
suma = 0

if(num1 >= num2):
    max = num1
    min = num2
else:
    max = num2
    min = num1

for i in range(min + 1, max):
    suma += i

print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = 1

suma = 0

while numero != 0:
    numero = int(input("Ingrese un número: "))
    suma += numero

print(f"Suma: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0, 9)

intentos = 0

while True:
    num_usuario = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if(num_usuario == num_aleatorio):
        break

print(f"Intentos: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

suma = 0

num = int(input("Ingresa un número entero positivo: "))

if(num > 0):
    for i in range(num):
        suma += i
    print(f"Suma: {suma}")
else:
   print("El numero debe ser positivo")                         

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0
cantidad = 100

for i in range(cantidad):
    num = int(input(f"Ingrese un número entero ({i + 1}/{cantidad}): "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0
cantidad = 100
media = 0

for i in range(cantidad):
    num = int(input(f"Ingrese un número entero ({i + 1}/{cantidad}): "))
    suma += num

media = suma / cantidad

print(f"Media: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero > 0:
    ultimo_digito = numero % 10 
    numero_invertido = numero_invertido * 10 + ultimo_digito
    numero = numero // 10 

print(f"Número invertido: {numero_invertido}")