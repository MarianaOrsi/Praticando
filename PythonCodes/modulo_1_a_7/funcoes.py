# Para a criação de uma função em Python, usamos a palavra reservada def, seguida do nome da função.

""" def boas_vindas():
    print('Olá Mariana!')
    print('Você está aprendendo funções em python!')

boas_vindas() """

# Funções diferentes mas variaveis iguais:

""" def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_numeros1():
    numero1 = 10
    numero2 = 15
    resultado = numero1 + numero2
    print(resultado)

somar_dois_numeros()
somar_dois_numeros1()
# OBS: como elas estão dentro de duas funções diferentes, o python não reclama de ter variáveis com o mesmo nome."""

# Funções: Parametro e Argumento:

"""def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notebooks em estoque')
boas_vindas('Mari', 5) """

# Default e Non-Default:
# Default = Aquele que você define o valor no parametro
# Non-Default = Aquele que você não define o valor no parametro
# Regra: o Default deve sempre vir por ultimo nos parametros
# Exemplo: (nome, quantidade=6) correto | (quantidade=6, nome) errado
"""def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notebooks em estoque')

boas_vindas('Mari')"""


# Return - Armazenar e retornar um valor

"""def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('João')

print(y)"""

# Lição: Criar uma função que soma vários números. (Vários Argumentos = xargs)
# o * no começo do parametro, significa vários argumentos - xargs (não tem um número definido)

"""def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2, 3, 4, 7)
print(x)"""

# Lição: Criar uma função que armazena vários parametros E argumentos
# o * no começo do parametro, significa vários ARGUMENTOS (não tem um número definido)
# e ** no começo do parametro, significa vários PARAMETROS (não tem um número definido)

def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branco', motor=1.0))
print(agencia(marca='Fiat', cor='Preto', motor=2.0, placa=123456))
print(agencia(marca='Bmw', cor='Azul', motor=5.0, placa='sem placa'))

