# funcoes.py

def inserir_produto(produtos):
    codigo = input("Digite o código do produto (13 caracteres): ")
    while len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido. Deve ter 13 caracteres numéricos.")
        codigo = input("Digite o código do produto (13 caracteres): ")

    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    while not nome or not nome[0].isupper():
        print("Nome inválido. Deve começar com letra maiúscula.")
        nome = input("Digite o nome do produto (começando com letra maiúscula): ")

    preco = input("Digite o preço do produto (formato XX.XX): ")
    while not preco.replace('.', '', 1).isdigit():
        print("Preço inválido. Deve ser um número válido.")
        preco = input("Digite o preço do produto (formato XX.XX): ")

    produtos.append({"codigo": codigo, "nome": nome, "preco": float(preco)})
    print("Produto inserido com sucesso.")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso.")
            return
    print("Produto não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\n--- Lista de Produtos ---")
        for i, produto in enumerate(produtos, start=1):
            print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"Preço do produto {produto['nome']}: R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")
