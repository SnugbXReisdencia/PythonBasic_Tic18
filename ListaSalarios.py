from AnaliseDadosABS import AnaliseDados

class ListaSalarios(AnaliseDados):

    def __init__(self, lista = []):
        super().__init__(type(float))
        self.__lista = lista        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            num_elementos = int(input("Quantos elementos deseja adicionar à lista? "))
        except:
            print("Valor Passado Invalido. Tente novamente.")
            return
        for i in range(num_elementos):
            try:
                elemento = float(input(f"Digite o salário {i+1}: "))
            except:
                print("Erro ao adicionar Salario/os. Tente novamente.")
                print("Valor Passado Invalido !!")
                return
            self.__lista.append(elemento)
        
        

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return
        
        self.__lista.sort()

        n = len(self.__lista)
        if n % 2 == 0:
            mediana = (self.__lista[n // 2] + self.__lista[n // 2 - 1]) / 2
        else:
            mediana = self.__lista[n // 2]

        print(f"Mediana: {mediana:.2f}")
        

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return
        
        print(f"Menor: {min(self.__lista):.2f}")
        

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return
        print(f"Maior: {max(self.__lista):.2f}")
    
    def listarEmOrdem(self):
        '''
        Este método ordena a lista
        '''
        if not self.__lista:
            print("A lista está vazia.")
            return
        self.__lista.sort()
        
    def __str__(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        str = ""
        try:
            for i in self.__lista:
                str += f"{i:.2f}\n"
        except BaseException as e:
            for i in self.__lista:
                print("Erro typo: ", type(i))            
            print("Erro ao mostrar a lista: ", e)
        return str
    
    def rajust10(self):
        if not self.__lista:
            print("A lista está vazia.")
            return
        numeros = list(map(lambda x: float(x) * 1.1, self.__lista_salarios))
        self.__lista = numeros
        print("Folha de Pagamento Reajustado 10%")
        print(self.__str__())

#Fazer os testes
if __name__ == "__main__":
    sls = ListaSalarios()
    sls.entradaDeDados()
    sls.mostraMediana()
    sls.mostraMenor()
    sls.mostraMaior()
    print(sls.__str__())
    