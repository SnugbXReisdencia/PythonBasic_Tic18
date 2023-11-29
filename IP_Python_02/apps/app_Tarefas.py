import os
import para_Json as Tj

bd = Tj.Repositorio("rep", "tarefasBd")

def limpar_console():
    try:
        if os.system('clear') != 0:
            os.system('cls')
        
    except os.error:
        pass
def pausa():
    try:
        input("Pressione <ENTER> para continuar...")
    except:
        pass
    

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

def registro_tarefas():
    try:
        tarefas = bd.load()
    except:
        tarefas = []
    print(10*"#"+f" Registrar Tarefas "+10*"#")
    tarefa = {}
    tarefa["Descrição"] = input("Descrição: ")
    tarefa["Descrição"].capitalize()
    tarefa["ID"] = len(tarefas) + 1
    tarefa["status"] = "[ ]"
    bd.saveTarefa(tarefa)

def listar_tarefas():
    try:
        tarefas = bd.load()
    except:
        pass
    print(10*"#"+f" Listar Tarefas "+10*"#")
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada !!!")
        return
    for tarefa in tarefas:
        print("ID: ", tarefa["ID"])
        if tarefa["status"] == "[ ]":
            print(f"Descrição: {tarefa['Descrição']} {tarefa['status']}")
        else:
            print(f"Descrição: {tarefa['Descrição']} {tarefa['status']}")

def concluir_tarefas():
    try:
        tarefas = bd.load()
    except:
        pass
    print(10*"#"+f" Concluir Tarefas "+10*"#")
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada !!!")
        return
    try:
        id = int(input("ID da tarefa que deseja concluir: "))    
    except:
        print("ID invalido !!!")
        return
    for i, val in enumerate(tarefas):
        if val["ID"] == id:
            if val["status"] != "[X]":
                val["status"] = "[X]"
                tarefas.pop(i)
                tarefas.insert(0, val)
                print("Tarefa concluída!")
                bd.AtualizaBD(tarefas)
                return
            else:
                print("Tarafa já foi concluida!!!")
                return
    
    print("Tarefa não encontrada !!")

def editar_tarefas():
    try:
        tarefas = bd.load()
    except:
        pass
    print(10*"#"+f" Editar de Tarefas "+10*"#")
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada !!!")
        return
    try:
        id = int(input("ID da tarefa que deseja editar: "))    
    except:
        print("ID invalido !!!")
        return
    for val in tarefas:
        if val["ID"] == id:
            srt = input("Nova Descrição: ")
            opc = input("Deseja realmente alterar a Descrição: [Y/N] ")
            if opc == "y" or opc == "Y":
                val["Descrição"] = srt
                val["Descrição"].capitalize()
                print("Alterações Realizada!")
                bd.AtualizaBD(tarefas)
                return
            else:
                print("Alterações não salvas!")
                return
    print("Tarefa não encontrada !!")

def main():
    while True:
        limpar_console()
        match Menu():
            case 1:
                limpar_console()
                registro_tarefas()
                pausa()
            case 2:
                limpar_console()
                concluir_tarefas()
                pausa()
            case 3:
                limpar_console()
                editar_tarefas()
                pausa()
            case 4:
                limpar_console()
                listar_tarefas()
                pausa()
            case 0:
                limpar_console()
                print("Programa encerrado !!!")
                pausa()
                break
            case _:
                limpar_console()
                print("Opção informada invalida !!!")
                pausa()

if __name__ == "__main__":
    main()
    

