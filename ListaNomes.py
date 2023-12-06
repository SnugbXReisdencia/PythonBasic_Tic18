from AnaliseDadosABS import AnaliseDados

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []     

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, lista):
        self.__lista = lista
           
        self.__lista = []  
    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self, lista):
        self.__lista = lista              
    def entradaDeDados(self):
        try:
            n = int(input("Quantidade de nomes que deseja adicionar à lista?: "))         
        except:
            print("Valor Passado Invalido. Tente novamente.")
            return
        for _ in range(n):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        try:
            if not self.__lista:
                raise ValueError("Lista vazia. Impossível calcular mediana.")
            sorted_lista = sorted(self.__lista)
            meio = len(sorted_lista) // 2
            print("Mediana:", sorted_lista[meio])
        except ValueError as e:
            print(str(e)) 
    def mostraMenor(self):
        try:
            print("Menor elemento:", min(self.__lista))
        except:
            print('Insira um Nome a Lista Primeiro!')
    def mostraMaior(self):
        try:
            print("Maior elemento:", max(self.__lista))
        except:
            print('Insira um Nome a Lista Primeiro!')
    def listarEmOrdem(self):
        try:
            print("Lista em ordem alfabética:", sorted(self.__lista)) 
        except:
            print('Insira um Nome a Lista Primeiro!')    
    def __str__(self):
        print(", ".join(self.__lista))
    
    
if __name__ == "__main__":
    sls = ListaNomes()
    sls.entradaDeDados()
    sls.mostraMediana()
    sls.mostraMenor()
    sls.mostraMaior()
    sls.listarEmOrdem()
    sls.__str__()