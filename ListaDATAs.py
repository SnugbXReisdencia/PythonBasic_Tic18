from AnaliseDadosABS import AnaliseDados
from Data import Data
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
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
        print('Menor data: ' + str(sorted(self.__lista)[0]))
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        print('Maior data: ' + str(sorted(self.__lista)[-1]))
    
    def __str__(self):
        listaDatasStr = ""
        for i in range(len(self.__lista)):
            listaDatasStr.append(str(self.__lista[i])+'\n')
        return listaDatasStr