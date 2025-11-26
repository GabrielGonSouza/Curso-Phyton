#Importando a biblioeteca os
import os

#Limpando a tela 
os.system("cls")

temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura >= 30:
    print("Está quente!")
elif temperatura >=20:
    print("Está agradavel !")
elif temperatura >=10:
    print("Está frio!")
else:
    print("Está muito Frio!")