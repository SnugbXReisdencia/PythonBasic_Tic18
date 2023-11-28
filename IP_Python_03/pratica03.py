
def main():

    lista = []

    while True:
        print('1 - Inserir um novo produto')
        print('2 - Excluir um produto cadastrado')
        print('3 - Listar todos os produtos com seus respectivos códigos e preços')
        print('4 - Consultar o preço de um produto através de seu código.')
        print('5 - Sair')
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            addProduto(lista)
        elif opcao == 2:
            if not verifica_vazio(lista):
                removeProduto(lista)
            else:
                print("----lista vazia----")   
        elif opcao == 3:
            if not verifica_vazio(lista):
                listarProdutos(lista)
            else:
                print("----lista vazia----")  
        elif opcao == 4:
            if not verifica_vazio(lista):
                consultarPreco(lista)
            else:
                print("----lista vazia----") 
        elif opcao == 5:
            break
        else:
            print('Opção inválida')

    print('Fim do programa')


def addProduto(lista_: list):
    try:
        id_ = input('Digite o codigo do produto: ')
        if validaCod(id_):
            produto = {
                "id": str(id_).zfill(13),
                "nome": input('Digite o nome do produto ').capitalize(),
                "preco": float(input('Digite o preço  produto: '))
            }

            lista_.append(produto)
            print("-----Produto adicionado com sucesso.-----")
        else:
            print("-----tamanho do codigo invalido, tamanho correto 13.-----")    
    except Exception as e:
        print("Erro ",e ) 

  
def removeProduto(lista_: list):
    try:
        cod_ = input('Digite o codigo para remoção do produto: ')
        for produto in lista_:
            if produto["id"] == cod_:
                lista_.remove(produto)
                print("-----Remoção do produto realizado com sucesso.-----")   
                break 
        else:
            print("----Produto não encontrado----")    
    except Exception as e:
        print("Erro ",e ) 

def buscar_codigo(lista_: list, codigo_: str):
    for i in range(len(lista_)):
        if lista_[i]["id"] == codigo_:
            return True

    return False

def listarProdutos(lista_: list):

    print("Produtos ordenados por preço em ordem crescente:")
    produto_ordenados = sorted(lista_, key=lambda x: x["preco"])
    for produto in produto_ordenados:
        print("<----------------->")
        print(f"Código: {produto['id']}, \nNome: {produto['nome']}, \nPreço: {produto['preco']}")


def consultarPreco(lista_: list):
    codigo = input('Digite o código do produto para consultar o preço: ')
    for produto in lista_:
        if produto["id"] == codigo:
            print("--------------------------------")
            print(f"Produto: {produto['nome']} \nPreço: {produto['preco']}")
            return

    print(f'Produto com código {codigo} não encontrado.')   

def validaCod(cod: str):
    if len(cod) > 13:
        return False
    return True

def verifica_vazio(lista_: list):
    return len(lista_) == 0
