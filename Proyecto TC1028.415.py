# Media Aritmética, Mediana y Moda con listas anidadas

# Lista principal para almacenar sublistas de números
nums = []

# Entrada de datos
entrada = input("Escribe números separados por comas o 'fin': ")
while entrada.lower() != "fin":
    sublista = []
    partes = entrada.split(",")  # Divide la entrada por comas
    for parte in partes:
        parte = parte.strip()  # Elimina espacios
        try:
            sublista.append(float(parte))  # Convierte a número
        except:
            print(f"Valor inválido: {parte}")
    if sublista:
        nums.append(sublista)  # Agrega la sublista
    entrada = input("Escribe números separados por comas o 'fin': ")

# Función para aplanar la lista anidada
def aplanar(lista):
    resultado = []
    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado

# Función para calcular la media aritmética
def media(nums):
    return sum(nums) / len(nums)

# Función para calcular la mediana
def mediana(nums):
    ordenados = sorted(nums)
    n = len(ordenados)
    mitad = n // 2
    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    else:
        return ordenados[mitad]

# Función para calcular la moda
def moda(nums):
    diccionario = {}
    for n in nums:
        if n in diccionario:
            diccionario[n] += 1
        else:
            diccionario[n] = 1
    max_valor = nums[0]
    max_repeticiones = diccionario[max_valor]
    for llave in diccionario:
        if diccionario[llave] > max_repeticiones:
            max_repeticiones = diccionario[llave]
            max_valor = llave
    return max_valor, diccionario

# Aplanar la lista antes de calcular
numeros = aplanar(nums)

# Menú de opciones
print("\nIngresa la opción que deseas realizar:")
print("1. Calcular media aritmética")
print("2. Calcular mediana")
print("3. Calcular moda")

opcion = input("Opción: ")

if opcion == "1":
    print("La media aritmética es:", "%.1f" % media(numeros))
elif opcion == "2":
    print("La mediana es:", "%.1f" % mediana(numeros))
elif opcion == "3":
    moda_resultado, repeticiones = moda(numeros)
    print("La moda es:", moda_resultado)
    print("Repeticiones de cada número:", repeticiones)
else:
    print("Por favor ingresa una opción válida.")