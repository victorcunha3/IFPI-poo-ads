'''Exercitando o processo de abstração, modele uma classe Relógio_Digital_Simples com seus estados e
comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus
atributos e execute os métodos criados. Recomendação: criar estados que possam ter seus valores alterados
por seus métodos.'''

import time
class Relogio:
    def __init__(self):
        self.hora=0
        self.minuto=0
        self.ligado=False

    def ajustar_hora(self,hora):
        self.hora = hora
    def ajustar_minuto(self,minuto):
        self.minuto = minuto
    def ligar_desligar(self):
        if self.ligado==False:
            self.ligado=True 
        else:
            self.ligado=False
    def que_horas_sao(self):
        h = self.hora
        m = self.minuto
        s = 0
        if self.ligado ==True:
            while True:
                print(f'{h}:{m}:{s}')
                time.sleep(1)
                s+=1
                if s==60:
                    s=0
                    m+=1
                    if m==60:
                        m=0
                        h+=1
                        if h>23:
                            h=0
                        else:
                            print ('Relógio desligado!')
r1 = Relogio()
r1.ligar_desligar()
r1.ajustar_hora(17)
r1.ajustar_minuto(49)
r1.que_horas_sao()
