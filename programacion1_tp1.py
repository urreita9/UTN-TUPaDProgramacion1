# Francisco Urrea
# DNI 34179266
# Programación 1
# Práctico 1: Estructuras secuenciales

# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo
# usando el nombre ingresado. Por ejemplo: si el usuario ingresa "Marcos", el programa debe
# imprimir por pantalla "Hola Marcos!". Consejo: esto será más sencillo si utilizas print(f…)
# para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario
# ingresa "Marcos", "Pérez", "30" y "Argentina", el programa debe imprimir "Soy Marcos Pérez,
# tengo 30 años y vivo en Argentina". Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarDeResidencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su
# área y su perímetro.
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
perimetro = 2*pi*radio
area = pi*(radio**2)
print(f"Area: {area}. Perimetro: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla
# a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese el primer número entero (distinto de 0): "))
numero2 = int(input("Ingrese el segundo número entero (distinto de 0): "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"\nResultados:")
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicacion: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su
# índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del
# siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"\nSu Índice de Masa Corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivale a {fahrenheit}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de {numero1}, {numero2} y {numero3} es: {promedio}")