
import os 
import random 

#Função que sorteia um número secreto (de 1 a 50)
def sortear_numero_secreto():
    numero_secreto = random.randint(1,50)
    return numero_secreto

#Função que solicita um palpite
def solicitar_palpite():
    palpite = int(input("Digite seu palpite: "))
    return palpite 

#Função que verificar o palpite do jogador
def verificar_palpite(palpite, numero_secreto):
    #Verificar se o palpite é menor que o número secreto 
    if palpite < numero_secreto:
        return "menor"
    #Verificar se o palpite é o maior que o número_secreto
    elif palpite > numero_secreto:
        return "maior"
    #Verificar se o palpite é igual ao número_secreto 
    else:
        return "igual"


#Função principal 
def main(): 
    #Limpa a tela 
    os.system("cls")

    #Gera o número secreto
    numero_secreto = sortear_numero_secreto()
    
    #Controla o número de tentativas 
    tentativas = 0 

    print("Bem vindo ao jogo da adivinhação!")
    print("Tente adivinhar o número entre 1 e 50 \n")
    print("Você tem 5 tentativas...")
    print("""
██████╗░░█████╗░░█████╗░  ░██████╗░█████╗░██████╗░████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██████╦╝██║░░██║███████║  ╚█████╗░██║░░██║██████╔╝░░░██║░░░█████╗░░
██╔══██╗██║░░██║██╔══██║  ░╚═══██╗██║░░██║██╔══██╗░░░██║░░░██╔══╝░░
██████╦╝╚█████╔╝██║░░██║  ██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝""")



    input("Pressione <Enter> para continuar...")


    while tentativas <= 5:
        os.system

        #Acresentar o número de tentativas 
        tentativas += 1 

        #Solicitando um palpite 
        palpite = solicitar_palpite()
    
        #Verificar o palpite do jogador 
        resultado = verificar_palpite(palpite, numero_secreto)
        print(f"O Resultado é: {resultado}")

        if resultado == "menor":
            print("Seu palpite foi menor que o número secreto")
            input("Pressione <Enter> para continuar...")

        elif resultado == "maior":
            print("Seu palpite foi maior que o número secreto, tente novamente..")
            input("Pressione <Enter> para continuar...")

        else: 
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            input("Pressione <Enter> para continuar...")
            break 

    else: 
        print("Fim de Jogo!")

#Chamar a função main
main()
