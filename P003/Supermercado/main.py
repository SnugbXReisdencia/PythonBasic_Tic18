# main.py

from funcoes import (
    inserir_produto,
    excluir_produto,
    listar_produtos,
    consultar_preco,
)

def main():
    produtos = []

    while True:
        print("\n--- Menu ---")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                inserir_produto(produtos)
            case 2:
                excluir_produto(produtos)
            case 3:
                listar_produtos(produtos)
            case 4:
                consultar_preco(produtos)
            case 0:
                print("Saindo do programa. Até mais!")
                return False
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
