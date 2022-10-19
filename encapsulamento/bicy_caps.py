class Bicicleta():
    def __init__(self,vel_atual,altura_cela,calibrar_pneus):
        self.__vel_atual = vel_atual
        self.__altura_cela = altura_cela
        self.__calibrar_pneus = calibrar_pneus
        self.vel_max = 20
        self.altura_max_cela = 12
        self.calibragem_max = 15

    @property
    def vel_atual(self):
        return self.__vel_atual

    @vel_atual.setter
    def vel_atual(self,valor_1):
        if valor_1 > 0:
            self.__vel_atual = valor_1
        else:
            print('entre com um valor maior ou igual a  0')
    
    @property
    def altura_cela(self):
        return self.__altura_cela
    
    @altura_cela.setter
    def altura_cela(self,valor_2):
        if valor_2 > 0:
            self.__altura_cela = valor_2
        else:
            print('entre com um valor maior ou igual a  0')

    @property
    def calibrar_pneus(self):
        return self.__calibrar_pneus
    
    @calibrar_pneus.setter
    def calibrar_pneus(self,valor_3):
        if valor_3 > 0:
            self.__calibrar_pneus = valor_3
        else:
            print('entre com um valor maior ou igual a  0')


    def regular_cela(self):
        if self.vel_atual == 0 and self.altura_cela <= self.altura_max_cela:
            self.altura_cela = self.altura_cela + 1
        else:
            print('a bicicleta esta em movimento, nao ha como regular a cela')

    
    def calibrar_pneus_f(self):
        if self.vel_atual == 0 and self.calibrar_pneus <= self.calibragem_max:
            self.calibrar_pneus = self.calibrar_pneus + 1
        else:
            print('a bicicleta esta em movimento, nao ha como calibrar os pneus')
    
    def pedalar_bicicleta(self):
        self.vel_atual = self.vel_atual + 1

    def frear_bicicleta(self):
        self.vel_atual = 0
    
    


bicy = Bicicleta(0,4,4)
bicy.vel_atual = -15
bicy.regular_cela()
print(bicy.altura_cela)
bicy.calibrar_pneus_f()
print(bicy.calibrar_pneus)
bicy.pedalar_bicicleta()
print(bicy.vel_atual)
bicy.regular_cela()
#bicy.frear_bicicleta()
#print(bicy.vel_atual)
