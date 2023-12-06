import os

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
    print("6 - Modificar dia das datas  inferiores ao ano de 2019")
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

def percorre_nomes_e_salarios(nomes, salarios):
    if len(nomes) == 0 or len(salarios) == 0:
        print('As duas listas devem estar preenchidas!')
    elif len(nomes) != len(salarios):
        print('As duas listas devem ter o mesmo tamanho!')
    else:
        for n, s in zip(nomes, salarios):
            print(f'Nome: {n}, Salário: {s}')
    pause()

def modificarDatasAnterioresA2019(datas):
    if len(datas) == 0:
        print('Lista de datas vazia!')
        pause()
        return
    lista_modificada = filter(lambda data: data.ano < 2019, datas)
    for data in lista_modificada:
        data.dia = 1
    print('Datas modificadas com sucesso!')
    pause()



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
            percorre_nomes_e_salarios(nomes.lista, salarios.lista)
        elif opc == 6:
            modificarDatasAnterioresA2019(datas.lista)
        else:
            print("Opcão inválida")
            pause()
        

if __name__ == "__main__":
    main()