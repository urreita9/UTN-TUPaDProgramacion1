# EJERCICIO 1: Factorial


def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def ejercicio_1():
    print("\n=== EJERCICIO 1: FACTORIAL ===")
    num = int(input("Ingresa un número: "))

    if num < 0:
        print("El número debe ser positivo.")
        return

    print(f"\nFactoriales del 1 al {num}:")
    for i in range(1, num + 1):
        print(f"Factorial de {i} = {factorial(i)}")


# EJERCICIO 2: Fibonacci


def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def ejercicio_2():
    print("\n=== EJERCICIO 2: SERIE DE FIBONACCI ===")
    pos = int(input("Ingresa la posición hasta la que quieres ver Fibonacci: "))

    if pos < 0:
        print("La posición debe ser un número positivo.")
        return

    print(f"\nSerie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(f"Posición {i}: {fibonacci(i)}")


# EJERCICIO 3: Potencia


def potencia(n, m):
    """Calcula n elevado a m recursivamente: n^m = n * n^(m-1)"""
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * potencia(n, m - 1)


def ejercicio_3():
    print("\n=== EJERCICIO 3: POTENCIA ===")
    base = int(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente: "))

    if exponente < 0:
        print("El exponente debe ser un número no negativo.")
        return

    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")


# EJERCICIO 4: Decimal a Binario


def decimal_a_binario(n):
    """Convierte un número decimal a binario de forma recursiva."""
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


def ejercicio_4():
    print("\n=== EJERCICIO 4: DECIMAL A BINARIO ===")
    num = int(input("Ingresa un número decimal: "))

    if num < 0:
        print("El número debe ser positivo.")
        return

    if num == 0:
        binario = "0"
    else:
        binario = decimal_a_binario(num)

    print(f"El número {num} en binario es: {binario}")


# EJERCICIO 5: Palíndromo


def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo de forma recursiva."""
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False


def ejercicio_5():
    print("\n=== EJERCICIO 5: PALÍNDROMO ===")
    palabra = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

    if es_palindromo(palabra):
        print(f"'{palabra}' ES un palíndromo.")
    else:
        print(f"'{palabra}' NO es un palíndromo.")


# EJERCICIO 6: Suma de Dígitos


def suma_digitos(n):
    """Suma recursivamente todos los dígitos de un número."""
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)


def ejercicio_6():
    print("\n=== EJERCICIO 6: SUMA DE DÍGITOS ===")
    num = int(input("Ingresa un número positivo: "))

    if num < 0:
        print("El número debe ser positivo.")
        return

    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es: {resultado}")


# EJERCICIO 7: Contar Bloques (Pirámide)


def contar_bloques(n):
    """Calcula el total de bloques en una pirámide de forma recursiva."""
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


def ejercicio_7():
    print("\n=== EJERCICIO 7: CONTAR BLOQUES ===")
    num = int(input("Ingresa el número de bloques en el nivel más bajo: "))

    if num < 1:
        print("El número debe ser al menos 1.")
        return

    resultado = contar_bloques(num)
    print(f"Para una pirámide con {num} bloques en la base:")
    print(f"Total de bloques necesarios: {resultado}")


# EJERCICIO 8: Contar Dígito


def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número de forma recursiva."""
    if numero == 0:
        return 0
    else:
        if (numero % 10) == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


def ejercicio_8():
    print("\n=== EJERCICIO 8: CONTAR DÍGITO ===")
    numero = int(input("Ingresa un número positivo: "))
    digito = int(input("Ingresa el dígito a buscar (0-9): "))

    if numero < 0 or digito < 0 or digito > 9:
        print("El número debe ser positivo y el dígito entre 0 y 9.")
        return

    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en {numero}")
