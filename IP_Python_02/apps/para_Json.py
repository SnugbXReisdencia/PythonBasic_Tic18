import os
import json

class Repositorio:
    def __init__(self, diretorio: str, nome: str):
        self.diretorio = os.path.join(os.path.dirname(__file__), diretorio)
        self.nome = nome
        os.makedirs(self.diretorio, exist_ok=True)

    def load(self):
        try:
            with open(f'{self.diretorio}/{self.nome}.json', 'r', encoding='utf-8') as fd:
                return json.load(fd)
        except:
            return []

    def saveTarefa(self, new_tarefa):
        tarefas = self.load()
        tarefas.append(new_tarefa)
        with open(f'{self.diretorio}/{self.nome}.json', 'w', encoding='utf-8') as fd:
            json.dump(tarefas, fd, ensure_ascii=False, indent=True)

    def AtualizaBD(self, Lista):
        with open(f'{self.diretorio}/{self.nome}.json', 'w', encoding='utf-8') as fd:
            json.dump(Lista, fd, ensure_ascii=False, indent=True)

if __name__ == "__main__":
    # bd = Repositorio("rep", "tarefasBd")
    # tarafas = bd.load()
    # tarafas.append({"Descrição": "teste" , "ID": 1, "status": "[ ]"})
    # bd.AtualizaBD(tarafas)
    pass
