# Media Aritmética y Mediana y Moda

# Explicación

print("Este programa calcula la media aritmética, mediana y moda de una lista de números")

print("Ingresa todos los números uno por uno. Cuando termines, escribe 'Fin':")

#Lista de variables

nums = []

while True:
    entrada = input()
    if entrada.lower() == 'fin':
        break
    try:
        numero = float(entrada)
        nums.append(numero)
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Media Aritmética

def media (nums):
    return sum(nums) / len(nums)

# Mediana

def mediana (nums):
    ordenados = sorted(nums)
    n = len(ordenados)
    mitad = n // 2
    
    if n % 2 == 0:
        return (ordenados[mitad - 1] + ordenados[mitad]) / 2
    else:
        return ordenados[mitad]
    

# Moda

def moda (nums):

    diccionario = {}

    for n in nums:
        diccionario[n] = 0

    for n in nums:
        diccionario[n] = diccionario[n] + 1

    max_valor = nums[0]
    max_repeticiones = diccionario[max_valor]

    for llave in diccionario:
        if diccionario[llave] > max_repeticiones:
            max_repeticiones = diccionario[llave]
            max_valor = llave

    return max_valor, diccionario
    
#Menú opciones

print("Ingresa la opción que deseas realizar:")
print("1. Calcular media aritmética:")
print("2. Calcular mediana:")
print("3. Calcular moda:")

opcion = int(input())

if opcion == 1:
    print("La media aritmética es:", "%.1f" % media(nums))
elif opcion == 2:
    print("La mediana es:", "%.1f" % mediana(nums))
elif opcion == 3:
    moda_resultado, repeticiones = moda(nums)
    print("La moda es:", moda_resultado)
    print("¿Quieres saber el número de repeticiones de cada dato? (s/n)")
    respuesta = input().lower()
    if respuesta == 's':
        for numero, rep in repeticiones.items():
            print(f"El número {numero} se repite {rep} veces.")
    elif respuesta == 'n':
        print("De acuerdo, no mostraré las repeticiones.")
    
else:
    print("Porfavor ingresa una opción válida.")

