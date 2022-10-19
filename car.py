'''1. Utilizando a linguagem python, implemente a classe carro de acordo com as especificações
vistas em
sala de aula:
Métodos:
ligar() : este método deverá mudar o estado do carro para: “ligado” e imprimir este estado.
Desligar(): este método deverá mudar o estado do carro para: “desligado” e o carro deve
parar, para isto
você deverá chamar o método parar(). Imprimir o estado do carro.
Parar(): este método deverá mudar a velocidade atual do carro para 0 (zero). Imprimir a
mensagem: “carro parado”.
Acelerar(valor): este método deverá mudar a velocidade atual do carro para o valor que está
no
parâmetro. O carro só pode acelerar se ele estiver ligado (fazer a condição). Fazer a condição
para que a
velocidade atual não ultrapasse a velocidade máxima do carro. Imprimir a velocidade atual do
carro.'''

class Carro():
    #ATRIBUTOS
    def __init__(self,nome, ano, cor, vel_atual,vel_max):
        self.__nome = nome
        self.__ano = ano
        self.__cor = cor
        self.vel_max = vel_max
        self.vel_atual = vel_atual
        self.estado = False

    #ENCAPSULAMENTO
    @property
    def nome (self):
        return self.__nome
    @nome.setter
    def nome (self,valor):
        print('o nome do carro nao pode ser alterado')
    
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,valor):
        print('o ano de fabricao do caro nao pode ser alterado')

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self,valor):
        print('a cor do caro nao pode ser alterada')

    #METODOS
    def ligar_carro(self):
        self.estado = True
        print('o carro está ligado')

    def desligar_carro(self):
        if self.estado == True:
            self.estado = False
            self.vel_atual = 0
            print('o carro está desligado')
        else:
            print('o carro já está desliagdo')

    def parar_carro(self):
        if self.vel_atual > 0:
            self.vel_atual = 0
            print('o carro parou')
        elif self.vel_atual == 0:
            print('o carro já está parado')

    def acelerar_carro(self,velocidade=None):
        if self.estado == True and velocidade == None and self.vel_atual < self.vel_max:
            self.vel_atual = self.vel_atual + 1

        elif self.estado == True and velocidade < self.vel_max:
            self.vel_atual = velocidade
        
        elif self.estado == True and velocidade > self.vel_max:
            print('a velocidade do atributo precisa ser menor que 400')
        
        elif self.estado == False:
            print('o carro está desligado, impossivel acelerar')

#OBJETOS
carro1 = Carro('Fiat',1996,'branco',37,400)
carro1.nome = 'chevrolet'
carro1.ano = 10
carro1.cor = 'cinza'
carro1.ligar_carro()
carro1.acelerar_carro(600)
carro1.acelerar_carro(230)
print(carro1.vel_atual)
carro1.parar_carro()
print(carro1.vel_atual)
carro1.parar_carro()
carro1.desligar_carro()