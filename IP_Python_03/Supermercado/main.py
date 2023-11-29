

def main():
    produtos = []

    opcao = 1

    while opcao != 0:
        print("1 - Inserir um produto")
        print("2 - Excluir um produto")
        print("3 - Listar os produtos")
        print("4 - Consultar o preco de um produto pelo codigo")
        print("0 - Encerrar programa")

        opcao = int(input("Digit uma opcao: "))

        if opcao == 1:
            insere_produto(produtos)
        elif opcao == 2:
            if(not verificaListaVazia(produtos)):
                excluiProduto(produtos)
            else:
                print("A lista de produtos esta vazia!")
        elif opcao == 3:
            if(not verificaListaVazia(produtos)):
                listarProdutos(produtos)
            else:
                print("A lista de produtos esta vazia!")
        elif opcao == 4:
            if(not verificaListaVazia(produtos)):
                consultarProduto(produtos)
            else:
                print("A lista de produtos esta vazia!")
        elif opcao == 0:
            print("Programa encerrado")
        else:
            print("Opcao invalida! Tente novamente")

def verificaListaVazia(produtos):
    return len(produtos) == 0

def insere_produto(produtos):
    id = input("Digite o codigo do produto: ")
    if validaCodigo(id):
        nome = input("Digite o nome do produto: ").capitalize()
        preco = float(input("Digite o preco do produto: "))

        produto = {"id": id, "nome": nome, "preco": preco}
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")
    else:
        print("O codigo do produto deve ter um tamanho de 13 caracteres e deve ser numerico. Tente novamente")

def excluiProduto(produtos):
    id = input("Digite o codigo do produto: ")
    
    for produto in produtos:
        if(produto["id"] == id):
            produtos.remove(produto)
            print("produto removido com sucesso!")
            break
    else:
        print("Produto nao encontrado...")

def listarProdutos(produtos):
    lista_ordenada = sorted(produtos, key=lambda x: x["preco"])

    print("### Lista de produtos ###")
    for i in range (0, len(lista_ordenada), 10):
        segmento = lista_ordenada[i:i + 10]

        for produto in segmento:
            print("--------------------------------------")
            print("Codigo: " + produto["id"])
            print("Produto: " + produto["nome"])
            print(f"Preco: {produto['preco']:.2f}" )
        print("--------------------------------------")
        input("Tecle enter para continuar...")

def consultarProduto(produtos):
    id = input("Digite o codigo do produto: ")
    for produto in produtos:
        if(produto["id"] == id):
            print("--------------------------------------")
            print("Produto: " + produto["nome"])
            print(f"Preco: {produto['preco']:.2f}")
            print("--------------------------------------")
            return
    print("Produto nao encontrado")

def validaCodigo(codigo):
    if len(codigo) != 13:
        return False
    elif not codigo.isdigit():
        return False
    return True


if __name__ == "__main__":
    main()


