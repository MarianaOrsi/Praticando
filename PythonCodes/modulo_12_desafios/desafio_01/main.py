temperatura = int(input('Qual é a temperatura da carne? '))


if temperatura < 48:
    print('A carne está crua! precisa cozinhar um pouco mais')

elif temperatura in range(48, 53):
    print('A carne está selada')

elif temperatura in range(54, 59):
    print('A carne está ao ponto para mal')

elif temperatura in range(60, 64):
    print('A carne está ao ponto')

elif temperatura in range(65, 70):
    print('A carne está pronta! bem passada')

else:
    print('A carne queimou ):')

