# Reto1-POO

---

## 1. Calculadora de Operaciones Básicas (`1_operaciones.py`)

**Objetivo:** Pedir dos números y un operador (+, -, *, /), y realizar la operación correspondiente.

**Cómo se resolvió:**

- Se creó una función llamada `calculate` que recibe dos números y una cadena con el operador.
- Se usaron condicionales (`if`, `elif`, `else`) para identificar qué operación realizar según el operador ingresado.
- En caso de división, se verifica si el divisor es cero para evitar errores matemáticos.
- El programa interactúa con el usuario a través de la función `input()` y muestra el resultado con `print()`.

---

## 2. Verificación de Palíndromos (`2_palindromo.py`)

**Objetivo:** Comprobar si una palabra se lee igual al derecho y al revés (palíndromo).

**Cómo se resolvió:**

- Se creó una función `palindrome` que recibe una palabra como argumento.
- La palabra se invierte letra por letra mediante un bucle `for` que recorre la palabra desde el final hacia el principio.
- Luego se compara la palabra original con la invertida.
- Si son iguales, se retorna que es un palíndromo; si no, se indica lo contrario.

---

## 3. Detección de Números Primos en una Lista (`3-primos.py`)

**Objetivo:** Leer una lista de números e identificar cuáles son primos.

**Cómo se resolvió:**

- Se creó una función `isPrime` que verifica si un número es primo:
  - Se descartan los números menores que 2.
  - Se intenta dividir el número por todos los valores desde 2 hasta su raíz cuadrada.
- Otra función llamada `list_prime` recorre la lista de números ingresada por el usuario, y usa `isPrime` para filtrar los primos.
- Finalmente, se imprime una nueva lista con los números primos encontrados.

---

## 4. Mayor Suma de Dos Números Consecutivos (`4_mayor_suma.py`)

**Objetivo:** Dada una lista de números, encontrar la mayor suma entre dos elementos que estén uno al lado del otro.

**Cómo se resolvió:**

- Se creó una función `max_sum_consecutive` que recorre la lista y suma pares consecutivos de elementos (`nums[i] + nums[i+1]`).
- Se mantiene un registro del valor máximo encontrado hasta el momento.
- Si la lista tiene menos de dos elementos, el programa devuelve un mensaje indicando que no hay suficientes datos.

---

## 5. Agrupación de Palabras con los Mismos Caracteres (`5_mismos_caracteres.py`)

**Objetivo:** Encontrar y agrupar palabras que tengan los mismos caracteres, sin importar el orden (anagramas).

**Cómo se resolvió:**

- Se creó una función `same_characters` que convierte cada palabra en una "clave" ordenando alfabéticamente sus letras.
- Las palabras con la misma clave se agrupan en un diccionario (`groups`).
- Luego se recorren los grupos, y se devuelven solo aquellos que tengan más de una palabra (es decir, que sean anagramas).
- Finalmente, se imprime la lista de palabras agrupadas.


