
import os

os.system("cls")

nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preco do produto: ") )
desconto = float(input("Digite o percentual de desconto: "))

#Calcular o desconto 
valor_desconto = preco * desconto / 100

#Calculando o preço final 
preco_final = preco - valor_desconto

#Exibir o preço final
print(f"Produto:  {nome_produto} - preço Final: R$ {preco_final}")