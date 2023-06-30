altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))
IMC = peso / (altura / 100) ** 2


if IMC < 18.5:
    print('O seu peso está muito baixo')

elif 18.5 <= IMC < 24.9:
    print('Seu peso está normal')

elif 25.0 <= IMC < 29.9:
    print('Você está com sobrepeso')

elif 30.0 <= IMC < 39.9:
    print('Você está com obesidade')

else:
    print('Você está com obesidade grave')