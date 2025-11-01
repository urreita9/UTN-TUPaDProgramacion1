
def cargar_productos(nombre_archivo):
    """Lee el archivo y retorna una lista de diccionarios con los productos."""
    productos = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                partes = linea.split(',')
                producto = {
                    'nombre': partes[0],
                    'precio': float(partes[1]),
                    'cantidad': int(partes[2])
                }
                productos.append(producto)
    return productos


def mostrar_productos(productos):
    """Muestra los productos en formato legible."""
    print("\n--- PRODUCTOS ---")
    for producto in productos:
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print()


def agregar_producto(productos):
    """Pide un nuevo producto al usuario y lo agrega a la lista."""
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print("Producto agregado.\n")


def buscar_producto(productos):
    """Busca un producto por nombre y muestra sus datos."""
    print("\n--- BUSCAR PRODUCTO ---")
    nombre_buscar = input("Nombre a buscar: ")
    
    encontrado = False
    for producto in productos:
        if producto['nombre'] == nombre_buscar:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.\n")


def guardar_productos(nombre_archivo, productos):
    """Sobrescribe el archivo con los productos actualizados."""
    with open(nombre_archivo, 'w') as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Productos guardados.\n")


def menu():
    """Menú principal del programa."""
    nombre_archivo = "productos.txt"
    
    # Crear archivo inicial
    with open(nombre_archivo, 'w') as archivo_inicial:
        archivo_inicial.write("Lapicera,120.5,30\n")
        archivo_inicial.write("Cuaderno,85.0,50\n")
        archivo_inicial.write("Borrador,15.75,100\n")
    
    productos = cargar_productos(nombre_archivo)
    
    while True:
        print("=== GESTOR DE PRODUCTOS ===")
        print("1. Mostrar productos")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Guardar cambios")
        print("5. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            mostrar_productos(productos)
        elif opcion == '2':
            agregar_producto(productos)
        elif opcion == '3':
            buscar_producto(productos)
        elif opcion == '4':
            guardar_productos(nombre_archivo, productos)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.\n")


menu()