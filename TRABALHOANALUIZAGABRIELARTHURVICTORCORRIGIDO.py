estoque = {}

def adicionar_item(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Item '{nome}' adicionado. Quantidade: {estoque[nome]}")

def remover_item(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Item '{nome}' removido do estoque.")
    else:
        print(f"Item '{nome}' não encontrado.")

def ver_estoque():
    print("\n--- Estoque Atual ---")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")
    print("----------------------")

def alterar_quantidade(nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do item '{nome}' alterada para {quantidade}.")
    else:
        print(f"Item '{nome}' não encontrado.")

while True:
    print("\n1. Adicionar Item\n2. Remover Item\n3. Ver Estoque\n4. Alterar Quantidade\n5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Somente numeros, Quantidade: "))
        adicionar_item(nome, quantidade)
    elif opcao == "2":
        nome = input("Nome do item: ")
        remover_item(nome)
    elif opcao == "3":
        ver_estoque()
    elif opcao == "4":
        nome = input("Nome do item: ")
        quantidade = int(input("Nova quantidade: "))
        alterar_quantidade(nome, quantidade)
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")