# Media Aritmética y Mediana

# Lista de variables

print("Ingresa una lista de 10 números para continuar:")

n1= float(input())
n2= float(input())
n3= float(input())
n4= float(input())
n5= float(input())
n6= float(input())
n7= float(input())
n8= float(input())
n9= float(input())
n0= float(input())

nums = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n0]

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
    
#Menú opciones

print("Ingresa la opción que deseas realizar:")
print("1. Calcular media aritmética:")
print("2. Calcular mediana:")

opcion = int(input())

if opcion == 1:
    print("La media aritmética es:", "%.1f" % media(nums))
elif opcion == 2:
    print("La mediana es:", "%.1f" % mediana(nums))
else:
    print("Opción no valida")
    




    