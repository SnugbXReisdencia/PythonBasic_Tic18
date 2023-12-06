from AnaliseDadosABS import AnaliseDados
from Data import Data
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, lista):
        self.__lista = lista

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            quantidade = int(input('Quantas datas a lista terá?'))
        except:
            print('Valor inválido!')
            return
        for i in range(quantidade):
            print('Data nº' + str(i+1) + ':')
            try:
                dia = int(input('Dia: '))
                mes = int(input('Mes: '))
                ano = int(input('Ano: '))
                data = Data(dia, mes, ano)
                self.__lista.append(data)
            except:
                print('Valor inválido!')
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if not self.__lista:
            print('A lista  está vazia!')
            return
        listaOrdenada = sorted(self.__lista)
        if len(self.__lista) % 2 == 0:
            mediana = listaOrdenada[int(len(listaOrdenada) / 2 - 1)]
        else:
            mediana = listaOrdenada[int(len(listaOrdenada) / 2)]
        print('Mediana da lista de datas = ' + str(mediana))
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if not self.__lista:
            print('A lista  está vazia!')
            return
        print('Menor data: ' + str(sorted(self.__lista)[0]))
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if not self.__lista:
            print('A lista  está vazia!')
            return
        print('Maior data: ' + str(sorted(self.__lista)[-1]))
    
    def __str__(self):
        if not self.__lista:
            print('A lista  está vazia!')
        for data in self.__lista:
            print(data)
        

    def listarEmOrdem(self):
        if not self.__lista:
            print('A lista  está vazia!')
            return
        for data in sorted(self.__lista):
            print(data)