# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7, 4, 5, 10, 8, 3, 6, 7, 8,5]

print(f"Notas: {notas}")

total= 0
promedio = 0
nota_min = notas[0]
nota_max = notas[0]

for nota in notas:
    if(nota < nota_min):
        nota_min = nota
    elif(nota > nota_max):
        nota_max = nota
    total += nota

promedio = total / len(notas)

print(f"Promedio: {promedio}")
print(f"Nota más baja: {nota_min}. Nota más alta: {nota_max}")
    


# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    productos.append(input("Agregue un producto a la lista: ")) 

print(f"Lista de productos ordenada alfabéticamente: {sorted(productos)}")

producto_a_eliminar = input("Qué producto desea eliminar?: ")

if(producto_a_eliminar in productos):
    productos.remove(producto_a_eliminar)
    print(f"Producto {producto_a_eliminar} eliminado. Listado actualizado: {sorted(productos)}")
else:
    print(f"{producto_a_eliminar} no esta en el listado de productos.")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = []
pares = []
impares = []

for i in range(15):
   numero_aleatorio = random.randint(1,100)
   numeros.append(numero_aleatorio)
   if(numero_aleatorio % 2 == 0):
       pares.append(numero_aleatorio)
   else:
       impares.append(numero_aleatorio)

print(f"Números pares: {pares}: {len(pares)} números. Números impares: {impares}: {len(impares)} números")


# 4) Dada una lista con valores repetidos
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

lista_numeros = [1,5,3,4,1,3,10,11]
numeros_unicos = []

for numero in lista_numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

print(f"Lista sin elementos repetidos: {numeros_unicos}")




# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ['Ana', "Juana", "Santiago", "Pedro", "Pablo", "Maria", "Francisco", "Verónica"]

input_user = int(input("Desea Agregar (1) o Eliminar (2) un estudiante?: "))

if input_user == 1:
    estudiante = input("Nombre del estudiante que desea agregar: ")
    estudiantes.append(estudiante)
    print(f"Estudiante agregado. Lista actualizada: {estudiantes}")

elif input_user == 0:
    estudiante = input("Nombre del estudiante que desea eliminar: ")
    if(estudiante in estudiantes):
        estudiantes.remove(estudiante)
        print(f"Estudiante eliminado. Lista actualizada: {estudiantes}")
    else:
        print("El estudiante no se encuentra en la lista. Fin.")

else:
    print("Opción invalida. Fin.")

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

lista_numeros_a_rotar = [0,1,2,3,4,5,6]
ultimo = lista_numeros_a_rotar.pop()
lista_numeros_a_rotar.insert(0, ultimo) 

print(f"Lista de números: {lista_numeros_a_rotar}")

# # 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# # semana.
# # • Calcular el promedio de las mínimas y el de las máximas.
# # • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 20],  
    [10, 18],  
    [14, 22],  
    [11, 21],  
    [13, 26],  
    [15, 24],  
    [9, 19]    
]

suma_minimas = 0
suma_maximas = 0
amplitud_termica_max = 0

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    amplitud_termica = maxima - minima

    if amplitud_termica > amplitud_termica_max:
        amplitud_termica_max = amplitud_termica
    
    suma_minimas += minima
    suma_maximas += maxima

promedio_minimas = suma_minimas/len(temperaturas)
promedio_maximas = suma_maximas/len(temperaturas)

print(f"Promedio mínimas: {promedio_minimas}. Promedio máximas: {promedio_maximas}")
print(f"Amplitud térmica máxima: {amplitud_termica_max}")


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6], 
    [5, 6, 7], 
    [9, 8, 10],
    [6, 7, 5], 
    [8, 9, 7]  
]

estudiantes_suma = []
materias_suma = [0,0,0]

suma_notas = 0
cant_materias = 3

for i in range(len(notas)):
    for k in range(len(notas[i])):
        suma_notas += notas[i][k]
        materias_suma[k] += notas[i][k]

    estudiantes_suma.append(suma_notas)
    suma = 0

for i in range(len(estudiantes_suma)):
    print(f"Promedio estudiante {i + 1}: {estudiantes_suma[i] / cant_materias}")

for i in range(len(materias_suma)):
    print(f"Promedio materia {i + 1}: {materias_suma[i] / len(notas)}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

juego = 1

while juego == 1:
    jugador_1_ok = 1
    jugador_2_ok = 1
    if "-" not in tablero[0] and "-" not in tablero[1] and "-" not in tablero[2]:
        print("Juego terminado.")
        juego = 0
        break
    while jugador_1_ok:
        jugador_1_fila = int(input("Jugador 1: Ingrese fila "))
        jugador_1_col = int(input("Jugador 1: Ingrese columna "))
        if tablero[jugador_1_fila][jugador_1_col] == "-":
            tablero[jugador_1_fila][jugador_1_col] = "X"
            for fila in tablero:
                print(" ".join(fila))
            jugador_1_ok = 0
        else: 
            print("Posición ocupada, elija otra.")
    if "-" not in tablero[0] and "-" not in tablero[1] and "-" not in tablero[2]:
        print("Juego terminado.")
        juego =0
        break
    while jugador_2_ok:
        jugador_2_fila = int(input("Jugador 2: Ingrese fila "))
        jugador_2_col = int(input("Jugador 2: Ingrese columna "))
        if tablero[jugador_2_fila][jugador_2_col] == "-":
            tablero[jugador_2_fila][jugador_2_col] = "O"
            for fila in tablero:
                print(" ".join(fila))
            jugador_2_ok = 0
        else: 
            print("Posición ocupada, elija otra.")

   

for fila in tablero:
    print(" ".join(fila))

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 12, 8, 15, 9, 11, 14],  
    [20, 18, 22, 25, 19, 21, 24],
    [5, 7, 6, 8, 5, 7, 6],       
    [30, 28, 32, 35, 31, 29, 33] 
]

productos_vendidos = []
ventas_dia = []
index_dia_max = 0
cant_dia_max = 0
producto_mas_vendido = 0

for i in range(len(ventas)):
    productos_vendidos.append(0)
    for k in range(len(ventas[i])):
        productos_vendidos[i] += ventas[i][k]
        if len(ventas_dia) == k:
            ventas_dia.append(ventas[i][k])
        else:
            ventas_dia[k] += ventas[i][k]

print(ventas_dia)
            
for i in range(len(ventas_dia)):
    if ventas_dia[i] > cant_dia_max:
        cant_dia_max = ventas_dia[i]
        index_dia_max = i

for i in range(len(productos_vendidos)):
    if productos_vendidos[i] > producto_mas_vendido:
        producto_mas_vendido = i

print(f"Total de productos vendidos: {productos_vendidos}")
print(f"Día con mayores ventas totales: Día {index_dia_max + 1}. Ventas: {cant_dia_max}")
print(f"Producto mas vendido: prod nro {producto_mas_vendido + 1}")