# Proyecto_TC1028.415
El proyecto presentado tendrá como objetivo optimizar tareas básicas en la materia de Estadística. A lo que ayudará es a calcular la Media, Moda y Mediana para datos simples y agrupados. Esto facilitará los cálculos rápidos para poder seguir con elaboraciones más complejas.

ALgoritmo Estadístico
  EO= ingresar tipo dato = (Moda,Mediana,Media) 
	si 
		res= Media
	entonces 
		insertar numero total datos
			sum= (total de datos)
			Media= sum/total de datos
		EF=(Media)
		
si no
		res= Moda 
	entonces
		insertar lista total de datos
			crear contador para cada numero
		Para cada numero hacer
			Aumentar contador
		Fin Para
		
Buscar contador mas alto
		Mostrar contenido contador más alto
		
EF=(Moda)
		
si no 
			res= Mediana
		entonces
			insertar lista total de datos
				ordenar de menor a mayor
				mostrar lista ordenada
					si
						cantidad de datos es impar
					entonces 
						seleccionar el valor del medio
					si no 
						seleccionar dos valores centrales
						sum= (valor_central1 + valor_central2)/2
					Fin si
			Mostrar sum
		EF=(Mediana)
		Fin Si
	Fin Si
