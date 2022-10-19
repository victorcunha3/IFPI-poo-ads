
class Pessoa():
    def __init__(self,nome,idade,peso,altura,sexo):
        self.nome = nome
        self.__idade = idade 
        self.peso = peso
        self.altura = altura
        self.__sexo = sexo
        self.__estado = 'vivo'
        self.estado_civil = 'solteiro'
        self.conjuge = None
    #encapsulamento IDADE
    @property
    def idade (self):
        return self.__idade
    @idade.setter
    def idade (self,valor):
        print('nao permitido')
    
    #encapsulamento ESTADO
    @property
    def estado (self):
        return self.__estado
    @estado.setter
    def estado (self,valor):
        print('nao é possivel alterar o estado')
    
    #encapsulamento SEXO
    @property
    def sexo (self):
        return self.__sexo
    @sexo.setter
    def sexo (self,valor):
        print('nao e possivel alterar o sexo')


        
    def envelhecer(self):
        if self.estado == 'vivo' and self.idade < 21:
            self.idade = self.idade + 1
            self.altura = self.altura + 0.05
    
    def engordar(self,valor=None):
        if valor == None:
            self.peso = self.peso + 1
        else:
            self.peso = self.peso + valor
    def emagrecer(self,valor=None):
        if valor == None:
            self.peso = self.peso - 1
        else:
            self.peso = self.peso - valor

    def crescer(self,valor=None):
        if self.idade <=21 and valor == None:
            self.altura = self.altura + 0.05
        elif self.idade <=21:
            self.altura = self.altura + valor
        else:
            print('a idade é maior do que 21 anos')
            
    def casar(self,conjuge):
        if self.estado_civil == 'casado':
            print('você nao pode casar novamente')
        elif self.idade < 18:
            print('pessoas menores de idade nao podem se casar')
        elif conjuge.idade < 18:
            print(f'o {conjuge.nome} nao pode casar pois é menor de idade')
        else:
            self.estado_civil = 'casado'
            print('casado')
    
    def morrer(self):
        self.estado = 'morto'   


'''pess1 = Pessoa('julia',15,55.1,1.56,'F')
pess1.envelhecer()
pess1.sexo = 'M'
pess1.idade = 15
pess1.estado = 'morto'
print(pess1.idade)
print(pess1.altura)
pess1.engordar()
print(pess1.peso)
pess1.emagrecer()
print(pess1.peso)
pess1.crescer()
pess1.casar()
pess1.morrer()
print(pess1.idade)'''

print('============Maria=============')
maria = Pessoa('Maria',5,20,1.00,'F')
maria.idade = 10
maria.envelhecer()
print(f'Maria está está com {maria.idade} anos e {maria.altura:.2f}cm de altura')
maria.morrer()

print('============João============')
joao = Pessoa('Joao',12,40,1.40,'M')

print('============Julia==========')
julia = Pessoa('Julia',30,65,1.70,'F')

print('==========Carlos=========')
carlos = Pessoa('Carlos',2,11,0.80,'M')

print('==========Bia==========')
bia = Pessoa('Bia',18,55,1.60,'F')
bia.casar(carlos)

print('==========Pedro===========')
pedro = Pessoa('Pedro',22,65,1.70,'M')
pedro.crescer(0.02)
pedro.casar(julia)
pedro.casar(bia)


print('=============Jonas============')
jonas = Pessoa('Jonas',34,70,1.80,'M')
jonas.casar(julia)
