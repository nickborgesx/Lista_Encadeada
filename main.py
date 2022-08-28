class _No:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None 

    def __str__(self): #Modo de 'Printagem' da No.
        proximo = f', {self.proximo}'
        if self.proximo is None:
            proximo = ''
        return f'{self.valor}{proximo}'

class ListaSimples:
    def __init__(self): #Lista
        self.inicio = None #ínicio da Lista
        self.tamanho = 0 #Tamanho da Lista
    
    def __str__(self): #Modo de 'Printagem' da Lista
        value_list = '['
        perc = self.inicio
        while perc.proximo:
            value_list += f'{perc.valor}, '
            perc = perc.proximo
        value_list += f'{perc.valor}]'
        return  value_list

    def adicionar(self, valor): #Adicionar 'No' sempre no final da lista
        no = _No(valor) #Criação do No
        if not self.inicio: #Se não houver um início
            self.inicio = no #O início liga ao No
        else:
            perc = self.inicio #Perc vai ao Inicio
            while perc.proximo is not None: #Se a próxima casa do perc não for None
                perc = perc.proximo #Perc vai para a próxima casa
            perc.proximo = no #Perc recebe o No
        self.tamanho += 1

    def remover_index(self, index): # Remover Index da lista
        if index >= self.tamanho or self.tamanho + index <0: #Se o index for maior que o tamanho ou a soma dos dois for menor que zero
            raise IndexError('Index não existente')
        elif index == 0: 
            self.inicio = self.inicio.proximo #O inicio vai começar da segunda casa
        else:
            perc = self.procurar_index(index-1) #Irá procurar o index (-1)
            perc.proximo = perc.proximo.proximo #Perc vai pegar uma casa a mais para ligar-se a lista.
        self.tamanho-=1
        return True
    
    def remover_item(self, valor): #Remover Item da lista
        if self.tamanho == 0:
            raise ValueError('Lista está vazia.')
        perc = self.inicio
        if perc.valor == valor: #Se for o início
            self.inicio = self.inicio.proximo #O inicio vai começar da segunda casa
            self.tamanho -= 1
            return
        while perc.proximo: #enquanto houver um próximo ele continua
            if perc.proximo.valor == valor:
                aux = perc.proximo #Aux será o apontador para o item da exclusão
                perc.proximo = aux.proximo #Liga o antecessor do Aux com o próximo do Aux
                self.tamanho -= 1
                return
            perc = perc.proximo
        raise ValueError('Não existe esse valor na lista.')
    
    def inserir(self,index,valor): #Inserir um No entre dois No's (elementos).
        no = _No(valor)
        if index >= self.tamanho: #Se não houver nada na lista
            self.adicionar(valor) #Criará um item no index 0
            return
        elif index == 0:
            no.proximo = self.inicio 
            self.inicio = no #No criado vai receber o inicio da lista
            self.tamanho += 1
        else:
            perc = self.inicio #Por o perc no inicio
            for i in range(index - 1): #Vai percorer toda a lista
                perc = perc.proximo
            no.proximo = perc.proximo
            perc.proximo = no
            self.tamanho += 1
            return

    def procurar_index(self, index): #Irá percorrer a lista até o index selecionado e irá retornar o valor.
        if index > self.tamanho or self.tamanho == 0: #Verificar se tem algo na lista
            raise IndexError('Não existe elementos na lista')
        elif index == 0:
            return self.inicio
        else:
            perc = self.inicio
            for i in range(index):
                perc = perc.proximo #Quando o valor do index for encontrado, ele irá retornar com os dados
            return perc
    
    def procurar_valor(self,index): #Irá percorrer a lista até o index selecionado e irá retornar o valor.
        if self.tamanho == 0: #Verificar se tem algo na lista
            raise IndexError('Não existe elementos na lista')
        if index == self.tamanho -1:
            return f' O valor do index selecionado é',self.inicio
        perc = self.inicio
        for i in range(index):
            perc = perc.proximo #Quando o valor do index for encontrado, ele irá retornar com os dados
        return f' O valor do index selecionado é ',perc.valor
    
    def editar_item(self, index, valor): #Criará um novo nó que irá substituir o item selecionado
        no = _No(valor) #Criação do No
        if index >= self.tamanho: #Verificar se a edição do Index está correta
            raise IndexError('Index não existente')
        elif index == 0: 
            self.inicio = self.inicio.proximo #No criado vai receber o inicio da lista
            no.proximo = self.inicio
            self.inicio = no
        else:
            perc = self.procurar_index(index-1)
            perc.proximo = perc.proximo.proximo
            no.proximo = perc.proximo
            perc.proximo = no
        return True

    def valor_repetido(self, valor): #Verificar quandas vezes o número selecionado foi repetido
        if self.tamanho == 0:
            raise ValueError('Lista está vazia.')
        cont = 0 #Contador de repetição
        perc = self.inicio #Perc no inicio
        if perc.valor == valor: #Verificar o primeiro Item se é o mesmo valor
            cont += 1
        while perc.proximo: #Se o valor da casa for o mesmo do valor a procurar irá aumentar em 1
            if perc.proximo.valor == valor:
                cont+=1
            perc = perc.proximo
        return f'O valor {valor} aparece {cont} vezes na lista.'

    def ordenamento_sort(self):
        for i in range(self.tamanho-1): #Fazer com todos os elementos da Lista
            inicio=self.inicio #Apontador 'Inicio' apontado para Inicio
            flag=inicio.proximo #Apotandor 'Flag' para próxima casa do Inicio
            aux=None #Apontador Auxiliador
            while flag: #
                if inicio.valor>flag.valor: #Enquando apontador inicio for maior que apontador flag
                    if aux == None:
                       aux = inicio.proximo
                       flag = flag.proximo
                       aux.proximo = inicio
                       inicio.proximo = flag
                       self.inicio = aux
                    else:   #Se o apontador auxiliador for menor que o apontador Inicio
                        temp = flag #( Temp > Auxiliadora de Apontador)
                        flag = flag.proximo
                        aux.proximo = inicio.proximo
                        aux=temp
                        temp.proximo = inicio
                        inicio.proximo = flag
                else:   #Regravamento da Lista
                    aux=inicio
                    inicio=flag
                    flag=flag.proximo
            i=i+1 #'Finalizador' do Processo



lista = ListaSimples()
print({lista.tamanho},' <-- Tamanho da Lista')
lista.adicionar(1)
lista.adicionar(2) 
lista.adicionar(3)
lista.adicionar(4)
print(lista)
print('-'*30)
lista.inserir(0, 6)
lista.remover_index(1)
lista.editar_item(0, 5)
lista.editar_item(2, 5)
lista.adicionar(5)
lista.remover_item(4)
print(lista)
print({lista.tamanho},' <-- Tamanho da Lista')
print(lista.valor_repetido(5))
lista.adicionar(3)
lista.adicionar(4)
lista.ordenamento_sort()
print(lista)
print({lista.tamanho},' <-- Tamanho da Lista')
print(lista.procurar_valor(0))

#OK
