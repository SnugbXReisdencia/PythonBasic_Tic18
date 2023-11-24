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

def imprimir_tarefas(lista):
    print("\n########### Lista de Tarefas ###########\n")
    for tarefa in lista:
        status = "[]" if tarefa['status'] == False else "[X]"
        print(f"ID: {tarefa['id']}, Tarefa: {tarefa['tarefa']} {status}")

# Nome do arquivo para armazenar a lista de tarefas
arquivo_tarefas = 'tarefas.json'

# Carregar a lista de tarefas do arquivo
lista_tarefa = carregar_lista_tarefas(arquivo_tarefas)
i = len(lista_tarefa)

while True:
    print('1 - Adicionar tarefa')
    print('2 - Remover tarefa')
    print('3 - Listar tarefas')
    print('4 - Marcar uma tarefa como realizado')
    print('5 - Editar descrição da tarefa')
    print('0 - Sair')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        tarefa = {
            "id": i + 1,
            "tarefa": input('Digite a tarefa: ').capitalize(),
            "status": False
        }
        lista_tarefa.append(tarefa)
        i += 1
        salvar_lista_tarefas(arquivo_tarefas, lista_tarefa)
    elif opcao == 2:
        id_tarefa = int(input('Digite o ID da tarefa a ser removida: '))
        for tarefa in lista_tarefa:
            if tarefa['id'] == id_tarefa:
                lista_tarefa.remove(tarefa)
                salvar_lista_tarefas(arquivo_tarefas, lista_tarefa)
                break
        else:
            print('Tarefa não encontrada.')
    elif opcao == 3:
        imprimir_tarefas(lista_tarefa)
    elif opcao == 4:
        id_escolhido = int(input("Digite o ID da tarefa para ser marcada como realizado: "))
        for i in range(len(lista_tarefa)):
            if lista_tarefa[i]["id"] == id_escolhido:
                tarefa_selecionada = lista_tarefa[i]  # Armazena o elemento que será movido
                lista_tarefa.remove(lista_tarefa[i]) 
                tarefa_selecionada["status"] = True
                lista_tarefa.insert(0, tarefa_selecionada)
                print(f"Tarefa  marcada como realizada.")
                salvar_lista_tarefas(arquivo_tarefas, lista_tarefa)
                break
        else:
            print("Tarefa não encontrada.")
    elif opcao == 5:
        id_escolhido = int(input("Digite o ID da tarefa para editar a descrição: "))
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        for tarefa in lista_tarefa:
            if tarefa["id"] == id_escolhido:
                print(f"Descrição anterior: {tarefa['tarefa']}")
                tarefa["tarefa"] = nova_descricao.capitalize()
                print(f"Tarefa editada: {tarefa['tarefa']}")
                print("A tarefa foi editada com sucesso.")
                salvar_lista_tarefas(arquivo_tarefas, lista_tarefa)
                break
        else:
            print("Tarefa não encontrada.")
    elif opcao == 0:
        break
    else:
        print('Opção inválida')

print('Fim do programa')
