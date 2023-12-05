from AnaliseDadosABS import AnaliseDados

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = [] 
    
    def validar_idade(self, idade):
        '''
        Este método verifica o parâmetro idade,
        retornando um booleano ao comparar se o valor 
        é maior que zero.
        '''
        try:
            return idade > 0  
        except Exception as e:
            print("Error no metodo validar_idade: ", e)        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            Qtd = 0
            while Qtd <= 0: 
                Qtd = int(input("Quantos elementos a lista de idade terá ?"))
            
            for _ in range(Qtd):   
                add_idade = int(input("Digite a idade: "))
                if self.validar_idade(add_idade):
                    self.__lista.append(add_idade)
                else: 
                    raise ValueError("Idade Invalida.")   

        except Exception as e:
            print("Error no metodo entradaDeDado: ", e)
        finally:
            print("Lista de idades:", self.__lista)   
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        try:
            listaOrdenada = self.listarEmOrdem()
            mediana = listaOrdenada[int(len(listaOrdenada) / 2 - 1)] if len(self.__lista) % 2 == 0 else listaOrdenada[int(len(listaOrdenada) / 2)]
        except Exception as e:
            print("Error no metodo mostraMediana", e)
        finally:
            print(f'Idade mediana: {mediana}, De lista ordenado: {listaOrdenada}') 
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        try:
            menor_numero = min(self.__lista, default=None)
        except Exception as e:
            print("Error no metodo mostraMenor", e)
        finally:
            print("Menor número da lista:", menor_numero) 
    
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        try:
            maior_numero = max(self.__lista, default=None)
        except Exception as e:
            print("Error no metodo mostraMaior", e)
        finally:
            print("Maior número da lista:", maior_numero) 


    def __str__(self):
        try:
            for num in self.__lista:
                print(f'-> {num}')
        except Exception as e:
            print("Error no metodo __str__", e)
            
    def listarEmOrdem(self):
        try:
            if not self.__lista:
                raise ValueError("A lista está vazia.")
            
            return sorted(self.__lista)
    
        except Exception as e:
            print("Erro ao listar em ordem:", e)
            return None

def main():
    Idade = ListaIdades()
    
    Idade.entradaDeDados()
    Idade.mostraMediana()
    Idade. mostraMenor()
    Idade. mostraMaior()
    Idade.__str__()


if __name__ == "__main__":
    main()