
#1 passo - importar a biblioteca os 
import os

#2 passo - Ultilizar a os para limpar a tela 
os.system("cls")

#3 passo - Realizar as entradas 
nome = input("Digite o seu nome: ")
idade =int(input("Digite sua idade: "))



#4 passo- Verificar a idade do usuário
if idade >=18:
    possui_carteira = input("Possui carteira de motorista? \n (1-Sim | 2-Não):")
    print("Pode dirigir!")

    if possui_carteira == "1":
        print("Pode dirigir")
    else:
     
     print("Não pode dirgir!")
else:
    print("Menor de idade")



    
          
    
   
