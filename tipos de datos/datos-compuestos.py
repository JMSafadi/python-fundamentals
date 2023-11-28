lista = [0, 1, 23, 'python']
lista[3] = 'java'

print(lista)


# Tupla funciona igual que un array, solo que no puede modificarse (como un const)
tupla = ('julian', 5, True)
print(tupla)

# conjunto (set)
set1 = { 'pepe', False, 652 }
print(set1)

# diccionario (como un JSON)
diccionario = {
  'nombre': 'Julian',
  'apellido': 'Safadi',
  'edad': 26
}
print(diccionario['apellido'])
