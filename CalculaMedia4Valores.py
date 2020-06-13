import os
os.system('cls')

#import os
#os.system('cls' if os.name == 'nt' else 'clear')

print('Cálculo da média entre 4 notas')
nota1 = float(input("Informe a 1ª nota = "))
nota2 = float(input("Informe a 2ª nota = "))
nota3 = float(input("Informe a 3ª nota = "))
nota4 = float(input("Informe a 4ª nota = "))
media = ((nota1 + nota2 + nota3 + nota4)/4)

#print("Nota 1 = ", nota1)
#print("Nota 2 = ", nota2)
#print("Nota 3 = ", nota3)
#print("Nota 4 = ", nota4)
print("Média = ", media)