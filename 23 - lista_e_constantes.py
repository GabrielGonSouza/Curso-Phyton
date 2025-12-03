
import os 

from typing import Final

os.system("cls")

#Definindo uma constante no python 

# TAXA_DE_CAMBIO = 10

# quantia_dolar = float(input("Digite o valor em dólares: "))
# TAXA_DE_CAMBIO = float(input("Digite o valor em dólares: "))
# valor_em_real = quantia_dolar * TAXA_DE_CAMBIO
# print(f"O Valor convertido em reais é: R$ {valor_em_real: .2f}")

#Exemplos de criação de listas 
numeros = [1,2,3,4,5]
nomes = ["Joaquim", "Maria", "Ana"]

print("List inicial")
print(nomes)

print("================================)")

#Alterando um elememento da lista
nomes[0] = "Carlos"
print(f"Nome da posição 0: {nomes[0]}")

#Adicionar um novo elemento na no final da lista 
nomes.append("Roberval")
nomes.append("Ricardo")

#Adicionando um elemento em uma posicao especifica da lista 
nomes.insert(1, "Fernanda")


print("lista Atualizada!")
print(nomes)


#Removendo o elemento da posicao 3 (Maria) da Lista
del nomes[3]

print ("Lista atualizada após a remoção da Maria")
print(nomes)

#Removendo e retornando o elemento no indice 2 
nome_removido = nomes.pop(2)
print(f"O nome removido foi: {nome_removido}")

print ("lista Atualizada após o POP")
print(nomes) 

#Apagar todos os elementos da lista 
nomes.clear()

print ("Lista Atualizada após o CLEAR")
print(nomes)



