import os

# Limpar a tela (Windows / Linux / Mac)
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Cálculo do salário por nível
def calcular_salario(nivel, aulas):
    valores = {"1": 12, "2": 17, "3": 25}
    return valores.get(nivel, 0) * aulas * 4

# Tela inicial com ASCII
def exibir_titulo():
    print(r"""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┫┃╭━━┳━┳┳━━╮╭━╯┣━━╮
╰━━╮┃╭╮┃┃┃╭╮┃╭╋┫╭╮┃┃╭╮┃╭╮┃
┃╰━╯┃╭╮┃╰┫╭╮┃┃┃┃╰╯┃┃╰╯┃╰╯┃
╰━━━┻╯╰┻━┻╯╰┻╯╰┻━━╯╰━━┻━━╯
""")

def main():
    limpar_tela()
    exibir_titulo()

    while True:
        print("Escolha seu nível:\n 1 - Nível 1\n 2 - Nível 2\n 3 - Nível 3")
        nivel = input("Informe o nível: ").strip()

        if nivel not in ["1", "2", "3"]:
            print("❌ Nível inválido! Tente novamente.\n")
            continue

        try:
            aulas = int(input("Quantidade de aulas por semana: "))
        except ValueError:
            print("❌ Digite um número válido!\n")
            continue

        salario = calcular_salario(nivel, aulas)
        print(f"💰 Seu salário será: R${salario:.2f}\n")

        if input("Deseja calcular novamente? (sim/não): ").lower() != "sim":
            break

    input("\nPressione <Enter> para finalizar...")

if __name__ == "__main__":
    main()
