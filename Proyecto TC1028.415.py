# Media Aritmética y Mediana y Moda

nums = [] #LISTA VACÍA PARA ALMACENAR LOS NÚMEROS

# CICLO WHILE PARA CANTIDAD INDEFINIDA DE DATOS
entrada = input("Escribe un número o 'fin': ")
while entrada.lower() != "fin": # Función ".lower()" coloca todos los caracteres en minúscula
    try:
        nums.append(float(entrada)) # ".append()" agrega datos al final de la lista
    except:
        print("Número inválido.")
    entrada = input("Escribe un número o 'fin': ") 

# Media Aritmética

def media (nums):
    return sum(nums) / len(nums) # "len()" longitud de la lista

# Mediana

def mediana (nums):
    ordenados = sorted(nums) # "sorted()" acomodar en orden los elementos en la lista
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
    print("Repeticiones de cada número:", repeticiones)
else:
    print("Porfavor ingresa una opción válida.")