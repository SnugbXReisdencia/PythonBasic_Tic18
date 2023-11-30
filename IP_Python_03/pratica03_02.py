import json

def salvar_lista_tarefas(arquivo, lista):
    with open(arquivo, 'w') as file:
        json.dump(lista, file)

def carregar_lista_tarefas(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
arquivo_tarefas = 'tarefas02.json'

def main():    

    lista = carregar_lista_tarefas(arquivo_tarefas)

    while True:
        print('1 - Inserir um novo funcionario')
        print('2 - Reajuste do salario do funcionario')
        print('3 - Listar todos os funcionarios')
        print('4 - Consultar os dados do funcionario através do RG.')
        print('5 - Sair')
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            AddFuncionario(lista)
            salvar_lista_tarefas(arquivo_tarefas, lista)

        elif opcao == 2:
            if not Verifica_vazio(lista):
                Reajusta_dez_porcento(lista)
                # salvar_lista_tarefas(arquivo_tarefas, lista)

            else:
                print("----lista vazia----")   
        elif opcao == 3:
            if not Verifica_vazio(lista):
                ListaFuncionario(lista)
            else:
                print("----lista vazia----")  
        # elif opcao == 4:
        #     if not verifica_vazio(lista):
        #         consultarPreco(lista)
        #     else:
        #         print("----lista vazia----") 
        # elif opcao == 5:
        #     break
        else:
            print('Opção inválida')

    print('Fim do programa')


def AddFuncionario(Lista: list):
    funcionario: dict = {}
    try:
        funcionario= {
            "nome" : input("Nome do funcionario: "),
            "sobreNome" : input("SobreNome do funcionario: "),
            "dataNasc" : input("Data de nascimento do funcionario: "),
            "rg" : input("RG do funcionario: "),
            "anoAdmissao" : input("Admissao do funcionario: "),
            "salario":float(input("Salario do funcionario: "))
        }

        if not VerificaFuncionario(Lista, funcionario):
            Lista.append(funcionario)
        else:
            print("Funcionario já está cadastrado")    

    except Exception as e:
        print("Erro ",e )



def VerificaFuncionario(Lista: list, funcionario_novo: dict):
    for i in range(len(Lista)):
        if Lista[i]['rg'] == funcionario_novo['rg']:
            return True
        
    return False

def ListaFuncionario(Lista: list):
    print("-------ListaFuncionario-------")
    for funcion in Lista:
        print(f'Nome: {funcion["nome"]} \nSobreNome: {funcion["sobreNome"]}\nData: {funcion["dataNasc"]} \
              \nRG: {funcion["rg"]} \nAno Admissao: {funcion["anoAdmissao"]} \nSalario: {funcion["salario"]}')


def Reajusta_dez_porcento(lista: list):
    for item in lista:
        aumento = item["salario"] * 0.10
        item["salario"] += aumento
        salvar_lista_tarefas(arquivo_tarefas, item)
        


def Verifica_vazio(lista_: list):
    return len(lista_) == 0

if __name__ == "__main__":
    main()