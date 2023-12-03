from AnaliseDadosABS import AnaliseDados

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

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
        print("Mediana:", sorted_lista[meio])

    def mostraMenor(self):
        print("Menor elemento:", min(self.__lista))

    def mostraMaior(self):
        print("Maior elemento:", max(self.__lista))

    def __str__(self):
        return ", ".join(self.__lista)

    def mostraMaior(self):
        print("Maior elemento:", max(self.__lista))
   
    def __str__(self):
        pass