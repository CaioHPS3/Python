# "def", é a definição de uma função em python

def aprentação():
    print("Parabens vc achou no conteudo de lista")

aprentação()
num1=int(input("Qual o 1° numero ?"))
num2=int(input("Qual o 1° numero ?"))

def somar():
    r= num1+num2
    print(f"A soma de {num1} e {num2} é {r}")

somar()
def subtração():
    r= num1-num2
    print(f"A subtração de {num1} e {num2} é {r}")

subtração()

print("")
print("")

########### argumentos de entrada #############
def somar(num1, num2):
    r= num1+num2
    print(f"A soma de {num1} e {num2} é {r}")

somar(50, 30)
#não precisa ser necessariamente na ordem que a função vai receber a função
#vc pode fala qual variavel variavel vai receber um certo valor
somar(num2=15, num1=5)
somar(6, 4)

#eu não preciso declara argumento por agumento de entrada posso colocar um "*"
#que vai reconhecer que vai entrar uma quantidade n de argumentos
#ex

def texto(*t):
    #Vai fazer o lupe ate a quantidade de parametros enviados acabar
    for i in t:
        print(i)

texto("Caio", "Henrique", "Pinho", "Santos")

def multiplicação(*m):
    res=1
    for i in m:
        res*=i
    return res
        
resposta=multiplicação(5,4,3,2,1)
print(resposta)        
#posso usar uma lista com argumento em uma função
lista=[1,2,3,4,5]
resposta= multiplicação(lista)
print(resposta)  
    
    
    