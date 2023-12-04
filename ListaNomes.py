from AnaliseDadosABS import AnaliseDados

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        
    def entradaDeDados(self):
        n = int(input("Quantidade de nomes: "))
        for _ in range(n):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        if len(sorted_lista) % 2 == 0:  # Se o número de elementos for par
            print("Mediana:", sorted_lista[meio - 1])  # Imprime o primeiro dos dois nomes em ordem alfabética
        else:
            print("Mediana:", sorted_lista[meio])

    def mostraMenor(self):
        print("Menor elemento:", min(self.__lista))

    def mostraMaior(self):
        print("Maior elemento:", max(self.__lista))
    def listarEmOrdem(self):
        print("Lista em ordem alfabética:", sorted(self.__lista)) 
    def __str__(self):
        print(", ".join(self.__lista))
    
    
# if __name__ == "__main__":
#     sls = ListaNomes()
#     sls.entradaDeDados()
#     sls.mostraMediana()
#     sls.mostraMenor()
#     sls.mostraMaior()
#     sls.listarEmOrdem()
#     sls.__str__()