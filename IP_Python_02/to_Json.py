import os
import json

class Repositorio:
    def __init__(self, diretorio:str, nome:str):
        self.diretorio = diretorio
        self.nome = nome
        os.makedirs(self.diretorio, exist_ok=True)

    def load(self):
        with open(f'{self.diretorio}/{self.nome}.json', 'r', encoding='utf-8') as fd:
            return json.load(fd)

    def saveCliente(self, new_client):
        clientes = self.load()
        clientes.append(new_client)
        with open(f'{self.diretorio}/{self.nome}.json', 'w', encoding='utf-8') as fd:
            json.dump(clientes, fd, ensure_ascii=False, indent=True)

    def AtualizaBD(self, Lista):
        with open(f'{self.diretorio}/{self.nome}.json', 'w', encoding='utf-8') as fd:
            json.dump(Lista, fd, ensure_ascii=False, indent=True)

