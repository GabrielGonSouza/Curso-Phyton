
import os
os.system("cls")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura )

print (f"Olá {nome}, seu IMC é: {round(imc, 2)}")

#Abaixo do peso 
if imc <= 18.5:
    print("Você está abaixo do peso")
#Peso é normal
elif imc >=24.9:
    print("Peso normal")
#Sobrepeso
elif imc <=29.9:
    print("Sobrepeso")
#Obesidade grau I
elif imc <=34.9:
    print("Obesidade grau I")
#Obesidade grau II
elif imc <=39.9:
    print("Obesidade Grau II")
elif imc >=40:
    print("Obesidade Grau III")

input("Pressione <Enter> para fechar o programa")