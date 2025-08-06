usuarios = []

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o e-mail: ")
    
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email
    }
    
    usuarios.append(usuario)
    print("✅ Usuário cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("⚠️ Nenhum usuário cadastrado.\n")
        return

    print("📋 Lista de Usuários:")
    for i, u in enumerate(usuarios):
        print(f"{i + 1}. Nome: {u['nome']}, Idade: {u['idade']}, E-mail: {u['email']}")
    print()

def remover_usuario():
    listar_usuarios()
    if not usuarios:
        return

    try:
        indice = int(input("Digite o número do usuário que deseja remover: ")) - 1
        if 0 <= indice < len(usuarios):
            removido = usuarios.pop(indice)
            print(f"🗑️ Usuário '{removido['nome']}' removido com sucesso!\n")
        else:
            print("❌ Índice inválido.\n")
    except ValueError:
        print("❌ Entrada inválida. Digite um número.\n")

def menu():
    while True:
        print("=== MENU ===")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Remover usuário")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            remover_usuario()
        elif opcao == "4":
            print("👋 Encerrando o programa. Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.\n")

# Inicia o programa
menu()
