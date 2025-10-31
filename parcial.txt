# Francisco Urrea
# DNI 34179266

# Primer Parcial – Programación 1
# Enunciado
# La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
# copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
# utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
# vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
# Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
# elija salir.
# Requisitos y Restricciones Técnicas
# • Estructuras Permitidas: Debes usar un bucle while para navegar por las opciones del
# menú hasta que el usuario elija salir. Se debe utilizar una estructura case (o su
# equivalente con if/elif/else) para el menú, así como estructuras condicionales y
# secuenciales de Python. Se permiten funciones para validar cadenas de texto como
# lower(), upper() o isdigit().
# • Estructuras Prohibidas: Está estrictamente prohibido usar excepciones, clases,
# diccionarios, funciones de creación propia y estructuras de datos avanzadas. Si se
# utilizan, la calificación máxima será de 10%.
# • Listas Paralelas: Las listas titulos[] y ejemplares[] deben estar sincronizadas, de modo
# que el título en un índice corresponda a la cantidad de copias en el mismo índice de la
# otra lista
# Ejemplo:
# • títulos[] = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
# • ejemplares[] = [5, 3, 7]
# En este ejemplo, "El Señor de los Anillos" tiene 5 copias, "Orgullo y Prejuicio" tiene 3 copias,
# y "Matar un Ruiseñor" tiene 7 copias.
# Requerimientos del Menú
# 1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la
# cantidad inicial.
# 2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título.
# 3. Mostrar catálogo → Muestra todos los libros y su stock actual.
# 4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares
# hay.
# 5. Listar agotados → Muestra los títulos que tienen 0 ejemplares.
# 6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al
# catálogo, respetando la sincronía de los índices en las listas.
# 7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un
# libro, elegido por el usuario, para registrar préstamos o devoluciones.
# - Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado,
# si hay unidades suficientes.
# - Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado.
# 8. Salir → Termina la ejecución del programa.
# Entregables
# El estudiante deberá subir el archivo del programa en lenguaje Python a la plataforma
# institucional. NO SUBIR UN REPOSITORIO DE GITHUB. SOLO SUBIR EL ARCHIVO.PY
# El código debe cumplir con:
# • Todas las funcionalidades solicitadas reflejadas en el menú.
# • Buena ejecución sin errores.
# • Nomenclatura clara en el nombre de las variables.
# • Legibilidad general y buenas prácticas de codificación.

titulos = []
ejemplares = []
prestados = []
programa = 1

MENU = """
===== BIBLIOTECA =====
1. Ingresar títulos
2. Ingresar ejemplares
3. Mostrar catálogo
4. Consultar disponibilidad
5. Listar agotados
6. Agregar título
7. Actualizar ejemplares (préstamo/devolución)
======================
8. Salir
"""
ERROR_REINTENTAR = "Debe ingresar un número del 1 al 8. Vuelva a intentar."
ERROR_NUMERO_MAYOR_IGUAL_CERO = "Debe ingresar un número mayor o igual a cero."
ERROR_NUMERO_MAYOR_IGUAL_CERO_MENU = (
    "Debe ingresar un número mayor o igual a cero. Volviendo al menú inicial."
)
ERROR_TITULO_EXISTENTE = "El título ingresado ya se encuentra en el listado."
ERROR_TITULO_NO_EXISTENTE = (
    "El título no se encuentra en el listado. Volviendo al menú inicial."
)
ERROR_TITULO_VACIO = "El título no puede estar vacío."
ERROR_TITULO_VACIO_MENU = "El título no puede estar vacío. Volviendo al menú inicial."
ERROR_TITULO_NO_PRESTADO = "El título no se encuentra prestado. Si desea agregar un título, seleccione la opción 6 del menú principal."

CANTIDAD_TITULOS_INICIALES = "Cantidad de títulos a ingresar: "
CANTIDAD_EJEMPLARES_A_INGRESAR = "Cantidad de ejemplares: "
BUSQUEDA_TITULO = "Ingrese el título que desea: "
INGRESAR_TITULO = "Ingrese el título: "
AGREGAR_TITULO = "Ingrese el título que desea agregar: "
PRESTAR_TITULO = "Ingrese el título que desea prestar: "
PRESTAMO_REALIZADO = "Prestamo realizado."
DEVOLUCION_REALIZADA = "Devolución registrada."
ACTUALIZAR_TITULO = "Ingrese el título que desea actualizar: "
DEVOLVER_TITULO = "Ingrese el título que desea devolver: "
RESET = "Esta opción hará un reset de la biblioteca. Presione 1 para continuar. Presione cualquier otra tecla para volver. "
BIBLIOTECA_RESETEADA = "Biblioteca: reset exitoso."
PRESTAMO_UNO = "Presione 1 para prestamo. "
DEVOLUCION_DOS = "Presione 2 para devolución. "
VOLVER_CUALQUIER_TECLA = "Presione Cualquier otra tecla para volver al menú inicial. "
VOLVER_MENU = "Volviendo al menú inicial."
CERO_EJEMPLARES = "Este título tiene cero ejemplares."
CATALOGO = "===== CATÁLOGO ====="


