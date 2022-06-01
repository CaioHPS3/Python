


carros=["Gol", "Fiat", "Polo", "Siena", "Combi"]
#Variavel x ira recer o que estar dentro(in) de carros 
"""
for x in carros:
    print(x)
#Da para exiber strings como ela é indexavel vai exbir item por item [0]...[n/]
for x in "Caio é o cara":
    print(x)
for x in ["Gol", "Fiat", "Polo", "Siena"]:
    print(x)

#percorendo o vetor carros de 0 a 5 pulando de dois em dois
for x in range (0, 5, 2):
    print(carros[x])
#percorendo o vetor carros na quantidade elementos do vetor carro
#usando a função len.
for x in range (len(carros)):
    print(carros[x])
"""    
############################### WHILE ##########################
#variavel de controle
a=0

while a<=10:#condição para continuar rodando
    print(a)
    a+=2 #modificando a variavel de controle

nomes=[]
nome=str(input("Qual vai ser o nome do novo carro ? "))
while nome != "-1":
    nomes.append(nome)
    nome=str(input("Qual vai ser o nome do novo carro ? "))    

i=0
while i<+len(nomes):
    print(nomes[i])
    i+=1    