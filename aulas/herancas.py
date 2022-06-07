#   Herança em python e dado quando uma classe erda caracteristicas de outras
#   classe tendo a classe pai e a classe filho que erda toda as carcteristica do
#   pai mais as suas proprias

class NPC: #Base, pai, Suber
    def __init__(self, nome, time, forca, municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=200
    def info(self):
        print(f"nome={self.nome}")
        print(f"time={self.time}")
        print(f"força={self.forca}")
        print(f"time={self.municao}")
        print(f"Vivo={self.vivo}")
        print(f"enegia={self.energia}")
        print("____________________________")
class soldado(NPC):
    def __init__(self, nome, time):
        self.municao=200
        self.forca=200
        #chamando o contrutor da classe pai
        #super tem a capacidade de invocar caracteristica da classe pai
        super().__init__(nome, time, self.forca, self.municao)
class Guarda(NPC):
    def __init__(self, nome, time):
        self.municao=100
        self.forca=150
        #chamando o contrutor da classe pai
        super().__init__(nome, time, self.forca, self.municao)
class Elite(NPC):
    def __init__(self, nome, time):
        self.municao=350
        self.forca=250
        #chamando o contrutor da classe pai
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()
            
s1=Guarda("Olho vivo", 1)
s2=Elite("Osvaldo", 2)
s3=soldado("Olho vivo", 1)
s4=Elite("Douglas", 0)
s1.info()
s2.info()
s3.info()
s4.inf()