while programa == 1:

    opcion_elegida = input(MENU)

    if opcion_elegida.isdigit():
        num_menu = int(opcion_elegida)

        match num_menu:
            case 1:
                # Ingresar títulos
                if len(titulos) > 0:
                    reset = input(RESET)
                    if reset == "1":
                        titulos = []
                        ejemplares = []
                        prestados = []
                        print(BIBLIOTECA_RESETEADA)
                    else:
                        print(VOLVER_MENU)
                        continue  # Menú principal
                cantidad_titulos = input(CANTIDAD_TITULOS_INICIALES)
                if cantidad_titulos.isdigit():
                    numero_de_titulos = int(cantidad_titulos)
                    while numero_de_titulos > 0:
                        titulo = input(INGRESAR_TITULO).upper()
                        if titulo == "":
                            print(ERROR_TITULO_VACIO)
                            continue
                        if titulo in titulos:
                            print(ERROR_TITULO_EXISTENTE)
                            continue
                        cantidad = input(
                            f"Ingrese cantidad de ejemplares para '{titulo}': "
                        )
                        if cantidad.isdigit():
                            titulos.append(titulo)
                            ejemplares.append(int(cantidad))
                            numero_de_titulos -= 1
                        else:
                            print(ERROR_NUMERO_MAYOR_IGUAL_CERO)
                            continue

                    print(
                        f"""
                                Títulos: {titulos}
                                Ejemplares: {ejemplares} 
                                """
                    )
                else:
                    print(ERROR_NUMERO_MAYOR_IGUAL_CERO_MENU)
            case 2:
                # Ingresar ejemplares
                busqueda_titulo = input(BUSQUEDA_TITULO).upper()
                if busqueda_titulo not in titulos:
                    print(ERROR_TITULO_NO_EXISTENTE)
                    continue  # Menú principal
                ingreso_ejemplares = input(CANTIDAD_EJEMPLARES_A_INGRESAR)
                if ingreso_ejemplares.isdigit():
                    cant_ejemplares = int(ingreso_ejemplares)
                    if cant_ejemplares >= 0:
                        posicion_titulo = titulos.index(busqueda_titulo)
                        ejemplares[posicion_titulo] = cant_ejemplares
                        print(
                            f"""
                                    Títulos: {titulos}
                                    Ejemplares: {ejemplares} 
                                """
                        )
                else:
                    print(ERROR_NUMERO_MAYOR_IGUAL_CERO_MENU)
            case 3:
                # Mostrar catálogo
                print(
                    f"""
                            {CATALOGO}
                            Títulos: {titulos}
                            Ejemplares: {ejemplares} 
                        """
                )
            case 4:
                # Consultar disponibilidad
                busqueda_titulo = input(BUSQUEDA_TITULO).upper()
                if busqueda_titulo not in titulos:
                    print(ERROR_TITULO_NO_EXISTENTE)
                    continue  # Menú principal
                posicion_titulo = titulos.index(busqueda_titulo)
                cant_ejemplares = ejemplares[posicion_titulo]
                print(
                    f"""
                          Título: {busqueda_titulo} 
                          Ejemplares: {cant_ejemplares}
                        """
                )
            case 5:
                # Listar agotados
                agotados = []
                for i in range(len(ejemplares)):
                    if ejemplares[i] == 0:
                        agotados.append(titulos[i])
                print(
                    f"""
                          Títulos Agotados: {agotados}
                        """
                )
            case 6:
                # Agregar título
                titulo = input(AGREGAR_TITULO).upper()
                if titulo == "":
                    print(ERROR_TITULO_VACIO_MENU)
                    continue  # Menú principal
                if titulo in titulos:
                    print(ERROR_TITULO_EXISTENTE)
                    continue  # Menú principal
                cantidad = input(f"Ingrese cantidad de ejemplares para '{titulo}': ")
                if cantidad.isdigit():
                    titulos.append(titulo)
                    ejemplares.append(int(cantidad))
                else:
                    print(ERROR_NUMERO_MAYOR_IGUAL_CERO_MENU)
                    continue  # Menú principal
                print(
                    f"""
                            Títulos: {titulos}
                            Ejemplares: {ejemplares} 
                        """
                )
            case 7:
                # Actualizar ejemplares (préstamo/devolución)
                titulo = input(ACTUALIZAR_TITULO).upper()
                if titulo not in titulos:
                    print(ERROR_TITULO_NO_EXISTENTE)
                    continue  # Menú principal
                posicion_titulo = titulos.index(titulo)
                prestamo = "1"
                devolucion = "2"
                seleccion = input(
                    f"{PRESTAMO_UNO}\n{DEVOLUCION_DOS}\n{VOLVER_CUALQUIER_TECLA}"
                )
                if seleccion == prestamo:
                    if ejemplares[posicion_titulo] == 0:
                        print(CERO_EJEMPLARES)
                        continue  # Menú principal
                    prestados.append(titulo)
                    ejemplares[posicion_titulo] -= 1
                    print(
                        f"""
                            {PRESTAMO_REALIZADO}
                            Título: {titulo}
                            Ejemplares: {ejemplares[posicion_titulo]} 
                        """
                    )

                elif seleccion == devolucion:
                    if titulo not in prestados:
                        print(ERROR_TITULO_NO_PRESTADO)
                        continue  # Menú principal
                    ejemplares[posicion_titulo] += 1
                    prestados.remove(titulo)
                    print(
                        f"""
                            {DEVOLUCION_REALIZADA}
                            Título: {titulo}
                            Ejemplares: {ejemplares[posicion_titulo]} 
                        """
                    )

                else:
                    print(VOLVER_MENU)
                    continue  # Menú principal
            case 8:
                print("Saliendo.")
                programa = 0
            case _:
                print(ERROR_REINTENTAR)
    else:
        print(ERROR_REINTENTAR)
