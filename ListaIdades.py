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
        pass    
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass

    def __str__(self):
        pass