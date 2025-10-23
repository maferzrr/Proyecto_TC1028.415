"""
Proyecto TC1028.415 en Python

Calculadora de Medidas de Tendencia Central.

El programa realiza diversos cálculos dependiendo de la necesidad del usuario,
ya sea que requiera calcular Media Aritmética, Mediana o Moda.
Al final, el programa imprime los resultados obtenidos de los datos otorgados por el usuario.
"""

# Bibliotecas
import sys
import time

# ========== Funciones principales ==========

def media(nums):

    """
    Pasando como parámetro la lista "nums"
    Utiliza:
    sum: para sumar los números en la lista
    len: cuenta todos los elementos en la lista
    Se dividen entre ellos.
    """
    return sum(nums) / len(nums)



def mediana(nums):

    """
    Pasando como parámetro la lista "nums"
    Utiliza:
    sorted: para odenar los números de menor a mayor.
    y len.
    If para verificar si la lista tiene números par o impar.
    """
    ordenados = sorted(nums)
    n = len(ordenados)
    mitad = n // 2
    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    else:
        return ordenados[mitad]


def moda(nums):

    """
    El diccionario almacena los datos de la lista.
    Ciclos for, iteran en el diccionario para comprobar los elementos.
    Compreuban la mayor cantidad de repeticiones de un elemento.
    """
    diccionario = {}
    for n in nums:
        diccionario[n] = diccionario.get(n, 0) + 1
    max_valor = max(diccionario, key=diccionario.get)
    return max_valor, diccionario

# ========== Main ==========

# Bienvenida
print("Hola! Bienvenido a esta calculadora de medidas de tendencia central!")
time.sleep(1)
print("Puedes calcular la media, mediana y moda de tus datos.")
time.sleep(1)


# Lista para guardar resultados
resultados = []

continuar = "S"
while continuar.upper() == "S":
    # Entrada de datos
    listas_datos = []
    print("\n¿Cuántas listas deseas ingresar?")
    cantidad_datos = int(input("Listas:"))
    for i in range(cantidad_datos):
        nums = []
        print("\nEscribe tus números separados por comas:")
        entrada = input("Datos: ")
        datos = entrada.split(",")
        # Limpiar lista validar entradas
        for dato in datos: 
            dato = dato.strip()
            if dato == "":
                print("Entrada vacía detectada.")
                print("Verifica que no haya comas al final.")
                print("Porfavor reincie el programa.")
                sys.exit()
            try:
                nums.append(float(dato))
            except ValueError:
                print("Valor inválido")
                print("Porfavor reincie el programa.")
                sys.exit()
        listas_datos.append(nums)
 
    """
    Se utiliza try y except para comprobar que los datos sean de tipo float.
    Si se detectan entradas inválidas el programa imprime error.
    """

    # Comprobar cantidad_datos
    print("\nListas ingresadas:", listas_datos)
    time.sleep(2)

    # Menú de opciones
    print("\n ==== MENÚ DE OPCIONES ====")
    print("1. Calcular media aritmética")
    print("2. Calcular mediana")
    print("3. Calcular moda")

    opcion = input("Opción: ")

    if opcion == "1":
        for nums in listas_datos:
            time.sleep(1)
            resultado = media(nums)
            print("La media aritmética es:", "%.2f" % resultado)
            resultados.append(f"Media: {resultado:.2f}")
    elif opcion == "2":
        for nums in listas_datos:
            time.sleep(1)
            resultado = mediana(nums)
            print("La mediana es:", "%.2f" % resultado)
            resultados.append(f"Mediana: {resultado:.2f}")
    elif opcion == "3":
        for nums in listas_datos:
            time.sleep(1)
            moda_resultado, repeticiones = moda(nums)
            print("La moda es:", moda_resultado)
            print("Repeticiones:", repeticiones)
            resultados.append(f"Moda: {moda_resultado}")
    else:
        print("¡ERROR! Opción inválida.")

        
    time.sleep(1)
    print("\n¿Deseas realizar otra operación? S/N")
    continuar = str(input())
    if continuar.upper() not in ["S", "N"]:
        print("Valor inválido")


# Mostrar todos los resultados
if continuar.upper() == "N":
    print("\n==== RESUMEN DE RESULTADOS ====")
    for r in resultados:
        print("-", r)
    print("\n¡Gracias por usar el programa!")

"""
(Condicionales IF)
Mandan a llamar al función requerida
dependiendo del input del usuario.
"""