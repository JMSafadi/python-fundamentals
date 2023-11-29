diccionario = {
  'nombre' : 'lucas',
  100 : 'dalto',
  'subs' : 1000,
}

claves = diccionario.keys() # iterar keys
claves = diccionario.get(100) # iterar keys
claves = diccionario['subs'] # iterar keys
diccionario.pop('subs')

print(diccionario)
