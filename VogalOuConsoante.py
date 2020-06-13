#VogalOuConsoante
import os
os.system('cls')

print('Vogal ou consoante ?')

letra = input('Informe uma letra: ')
letra = letra.lower()

vogais = ['a','e','i','o','u']

if letra in vogais:
    print('É uma Vogal')
elif (letra.isalpha()) == True:
    print('É uma Consoante')
else:
    print('Não é uma Letra !')