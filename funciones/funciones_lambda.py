numeros = [5, 3, 0, 511, 10, 20, 14]

# Son como las arrow functions de Javascript. No tienen nombre y siempre retornan algo
multiplicar_por_dos = lambda x : x * 2


# Funcion comun que diga si es par o no
def es_par(num):
  if (num % 2 == 0):
    return True

# Usando filter con una funcion compu
numeros_pares = filter(es_par, numeros)


# Con Lambda
numeros_pares = filter(lambda numero:numero % 2 == 0, numeros)
print(list(numeros_pares))