
import os 

os.system("cls")

print("Exemplo - Calculando a Tabuada")

numero = int(input("Digite um número:"))

#Contador ou incremento
i = 0 
while (i <= 10):
    print(f"{numero} X {i} = {numero * i}")
    i+=1
print("O programa terminou")
input("Pressione a tecla <enter> para finalizar...")

