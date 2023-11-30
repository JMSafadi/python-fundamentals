animales = ['gato', 'perro', 'loro', 'cocodrilo', 'pez']

# for animal in animales:
#   print(f'Ahora la variable animal es igual a: {animal}')

# print(numeros_dobles)

numeros = [10, 62, 12, 72]
resultados = []

for numero in numeros:
  duplicado = numero * 10
  resultados.append(duplicado)
  
# print(resultados)

for numero, animal in zip(animales, numeros):
  print(f'recorriendo lista 1: {numero}')
  print(f'recorriendo lista 2: {animal}')


# Recorrer por rango qu le digamos (primer argumento=donde empieza, segundo argumento=donde termina)
# Forma no optima
for num in range(len(numeros)):
  print(numeros[num])

# Forma optima
for num in enumerate(numeros):
  indice = num[0]
  valor = num[1]
  print(f'el indice es: {indice} y el valor es: {valor}')

# usando el else
for numero in numeros:
  print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else: print('el bucle termino')
