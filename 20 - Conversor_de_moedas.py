import os

# Função que exibe o menu 
def exibir_menu():
    print("\n === CONVERSOR DE MOEDAS ===")
    print("[1] Converter Dolar -> REAL")
    print("[2] Converter REAL -> DOLAR")
    print("[0] Sair")

# Função Converter de dolar para a real 
def converter_dolar_para_real(quantia_dolar, taxa):
    return quantia_dolar * taxa 

# Função converter de real para dolar
def converter_real_para_dolar(quantia_real, taxa):
    return quantia_real / taxa 

# Função principal do programa
def main():
    os.system("cls")

    # Solicitando a taxa de cambio do dia 
    taxa_cambio = float(input("Informe a taxa de câmbio (1 USD = quantos BRL?): "))

    resposta = "sim"

    while resposta.lower() == "sim":
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            qtd_dolar = float(input("Digite a quantia em DOLAR (USD): "))
            total_convertido = converter_dolar_para_real(qtd_dolar, taxa_cambio)
            print(f"USD {qtd_dolar} = R$ {total_convertido:.2f}")

        elif opcao == "2":
            quantia_real = float(input("Digite o valor em REAL (BRL): "))
            total_convertido = converter_real_para_dolar(quantia_real, taxa_cambio)
            print(f"R$ {quantia_real} = USD {total_convertido:.2f}")

        elif opcao == "0":
            print("Encerrando o programa... Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

        resposta = input("Deseja realizar outra conversão? (sim/não): ")

# Chamando a função main 
main()
