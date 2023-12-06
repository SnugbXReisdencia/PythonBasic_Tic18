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
            sorted_lista = sorted(self.__lista)
            meio = len(sorted_lista) // 2
            print("Mediana:", sorted_lista[meio])
        except:
            print('Insira um Nome a Lista Primeiro!')   
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
    def modificar_datas(self):
        print("############ Iterador filter (Modificação de Datas) ##########")
        for i in range(len(self.__lista)):
            if self.__lista[i].ano < 2019:
                self.__lista[i].dia = 1
        print("Datas modificadas:", self.__str__())
    
if __name__ == "__main__":
    sls = ListaNomes()
    sls.entradaDeDados()
    sls.mostraMediana()
    sls.mostraMenor()
    sls.mostraMaior()
    sls.listarEmOrdem()
    sls.__str__()