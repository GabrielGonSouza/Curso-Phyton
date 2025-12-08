
import os

# Lista que armazena todos os clientes
lista_de_clientes = [
    {
        "nome": "Ana Silva",
        "idade": 29,
        "email": "ana.silva@email.com",
        "celular": "11 91234-5678"
    },
    {
        "nome": "Carlos Pereira",
        "idade": 34,
        "email": "carlos.pereira@email.com",
        "celular": "21 99876-5432"
    },
    {
        "nome": "Mariana Torres",
        "idade": 22,
        "email": "mariana.torres@email.com",
        "celular": "31 98765-4321"
    },
    {
        "nome": "João Mendes",
        "idade": 41,
        "email": "joao.mendes@email.com",
        "celular": "48 99555-1111"
    },
    {
        "nome": "Fernanda Costa",
        "idade": 27,
        "email": "fernanda.costa@email.com",
        "celular": "19 99123-4455"
    }
]

# Função que limpa a tela
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função que exibe o menu na tela
def exibir_menu():
    print("\n=== MENU PRINCIPAL ===")
    print('[1] - Cadastro de Clientes')
    print('[2] - Listar Clientes Cadastrados')
    print('[3] - Editar Dados de Cliente')
    print('[4] - Excluir um Cliente')
    print('[5] - Sair do Sistema \n')

# Função que volta para o menu principal
def voltar_ao_menu_principal():
    input("\nPressione <Enter> para voltar ao menu inicial...")
    main()

# Função que cadastra um novo cliente
def cadastrar_novo_cliente():
    limpar_tela()
    print("=== CADASTRO DE NOVO CLIENTE ===\n")

    # Solicitando os dados do cliente
    nome = input("Digite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    celular = input("Digite o celular do cliente: ")

    # Agrupando os dados do cliente
    dados_cliente = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'celular': celular
    }

    # Adicionando o cliente na lista
    lista_de_clientes.append(dados_cliente)

    # Exibindo mensagem de sucesso
    print(f"\nO Cliente {nome} foi cadastrado com sucesso!")

    # Voltar para o menu principal
    voltar_ao_menu_principal()

# Função que lista todos os clientes cadastrados
def listar_clientes_cadastrados():
    limpar_tela()
    print("=== LISTA DE CLIENTES CADASTRADOS ===\n")

    if not lista_de_clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for indice, cliente in enumerate(lista_de_clientes):
            print(f"Índice: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")

    voltar_ao_menu_principal()

# Função que exclui um cliente cadastrado
def excluir_cliente():
    limpar_tela()
    print("=== REMOVER CLIENTE ===\n")

    if not lista_de_clientes:
        print("Nenhum cliente para remover.")
    else:
        # Listando os clientes
        for indice, cliente in enumerate(lista_de_clientes):
            print(f"Índice: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")

        # Solicitar ao usuário o índice para remover
        try:
            indice = int(input("\nDigite o índice do cliente que deseja remover: "))

            # Verifica se o índice é válido
            if indice >= 0 and indice < len(lista_de_clientes):
                cliente_removido = lista_de_clientes.pop(indice)
                print(f"\nCliente {cliente_removido['nome']} removido com sucesso!")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, insira um número válido.")

    # Voltar ao menu principal
    voltar_ao_menu_principal()

# Função para editar os dados do cliente
def editar_dados_clientes():
    limpar_tela()
    print("=== EDITAR DADOS DO CLIENTE ===\n")

    # Listando os clientes
    for indice, cliente in enumerate(lista_de_clientes):
        print(f"Índice: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']} | E-mail: {cliente['email']} | Celular: {cliente['celular']}")

    try:
        # Solicitar ao usuário o índice do cliente a ser editado
        indice = int(input("\nDigite o índice do cliente que deseja editar: "))

        if indice >= 0 and indice < len(lista_de_clientes):
            dados_do_cliente = lista_de_clientes[indice]

            print(f"\nEditando os dados do cliente: {dados_do_cliente['nome']}")

            # Solicitar os novos dados
            novo_nome = input(f"Digite o novo nome: (Atual - {dados_do_cliente['nome']}) ")
            nova_idade = input(f"Digite a nova idade: (Atual - {dados_do_cliente['idade']}) ")
            novo_email = input(f"Digite o novo e-mail: (Atual - {dados_do_cliente['email']}) ")
            novo_celular = input(f"Digite o novo celular: (Atual - {dados_do_cliente['celular']}) ")

            # Atualizar os dados
            dados_do_cliente['nome'] = novo_nome
            dados_do_cliente['idade'] = nova_idade
            dados_do_cliente['email'] = novo_email
            dados_do_cliente['celular'] = novo_celular

            print("\nDados atualizados com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

    # Voltar ao menu principal
    voltar_ao_menu_principal()

# Função Principal do meu programa
def main():
    limpar_tela()
    print("Bem-vindo ao Gerenciador de Clientes")

    # Chamar a função que exibe o menu
    exibir_menu()

    # Solicitar uma opção para o usuário
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print("Por favor, escolha uma opção válida.")
        voltar_ao_menu_principal()
        return

    # Verificando qual foi a opção escolhida
    if opcao == 1:
        cadastrar_novo_cliente()
    elif opcao == 2:
        listar_clientes_cadastrados()
    elif opcao == 3:
        # Abrir a edição de clientes
        editar_dados_clientes()
    elif opcao == 4:
        excluir_cliente()
    elif opcao == 5:
        print("\nSaindo do Sistema...")
        exit()  # Finaliza o programa
    else:
        print("Opção Inválida!")
        voltar_ao_menu_principal()

# Chamando a função principal
main()

