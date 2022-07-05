from ast import Num


class Pais:
    '''Construtor que inicialize o código, o nome e a dimensão do país'''
    def __init__(self, c, n, d):
        self.codigo=c
        self.nome=n
        self.populacao=0
        self.dimensao=d
        self.fronteira=[]
    '''Métodos de acesso (get/set) para as propriedades 
        código,nome, população e dimensão do país'''
    def setCodigo(self, cod):
        self.codigo=cod.upper()

    def setNome(self, nom):
        self.nome=nom.capitalize()

    def setPopul(self, num):
        self.populacao=num

    def setDimen(self, tam):
        self.dimensao=tam
        
    def get_Codigo(self):
        return self.codigo

    def get_Nome(self):
        return self.nome

    def get_Popul(self):
        return self.populacao

    def get_Dimen(self):
        return self.dimensao
    
    '''Um método que permita verificar se dois objetos representam
        o mesmo país. Dois países são iguais se tiverem o mesmo código;'''
    def comparaPais(self, codigo):
        if (self.codigo == codigo):
            print("Pais igual\n")
        else:
            print("Pais diferente\n")
    def paisesfront(self):
        p=""
        nome=""
        while (p != "não"):
            nome=str(input("Qual o pais que faz fontreira ?\n")).capitalize()
            self.fronteira.append(nome)
            p=(input("Mais algum pais ?\n"))
    ''' Um método que informe se outro país é 
        limítrofe do país querecebeu a mensagem'''
    def limitrofe(self, pais):
        if (pais in self.fronteira):
            print("Pais faz fronteira")
        else:
            print("Pais não faz frontera")
    ''' Um método que retorne a densidade populacional do país'''
    def densidade(self):
        return float(self.populacao/self.dimensao)
    ''' Um métodoque receba um país como parâmetro e retorne a 
        lista de vizinhos comuns aos dois países'''
    def paiscomum(self, op):
        comum=[]
        for x in op.fronteira:
            if x in self.fronteira:
                comum.append(x)
                
        print(f"Os paises vizinhos de {self.get_Nome()} e {op.get_Nome()}")
        for i in comum:
            print(i)
    '''Um método que retorne os países em ordem alfabética'''
    def ordenaPFront(self):
        frontOrdem=[]
        
        for i in self.fronteira:
            frontOrdem.append(i)

        frontOrdem.sort()
        for f in frontOrdem:
            print(f)