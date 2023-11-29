# crear un conjunto con set()
conjunto = set(['dato1', 'dato2'])

# para meter conjunto de otro conjunto
# conjunto1 = frozenset (['dato1', 'dato2'])
# conjunto2 = {conjunto1, 'dato3'}


# Teoria de ocnjuntos

conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# issubset
resultado = conjunto2.issubset(conjunto1) # issubset puede reemplazarse con <= y >=(sub) o < y >(super)

print(resultado)
