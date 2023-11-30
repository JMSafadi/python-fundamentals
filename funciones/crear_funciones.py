# creando funciones simples
def saludar(nombre, sexo):
  sexo = sexo.lower()
  if(sexo == 'hombre'):
    print(f'Hola, {nombre}, mi maestro. todo bien?')
  elif(sexo == 'mujer'):
    print(f'Hola, {nombre}, mi maestra. todo bien?')
  else:
    print(f'Hola, {nombre}, mi maestrx. todo bien?')


# Ejecutando
saludar('Boluda', 'asdasd')

# funcion que retorne valores
def crear_contraseña_random(num):
  chars = 'aorijsrlaofnakjfn'
  num_entero = str(num)
  num = int(num_entero[0])
  c1 = num - 2
  c2 = num
  c3 = num - 5
  contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
  return contraseña, num

password, num = crear_contraseña_random(8)
frase = f'Tu contraseña nueva es: {password}. Num utilizado: {num}'
print(frase)

# sumar valores de array con FOR
def suma(*numeros):
  return sum(numeros)

resultado = suma(2,6,1,5,125)
print(resultado)
