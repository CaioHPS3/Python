#classes em python equivale a struct em C
#para declara uma classe vc usa o "class"
# podendo declarra outras variaveis la dentro
from calendar import c
from select import select


class Carro:
    velocida=0
    ligado=False
    cor=""
    preço=0,0
    

#criando uma instancia da classe que eu criei
c1=Carro
c2=Carro
c3=Carro

#add nas variaveis da classe
c1.velocida=200
c1.cor="vermelho"
c1.preço=10,5
c1.ligado=True

#últilizando
print(f"A velocidade do carro 1 e {c1.velocida}")
estado= "ligado" if c1.ligado else "desligado"
print(f"O carro esta {estado}")


class bolacha:
    nome=""
    sabor=""
    quat=0,0
    valor=0
    #vc pode criar varias funções dentro da classe para manipular o conteudo dela
    
    #definindo um METODO "função" contrutor "init" que vai me ajuda a armazena na declaração da instancia
    #self e uma declarção referenciando a propria classe já "s, q, v" são declarações genericas
    #q foi usada para receber os valores das variaveis da classe
    def __init__(self,n,s,q,v):
            self.nome=n
            self.sabor=s
            self.quat=q
            self.valor=v
    
    
# Essa METODO "função"  vai mostrar o conteudo armazenado
    def mostra(self):
        print(f"O nome da bolacha e {self.nome}")
        print(f"O valor da bolacha {self.nome} = {self.valor}")
        print(f"A quantidade de unidade da bolacha {self.nome} = {self.quat}")
        print(f"O sabor da bolacha {self.nome} = {self.sabor}")
#modifica o valor de bolacha   
    def novosabor(self, s):
        self.sabor=s
            
        

#o contrutor "init" ajuda e declara os valores direto
#comparar com a  classe Carro
negrito=bolacha("Negrito","chocolate", 20, 3.5)
negrito.mostra()
negrito.novosabor("morango")
negrito.mostra()


