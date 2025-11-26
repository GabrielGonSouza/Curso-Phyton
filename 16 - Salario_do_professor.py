
import os 

#Limpar a tela
os.system("cls")

print("Atividade 04 - Salario do professor")

print("Digite qual é o seu nível: \n 1 - Nível 1 \n 2 - Nível 2 \n 3 - Nível 3")

nivel = input("Informe o seu nível:")

qtd_aulas = int(input("Qual é sua qtd de aulas por semana:"))

if nivel == "1":
    salario = (qtd_aulas * 12) * 4  
elif nivel == "2":
    salario = (qtd_aulas * 17) * 4
elif nivel =="3":
    salario = (qtd_aulas * 25) * 4
else:
    print("O nível digitado é invalido!")

#Saida
print(f"O seu salário será: {salario}")
