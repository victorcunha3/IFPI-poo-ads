'''Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual,
altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela,
calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).'''



class Bicicleta():
    def __init__(self,vel_atual,altura_cela,calibrar_pneus):
        self.vel_atual = vel_atual
        self.altura_cela = altura_cela
        self.calibrar_pneus = calibrar_pneus
        self.vel_max = 20
        self.altura_max_cela = 12
        self.calibragem_max = 15
    
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
bicy.regular_cela()
print(bicy.altura_cela)
bicy.calibrar_pneus_f()
print(bicy.calibrar_pneus)
bicy.pedalar_bicicleta()
print(bicy.vel_atual)
#bicy.frear_bicicleta()
#print(bicy.vel_atual)


