from array import array

# Arrays
    # São similares a lista
    # Armazenam mais informações que a lista
    # Melhor performance
    # Precisam ser importadas
    # Precisam do type code > https://docs.python.org/pt-br/3.7/library/array.html

letras = ['a', 'b', 'c', 'd']
numeros_int = [10, 20, 30, 40]
numeros_float = [1.2, 2.2, 3.2, 4.2]

print(letras)
print(numeros_int)
print(numeros_float)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_int = array('i', [10, 20, 30, 40])
numeros_float = array('f', [1.2, 2.2, 3.2, 4.2])

print(letras)
print(numeros_int)
print(numeros_float)
