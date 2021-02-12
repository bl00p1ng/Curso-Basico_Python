# Curso básico de Python

## 📚 Módulo 1. Introducción a la programación con Python

- ### Clase 3. El núcleo de un programa: los algoritmos

  #### Algoritmo

  - Serie de pasos para resolver un problema
  - Finito
  - No ambiguo. Pasos definidos, con el mismo comportamiento independientemente del contexto.

## 📚 Módulo  2. Conceptos básicos de Python

- ### Clase 8. Explorando Python: operadores aritméticos

  `21 // 5` → Hacer una división entera.

  `2 ** 2` → potenciación

- ### Clase 9. ¿Qué es una variable?

  `x = 2` → Declarar variables en Python

  En Python cuando los nombres de las variables tienen múltiples palabras, cada palabra se separa con un un _

- ### Clase 10. Los primitivos: tipos de datos sencillos

  En Python los decimales se separan con . no con ,

- ### Clase 11. Convertir un dato a un tipo diferente

  - **Input("")** →  pedirle al usuario que introduzca datos.
  - **int()** → se datos o variables como parámetros para convertirlos en números  enteros.
  - **str()** → para convertir números tanto decimales como enteros en strings.

- ### Clase 12. Operadores lógicos y de comparación

  `and`, `or`, `not`

  **🛈 Nota:** en Python los booleanos deben empezar con mayúscula. `True` , `False`

- ### Clase 13. Tu primer programa: conversor de monedas

  ````python
  usd = round(usd, 2) # Redondear una variable a x decimales
  ````


## 📚 Módulo 3. Herramientas para programar

- ### Clase 14. Construyendo el camino de un programa con condicionales

  ````python
  if number > 5:
      print('Es mayor a 5')
  elif number == 5:
      print('Es igual a 5')
  else:
      print('Es menor a 5')
  ````

- ### Clase 15. Varios países en mi conversor de monedas

  ````python
  menu = """
  ...
  """
  ````

  Crear un String de múltiples líneas.

- ### Clase 18. Trabajando con texto: cadenas de caracteres

  `.upper()` → Convertir String en mayúsculas.

  `.capitalize()` → Primera letra en mayúscula

  `.strip()` → Elimina los espacios basura al principio y al final del String

  `.lower()` → Convertir String en minúsculas.

  `.replace('x', 'y')` → Reemplaza todas las ocurrencias por el caracter especificado

  `len(string)` → Retorna longitud del String

  **Acceder a caracteres específicos:** 

  ````python
  string[0]
  ````

- ### Clase 19. Trabajando con texto: slices

  ```python
  string[1:3]
  string[:3] # → va desde el índice 0 hasta el caracter antes del índice 3
  string[3:] # → desde el índice 3 hasta el final
  string[1:7:2] # :2 → pasos/saltos
  string[::] # Traer el string completo
  string[::-1] # Ir desde el final hasta el principio
  ```

- ### Clase 20. Proyecto: palíndromo

  **🛈 Nota:** es una buena práctica en Python tener una función principal que corra el programa y un punto de entrada:

  ````python
  def run(): # Función principal
      pass
  
  
  if __name__ == '__main__': # Punto de entrada
      run()
  
  ````


## 📚 Módulo 4. Bucles

- ### Clase 22. El ciclo while

  ```python
  while power_2 < LIMIT:
      print('2 elevado a ' + str(i) + ' es igual a: ' + str(power_2))
      i += 1
      power_2 = 2**i
  ```

- ### Clase 23. Explorando un bucle diferente: el ciclo for

  ```python
  for i in range(1000):
      print(i)
  ```
  ````python
  for i in range(1, 1001): # i → inicio. 1000 → final
      print(i)
  ````

- ### Clase 24. Recorriendo un string con for

  ```python
  for letter in name:
      print(letter)
  ```

- ### Clase 25. Interrumpiendo ciclos con break y continue

  ```python
  for i in range(100):
  	if i % 2 != 0:
  		continue
  	print(i)
  ```
  ```python
  for i in range(10000):
      if i == 5678:
          break
      print(i)
  ```

- ### Clase 27. Proyecto: videojuego

  ````python
  import random
  
  random_number = random.randint(1, 100) # Generar número alteatorio entero
  ````

## 📚 Módulo 5. Estructuras de datos

- ### Clase 28. Almacenar varios valores en una variable: listas

  #### Estructuras de datos

  Son elementos de los lenguajes de programación que permiten guardar múltiples datos en una variable.

  #### Listas

  ````python
  numbers = [1, 2, 5, 8, 9, 16]
  obj = ['hello', 2, 4, 5, True]
  
  obj[1] # Acceder al elemento de una lista
  obj.append(False) # Agregar un elemento al final de la lista
  obj.pop(3) # Borra el elemento en el índice que se pasa por parametro
  
  # Recorrer un objeto
  for element in object:
      print(element)
      
  obj[::-1] # Inverir un array. Se pueden usar slices en arrays
  
  #Suma (+) Concatena dos o más listas:
  a=[1,2]
  b=[3,4]
  a + b # --> [1,2,3,4]
  
  # Multiplicación (*) Repite la misma lista:
  a=[1,2]
  a * 2 # —> [1,2,1,2]
  
  # Añadir elemento al final de la lista:
  a=[1]
  # a.append(2)=[1,2]
  
  # Eliminar elemento al final de la lista:
  a=[1,2]
  b=a.pop()
  # a=[1]
  
  # Eliminar elemento dado un indice:
  a=[1,2]
  b=a.pop(1)
  # a=[2]
  
  # Ordenar lista de menor a mayor, esto modifica la lista inicial
  a=[3,8,1]
  a.sort() # —> [1,3,8]
  
  # Ordenar lista de menor a mayor, esto NO modifica la lista inicial
  a=[3,8,1]
  a.sorted() # —> [1,3,8]
  
  # Eliminar elementos de lista Elimina el elemento de la lista dado su indice
  a=[1,2,3]
  del a[0] # —> a[2,3]
  
  # Eliminar elementos de lista Elimina el elemento de la lista dado su valor
  a=[0, 2, 4, 6, 8]
  a.remove(6)
  # a=[0, 2, 4, 8]
  
  # **Range creacion de listas en un rango determinado
  a=(list(range(0,10,2))) # -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
  # a=[0,2,4,6,8]
  
  # Tamaño lista len Devuelve el valor del tamaño de la lista:
  a=[0,2,4,6,8]
  len(a)=5
  ````

- ### Clase 29. Entendiendo cómo funcionan las tuplas

  Las pueden ser un tanto ineficientes pues al ser dinámicas requieren mucha más memoria para mantenerlas funcionando.

  Las **tuplas** son estructuras muy similares a las listas, con la diferencia de que las tuplas **sin inmutables**. Es más rápido recorrer una tupla que recorrer una lista.