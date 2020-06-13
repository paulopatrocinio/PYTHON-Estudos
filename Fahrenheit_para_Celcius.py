import os

#os.system('cls' if os.name == 'nt' else 'clear')
#nome = os.name
#print(nome, '\n')

os.system('cls')

print("Converte de Fahrenheit para Celsius", '\n')
tempFahrenheit = int(input("Temperatura em Fahrenheit = "))
tempCelcius = (5*(tempFahrenheit-32)/9)
print("Temperatura em Celcius = ", tempCelcius, '\n')