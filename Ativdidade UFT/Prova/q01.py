from os import system
from moduloq01 import Pais

def menu(x):
    
    while 0xc:
        xmode=int(input('\n1. Alterar\n2. Consultar\n0. Outro País\n: '))

        if xmode == 1:
            while 0xc:
                system('clear')
                print(f"MENU: Alterar | PAÍS: {x.get_Nome()}")                
                print('1. Nome')
                print('2. Código')
                print('3. População')
                print('4. Dimensão')
                print('5. Países Limítrofes')
                smode=int(input('0. voltar\n: '))

                if smode == 1:
                    nome=str(input('Novo Nome: '))
                    x.setNome(nome)

                elif smode == 2:
                    code=str(input('Novo Código: '))
                    x.setCodigo(code)
                
                elif smode == 3:
                    pop=int(input('Nova Quantide População: '))
                    x.setPopul(pop)
                
                elif smode == 4:
                    dim=float(input('Nova Dimensaõ: '))
                    x.setDimen(dim)

                elif smode == 5:
                    # print('Adicionar País')
                    x.paisesfront()
                else:
                    break

        elif xmode == 2:
            while 0xc:
                system('clear') #LINUX

                print('MENU: Consula | PAÍS: {}'.format(x.get_Nome()))
                print('1. Nome')
                print('2. Código')
                print('3. População')
                print('4. Dimensão')
                print('5. Mesmo País?')
                print('6. Países Limítrofes?')
                print('7. Densidade Populacional')
                print('8. Vizinhos Comuns')
                print('9. Países vizinhos ordenados')
                gmode=int(input('0. Voltar\n: '))
                

                if gmode == 1:
                    print(x.get_Nome())

                elif gmode == 2:
                    print(x.get_Codigo())
                
                elif gmode == 3:
                    if (x.get_Popul() == 0):
                        print("Dado não foi preenchido, Altere!\n")
                    else:
                        print(x.get_Popul())
                
                elif gmode == 4:
                    print('{} m^2'.format(x.get_Dimen()))

                elif gmode == 5:
                    code=str(input('\nCódigo do País para verificar: ')).upper()
                    x.comparaPais(code)

                elif gmode == 6:
                    name=str(input('\nNome do País para verificar: ')).capitalize()
                    x.limitrofe(name)

                elif gmode == 7:
                    if x.populacao == 0:
                        print("População ainda não definida, Altere!\n")
                    else:
                        print(x.densidade())

                elif gmode == 8:
                    print()
                    for p in lpaises:
                        if p.get_Codigo() == x.get_Codigo():
                            continue
                        print('{0} - {1}'.format(p.get_Codigo(), p.get_Nome()))

                    code = str(input('\nCódigo do País para verificar os vizinhos comuns\n: ')).upper()
                    
                    for p in lpaises:
                        if p.get_Codigo() == code:
                            x.paiscomum(p)

                elif gmode == 9:
                    print('\nPaíses vizinhos do {} em ordem alfabética:'.format(x.get_Nome()))
                    x.ordenaPFront()

                else:
                    break

                input('\n[ Tecle ENTER para continaur ] ')
                system('clear') 

        else:
            return


lpaises=[]
print('INFORME AS SEGUINTES INFORMAÇÕES DOS PAÍSES')
aux=""
i=0
while aux != "Não":
    c=str(input(f"Codigo do pais {i+1} ?\n")).upper()
    n=str(input(f"Nome do pais {i+1} ?\n")).capitalize()
    d=float(input(f"Dimenção do pais {i+1} ?\n"))
    p=Pais(c, n, d)
    i=i+1
    lpaises.append(p)
    aux=input("Adicionar mais um pais ?\n").capitalize()
    

while 0xc:
    system('clear')
    for i in range(len(lpaises)):
        print(f" {i+1} . {lpaises[i].get_Nome()}")

    op=int(input('\nPaís para ALTERAR ou CONSULTAR informações | [0] Sair\n: '))
    if op == 0:
        break
    else:
        menu(lpaises[op-1])
