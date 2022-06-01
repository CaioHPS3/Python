#matrizes em python é uma lista dentro de outra lista
carros = [["Modelo", "Polo"], ["Fabricante", "Chevrole"], ["Ano", "2021"]]

print(carros[2][1])
carros[0][1]= "Gol"
#criar a linha e multiplicar pela quantidade desejada por linha
linha= [""]*3
#depois criar a matriz em si usando a lista de linhas e multiplica pela quantidade de calunas
#desejado
nomes= [linha] *3

#para acessar os espaço da matriz so usa os [][];
#for x in range (3):
    #for y in range (3):
        #nomes[x][y]=str(input(f"Qual vai ser o nome[{x}][{y}] ? "))

#Ou pode ser criado um loço de repetição para criar a matriz
notas=[]
#e criado uma lista de nota
for i in range (5):
    #a lista nota vai receber a variavel outros listas zeradas que vão ser as colunas
    notas.append(["   0    "]*5)

notas[0][0]="Portugues"
notas[1][0]="Ingles"
notas[2][0]="Física"
notas[3][0]="Matematica"
notas[4][0]="Programação"
notas[0][0]="Materias"
notas[0][1]="1° Bimestre"
notas[0][2]="2° Bimestre"
notas[0][3]="3° Bimestre"
notas[0][4]="4° Bimestre"

for i in range (5):
    print(notas[i])
