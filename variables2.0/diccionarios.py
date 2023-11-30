# creando diccionarios con dict()
# es un set pero con Keys que elijamos (JSON)
diccionario = dict(nombre='Lucas', apellido='Dalto')

diccionario2 = dict.fromkeys(['nombre', 'apellido'])

diccionario3 = dict.fromkeys(['nombre', 'apellido'], 'no se')

print(diccionario)
print(diccionario2)
print(diccionario3)
