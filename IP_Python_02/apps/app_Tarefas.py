import os

tarefas = []

def limpar_console():
    try:
        os.system('cls')
    except:
        os.system('clear')
def pausa():
    try:
        os.system('pause')
    except:
        input("Pressione <ENTER> para continuar...")
    

def Menu():
    print(10*"#"+f" Menu de Tarefas "+10*"#")
    print("1 - Registrar Tarefas")
    print("2 - Concluir Tarefa")
    print("3 - Editar Tarefa")
    print("4 - Listar Tarefa")
    print("0 - Sair do programa")
    try:
        return int(input("Informe uma das alternativas: "))
    except BaseException as e:
        print(f"Erro: {e}")
        print("Valor passado invalido tente novamente !!!")

def registro_tarefas(tarefas):
    print(10*"#"+f" Registrar Tarefas "+10*"#")
    tarefa = {}
    tarefa["Descrição"] = input("Descrição: ")
    tarefa["Descrição"].capitalize()
    tarefa["ID"] = len(tarefas) + 1
    tarefa["status"] = "[ ]"
    tarefas.append(tarefa)

def listar_tarefas(tarefas):
    print(10*"#"+f" Listar Tarefas "+10*"#")
    for tarefa in tarefas:
        print("ID: ", tarefa["ID"])
        if tarefa["status"] == "[ ]":
            print(f"Descrição: {tarefa['Descrição']} {tarefa['status']}")
        else:
            print(f"Descrição: {tarefa['Descrição']} {tarefa['status']}")

def concluir_tarefas(tarefas):
    print(10*"#"+f" Concluir Tarefas "+10*"#")
    id = int(input("ID da tarefa que deseja concluir: "))
    for i, val in enumerate(tarefas):
        if val["ID"] == id:
            if val["status"] != "[X]":
                val["status"] = "[X]"
                tarefas.pop(i)
                tarefas.insert(0, val)
                print("Tarefa concluída!")
                return
            else:
                print("Tarafa já foi concluida!!!")
                return
    
    print("Tarefa não encontrada !!")

def editar_tarefas(tarefas):
    print(10*"#"+f" Editar de Tarefas "+10*"#")
    id = int(input("ID da tarefa que deseja editar: "))
    for i, val in enumerate(tarefas):
        if val["ID"] == id:
            srt = input("Nova Descrição: ")
            opc = input("Deseja realmente alterar a Descrição: [Y/N] ")
            if opc == "y" or opc == "Y":
                val["Descrição"] = srt
                val["Descrição"].capitalize()
                print("Alterações Realizada!")
                return
            else:
                print("Alterações não salvas!")
                return
    print("Tarefa não encontrada !!")

if __name__ == "__main__":
    pass
