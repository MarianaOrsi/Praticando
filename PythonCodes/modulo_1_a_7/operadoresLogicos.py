# Operadores If e Else com and e or


"""renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento Aprovado')

else:
    print('Financiamento Reprovado')


renda_acima_10mil = True
nome_limpo02 = False

if renda_acima_10mil or nome_limpo02:
    print('Financiamento Liberado')

else:
    print('Financiamento Negado')


# If Ternário:

idade = 17

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'
print(resultado)


# Multiplos Operadores de Comparação:

valor = 41

if 10 <= valor < 40:
    print('Seu produto foi aceito')

else:
    print('Seu produto foi negado') """


# For Loops - Looping:

# Imprimindo números
# Lembrando que o python sempre imprime começando do index, ou seja, do 0
# Neste caso, colocando o Range 5 será impresso de 0 a 4

""" for numero in range(5):
    print(numero) """

# Para imprimir do 1 ao 5 você pode utilizar o Range da seguinte forma:

""" for numero01 in range(1, 6):
    print(numero01) """

# O Range também possui o step
# O step imprime um número e pula outro, por exemplo:

""" for numero02 in range(1, 20, 2):
    print(numero02) """

# range( iniciar , parar, etapa )
# no caso, irá iniciar do 1, vai parar no 19 e vai pular de duas em duas etapas


# For Loops - Looping para strings
"""  palavra = 'Google'
for letra in palavra:
    print(f' {letra} está dentro da palavra {palavra}') """


# Lição: Enviar um e-mail com os detalhes da compra
# Máximo 3 tentativas para compras confirmadas

"""compra_confirmada = True
dados_compra = 'Compra no valor de 40.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break

else:
    print('Falha na compra') """


# For Loop - Nested Loops:

   # Outer loop
        # Inner loop

"""for numero01 in range(1, 6):
    print('Produto ' + str(numero01))
    for numero02 in range(11):
        print(numero01, numero02)"""


# Lição: Modificar a palabra FANTASTICO para F A N T A S T I C O

""" palavra = 'FANTASTICO'

for spaco in palavra:
    print(f' {spaco}' , end='') """


# While Loops:
"""valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto será vendido por R${valor}')
    valor -= 5 """

# Diferenças entre if for e while loop

#O if / else sempre executa uma vez só (verdadeiro ou falso)

#O for loop serve quando você já sabe quantas vezes você quer executar (quero que execute por X vezes)

#O while loop serve quando você NÃO sabe quantas vezes você quer executar (faça isso enquanto...)




# Lição: Criar um programa para publicar um produto com comissão de 10% se for acima de R$20:
valor = int(input('Digite o valor do seu produto em R$: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R${valor}')
    break



