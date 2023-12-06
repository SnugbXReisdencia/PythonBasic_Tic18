import os
from Data import Data

from ListaNomes import ListaNomes
from ListaDATAs import ListaDatas
from ListaSalarios import ListaSalarios
from ListaIdades import ListaIdades

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Pressione <ENTER> para continuar...")

def menu():
    limpar_tela()
    print("############ MENU ##########")
    print("1 - Lista de nome")
    print("2 - Lista de idade")
    print("3 - Lista de salario")
    print("4 - Lista de data")
    print("5 - Pecorre a lista de nomes e salarios")
    print("6 - Pecorre a lista de datas ano anterior a 2019 modifica o dia para 1ª dia do mes")
    print("0 - Sair")
    try:
        opc = int(input("Escolha uma opção: "))
    except:
        opc = -1
    return opc

def menuNome():
    limpar_tela()
    print("############ Lista de nome ##########")
    print("1 - Adicionar nome")
    print("2 - Listar nome")
    print("3 - Mediana de nome")
    print("4 - Menor nome")
    print("5 - Maior nome")
    print("0 - Voltar")
    try:
        opc = int(input("Escolha uma opção: "))
    except:
        opc = -1
    return opc

def menuIdade():
    limpar_tela()
    print("############ Lista de idade ##########")
    print("1 - Adicionar idade")
    print("2 - Listar idade")
    print("3 - Mediana de idade")
    print("4 - Menor idade")
    print("5 - Maior idade")
    print("0 - Voltar")
    try:
        opc = int(input("Escolha uma opção: "))
    except:
        opc = -1
    return opc

def menuSalario():
    limpar_tela()
    print("############ Lista de salario ##########")
    print("1 - Adicionar salario")
    print("2 - Listar salario")
    print("3 - Mediana de salario")
    print("4 - Menor salario")
    print("5 - Maior salario")
    print("6 - Calcular o valor da folha com um reajuste de 10%")
    print("0 - Voltar")
    try:
        opc = int(input("Escolha uma opção: "))
    except:
        opc = -1
    return opc

def menuData():
    limpar_tela()
    print("############ Lista de data ##########")
    print("1 - Adicionar data")
    print("2 - Listar data")
    print("3 - Mediana de data")
    print("4 - Menor data")
    print("5 - Maior data")
    print("0 - Voltar")
    try:
        opc = int(input("Escolha uma opção: "))
    except:
        opc = -1
    return opc

def gerenciaNomes(lst):
    while True:
        opc = menuNome()
        if opc == 0:
            break
        elif opc == 1:
            lst.entradaDeDados()
        elif opc == 2:
            lst.__str__()
        elif opc == 3:
            lst.mostraMediana()
        elif opc == 4:
            lst.mostraMenor()
        elif opc == 5:
            lst.mostraMaior()
        else:
            print("Opcão inválida")
        pause()
    return lst

def gerenciaIdades(lst):
    while True:
        opc = menuIdade()
        if opc == 0:
            break
        elif opc == 1:
            lst.entradaDeDados()
        elif opc == 2:
            lst.__str__()
        elif opc == 3:
            lst.mostraMediana()
        elif opc == 4:
            lst.mostraMenor()
        elif opc == 5:
            lst.mostraMaior()
        else:
            print("Opcão inválida")
        pause()
    return lst

def gerenciaSalarios(lst):
    while True:
        opc = menuSalario()
        if opc == 0:
            break
        elif opc == 1:
            limpar_tela()
            print("############ Adicionar Salario/os ##########")
            lst.entradaDeDados()
            pause()
        elif opc == 2:
            limpar_tela()
            print("############ Lista de Salario ##########")
            print("Salarios:")
            if lst.__str__() != None:print(lst.__str__())
            pause()
        elif opc == 3:
            limpar_tela()
            print("############ Mediana ##########")
            lst.mostraMediana()
            pause()
        elif opc == 4:
            limpar_tela()
            print("############ Menor Salario ##########")
            lst.mostraMenor()
            pause()
        elif opc == 5:
            limpar_tela()
            print("############ Maior Salario ##########")
            lst.mostraMaior()
            pause()
        elif opc == 6:
            limpar_tela()
            print("############ Reajuste Folha de Pagamento ##########")
            lst.rajust10()
            pause()
        else:
            print("Opcão inválida")
            pause()
    return lst
        

def gerenciaData(lst):
    while True:
        opc = menuData()
        if opc == 0:
            break
        elif opc == 1:
            lst.entradaDeDados()
        elif opc == 2:
            lst.__str__()
        elif opc == 3:
            lst.mostraMediana()
        elif opc == 4:
            lst.mostraMenor()
        elif opc == 5:
            lst.mostraMaior()
        else:
            print("Opcão inválida")
        pause()

    return lst

def ListaDatasAnoAnterior2019(lst):
    #usando o filter para filtrar
    if len(lst) == 0:
        print("Lista vazia")
        pause()
        return
    lista_filtrada = filter(lambda data: data.ano < 2019, lst)
    print("Lista atualizada com o ano anterior a 2019 modificado para 1° dia do mes")
    #exibindo a lista filtrada com o ano anterior a 2019 modificado para 1° dia do mes
    lista_filtrada = list(
        map(lambda data: Data(1, data.mes, data.ano), lista_filtrada)
        )
    for data in lista_filtrada:
        print(data.__str__())
    pause()

def ListaNomesSalarios(listNomes, listSalarios):
    if len(listNomes) != len(listSalarios):
        print("As duas listas devem ter o mesmo tamanho")
        pause()
        return
    if len(listNomes) == 0:
        print("Lista de nomes vazia")
        pause()
        return
    if len(listSalarios) == 0:
        print("Lista de salarios vazia")
        pause()
        return
    if len(listNomes) == len(listSalarios):
        #usando o zip para Listar
        for nome, salario in zip(listNomes, listSalarios):
            print(f"Nome: {nome} | Salário: {salario}")
        
        pause()
        return
    else:
        print("As duas listas devem ter o mesmo tamanho")
        pause()
        return

def main():
    nomes = ListaNomes()
    idades = ListaIdades()
    salarios = ListaSalarios()
    datas = ListaDatas()
    while True:
        opc = menu()
        if opc == 0:
            break
        elif opc == 1:
            nomes = gerenciaNomes(nomes)
        elif opc == 2:
            idades = gerenciaIdades(idades)
        elif opc == 3:
            salarios = gerenciaSalarios(salarios)
        elif opc == 4:
            datas = gerenciaData(datas)
        elif opc == 5:
            ListaNomesSalarios(nomes.lista, salarios.lista)
        elif opc == 6:
            ListaDatasAnoAnterior2019(datas.lista)
        else:
            print("Opcão inválida")
            pause()
        

if __name__ == "__main__":
    main()