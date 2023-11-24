from apps.app_Tarefas import *

if __name__ == "__main__":
    while True:
        limpar_console()
        match Menu():
            case 1:
                limpar_console()
                registro_tarefas(tarefas)
                pausa()
            case 2:
                limpar_console()
                concluir_tarefas(tarefas)
                pausa()
            case 3:
                limpar_console()
                editar_tarefas(tarefas)
                pausa()
            case 4:
                limpar_console()
                listar_tarefas(tarefas)
                pausa()
            case 0:
                limpar_console()
                print("Programa encerrado !!!")
                pausa()
                break
            case _:
                limpar_console()
                print("Opção indormada invalida !!!")
                pausa()
