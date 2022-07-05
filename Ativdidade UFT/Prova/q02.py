from moduloq02 import Continente
from os import system

def menu(x):
    while True:
        opcao=int(input('\n1. Adicionar Países\n2. Consultar\n0. Outro Continente\n: '))
        
        if opcao == 1:
            op = 'a'
            while op != 'v':
                n=str(input('\nNome do País: ')).capitalize()
                p=int(input('População do País: '))
                d=float(input('Dimensão do País: '))
                x.Pais(n,p,d)
                op=str(input('\n[a]dicionar país / [v]oltar | [a/v]: '))
                
        elif opcao ==2:
            while True:
                gmode=int(input('\n1. Dimensão Total Continente\n2. População Total Continente\n3. Pais Maior População\n'
				'4. Pais Menor População\n5. Pais Maior Dimensão\n6. Pais Menor Dimensão\n7. Razão País Maior e Menor Dimensão\n0. volta\n: '))

                if gmode == 1:
                    print('\n',x.dTotal())

                elif gmode == 2:
                    print('\n',x.pTotal())

                elif gmode == 3:
                    print('\n',x.paisMaiorP()['nome'])

                elif gmode == 4:
                    print('\n',x.paisMenorP()['nome'])

                elif gmode == 5:
                    print('\n',x.paisMaiorD()['nome'])

                elif gmode == 6:
                    print('\n',x.paisMenorD()['nome'])

                elif gmode == 7:
                    print('\n',x.razaoDimenMaiorMenor())
                elif gmode == 0:
                    break
        elif opcao == 0:
            break

lcontinente=[]
print('INFORMAÇÃO SOBRE O CONTINENTE')
aux=""
i=0
while aux != "Não":
    
    cont=Continente(str(input('Nome Continente: ')).capitalize())
    i=i+1
    lcontinente.append(cont)
    aux=input("Adicionar mais um continente ?\n").capitalize()
    

while 0xc:
    system('clear')
    for i in range(len(lcontinente)):
        print(f" {i+1} . {lcontinente[i].nome}")

    op=int(input('\nPaís para ALTERAR ou CONSULTAR informações | [0] Sair\n: '))
    if op == 0:
        break
    else:
        menu(lcontinente[op-1])

menu(cont)