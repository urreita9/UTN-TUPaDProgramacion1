# TP 6: Estructuras de Datos Complejas

# EJERCICIO 1: Añadir frutas al diccionario
print("=== EJERCICIO 1 ===")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# EJERCICIO 2: Actualizar precios
print("\n=== EJERCICIO 2 ===")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# EJERCICIO 3: Lista con solo las frutas
print("\n=== EJERCICIO 3 ===")
frutas = list(precios_frutas.keys())
print(frutas)

# EJERCICIO 4: Agenda telefónica
print("\n=== EJERCICIO 4 ===")
contactos = {}
for i in range(5):
    nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
    numero = input(f"Ingresa el número de {nombre}: ")
    contactos[nombre] = numero

nombre_buscar = input("\n¿Qué contacto deseas buscar? ")
if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
else:
    print(f"El contacto {nombre_buscar} no existe.")

# EJERCICIO 5: Análisis de palabras
print("\n=== EJERCICIO 5 ===")
frase = input("Ingresa una frase: ")
palabras = frase.lower().split()

# Palabras únicas usando set
palabras_unicas = set(palabras)
print(f"Palabras únicas: {palabras_unicas}")

# Diccionario con conteo de palabras
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print(f"Conteo de palabras: {conteo_palabras}")

# EJERCICIO 6: Promedio de notas de alumnos
print("\n=== EJERCICIO 6 ===")
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresa la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# EJERCICIO 7: Análisis de parciales con sets
print("\n=== EJERCICIO 7 ===")
aprobaron_p1 = {1, 2, 3, 4, 5}
aprobaron_p2 = {3, 4, 5, 6, 7}

ambos = aprobaron_p1 & aprobaron_p2
print(f"Aprobaron ambos parciales: {ambos}")

solo_uno = aprobaron_p1 ^ aprobaron_p2
print(f"Aprobaron solo uno: {solo_uno}")

al_menos_uno = aprobaron_p1 | aprobaron_p2
print(f"Aprobaron al menos uno: {al_menos_uno}")

# EJERCICIO 8: Gestión de stock
print("\n=== EJERCICIO 8 ===")
stock = {'Laptop': 5, 'Mouse': 20, 'Teclado': 15}

while True:
    print("\n1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        producto = input("Ingresa el nombre del producto: ")
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]}")
        else:
            print(f"El producto {producto} no existe.")
    
    elif opcion == '2':
        producto = input("Ingresa el nombre del producto: ")
        if producto in stock:
            unidades = int(input(f"¿Cuántas unidades deseas agregar? "))
            stock[producto] += unidades
            print(f"Nuevo stock de {producto}: {stock[producto]}")
        else:
            print(f"El producto {producto} no existe.")
    
    elif opcion == '3':
        producto = input("Ingresa el nombre del nuevo producto: ")
        cantidad = int(input("Ingresa la cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con stock: {cantidad}")
    
    elif opcion == '4':
        break
    
    print(f"Stock actual: {stock}")

# EJERCICIO 9: Agenda con tuplas de (día, hora)
print("\n=== EJERCICIO 9 ===")
agenda = {
    (1, 10): "Reunión con cliente",
    (1, 14): "Almuerzo",
    (2, 9): "Presentación",
    (3, 16): "Capacitación"
}

dia_buscar = int(input("¿Qué día? "))
hora_buscar = int(input("¿Qué hora? "))
clave = (dia_buscar, hora_buscar)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividad programada en ese horario.")

# EJERCICIO 10: Invertir diccionario país-capital
print("\n=== EJERCICIO 10 ===")
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario original (País -> Capital):")
print(paises_capitales)
print("\nDiccionario invertido (Capital -> País):")
print(capitales_paises)