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