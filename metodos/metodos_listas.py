# 

nombres = ['juan', 'pepe']
nombres.append('toto')
nombres.insert(1, 'capo')
nombres.extend([False, 'nashe'])
nombres.pop(2)
# nombres.pop(-2) - elimina el ultimo siempre
nombres.remove('capo')
# lista.clear() - elimina todos los elementos
nombres.reverse()

# print(nombres)
# print(len(nombres))


numeros = [5, 12, 0, -25]
# numeros.sort() # reverse=true los ordena de forma descendente
print(numeros.index(12))
