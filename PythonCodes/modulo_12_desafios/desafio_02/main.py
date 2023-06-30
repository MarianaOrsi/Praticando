rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))

def calcular():
    resultado = altura * largura / rendimento
    return resultado
print(f'Você precisa de {calcular()} latas de tinta')