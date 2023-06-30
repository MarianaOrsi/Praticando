nome01 = input('Digite o seu nome: ')
quantidade = 10

def boas_vindas():
    print(f'Olá {nome01}')
    print(f'Temos {str(quantidade)} notebooks em estoque')
    valor_input = int(input('Digite aqui quantos você deseja comprar: '))

    if quantidade >= valor_input:
        resultado = quantidade - valor_input
        print(f'Sobraram {resultado} no estoque')
    else:
        print('Sem estoque no momento')

boas_vindas()