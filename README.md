# Central Tendency Calculator

###  Contexto
------------
Las medidas de tendencia central son herramientas fundamentales en el análisis estadístico. Nos permiten resumir grandes volúmenes de datos en valores representativos, facilitando la interpretación y toma de decisiones en diversos contextos: desde estudios académicos hasta reportes empresariales. Sin embargo, muchas veces se utilizan sin comprender del todo su significado, sus diferencias o cuándo es más adecuado aplicar cada una.

Este proyecto presenta una calculadora interactiva que permite al usuario ingresar un conjunto de datos y obtener automáticamente las principales medidas de tendencia central: **media**, **mediana** y **moda**. 

Se implementan los siguientes métodos:
- **Media aritmética**: suma de los valores dividida entre el número de datos.
- **Mediana**: valor central en un conjunto ordenado.
- **Moda**: valor o valores que más se repiten.

Referencias:
- https://repositorio-uapa.cuaed.unam.mx/repositorio/moodle/pluginfile.php/2752/mod_resource/content/1/UAPA-Medidas-Tendencia-Central/index.html

------------
### Algoritmo

    EO = ingresar tipo dato (Moda,Mediana,Media)
    	si 
    		res= Media
    	entonces 
    		insertar numero total datos
    			sum = (total de datos)
    			Media = sum/total de datos
    		EF = (Media)
    		
    	si no
    		res = Moda 
    	entonces
    		insertar lista total de datos
    			crear contador para cada numero
    		Para cada numero hacer
    			Aumentar contador
    		Fin Para
    		
    		Buscar contador mas alto
    		Mostrar contenido contador más alto
    		
    		EF = (Moda)
    		
    		si no 
    			res = Mediana
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
    						sum = (valor_central1 + valor_central2)/2
    					Fin si
    			Mostrar sum
    		EF = (Mediana)
    		Fin Si
    	Fin Si

------------
### Módulo utilizado

#### Módulo sys
En este proyecto, el módulo sys se utiliza para terminar la ejecución del programa de forma segura cuando se detectan errores en la entrada del usuario. Por ejemplo, si el usuario introduce un valor no numérico o deja una entrada vacía (como una coma final sin número), el programa muestra un mensaje de advertencia y luego llama a sys.exit() para detener el flujo y evitar cálculos incorrectos.
Este enfoque permite mantener la integridad del programa y ofrece una experiencia más controlada para el usuario.

#### Módulo time
Esta calculadora utiliza el módulo estándar time de Python, no para la lógica de cálculo en sí, sino para la medición del rendimiento y la eficiencia de los algoritmos de las medidas de tendencia central.

------------

#### Instrucciones
Descargar el código y correr en terminal o IDE de su preferencia.








