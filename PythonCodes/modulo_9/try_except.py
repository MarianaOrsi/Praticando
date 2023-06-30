# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

"""try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')"""



# Try e Except com Input:

"""try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar o valor em números')
"""


# Try e Except com Else

"""try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar o valor em números')
else:
    print('Valor correto!')"""


# Try e Except com Finally

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar o valor em números')
finally:
    print('Valor correto!')

"""
else: A cláusula else permite executar um bloco de código caso o código dentro do bloco try 
tenha sido executado sem erros (ou seja, sem lançar nenhuma exceção).

finally: Todo código inserido em uma cláusula finally é executado independentemente de ter havido 
ou não erros na execução do bloco try.
"""

















