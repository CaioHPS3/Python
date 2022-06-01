#função "type" retorna o tipo da variavel
a=20
b=2.5
c=False

mensagem="Nova Linguagem Python"

print(type(a))
print(type(mensagem))
print(type(b))
print(type(c))

# para criar um lista (vetor) em python bastar colocar []

misto=[5.5, 10, "Caio", False] #Em Python os array pode receber diferentes tipos de dados

veiculos=["Carros", "Motocipleta", "Avião", "Barco"]
print(veiculos[1])

#lista podem ser modificadas

veiculos[1]= "bike"
print(veiculos[1])

# existe também a tupla que são entre parentezes

motos=("Xj6", "Honet", "Honda", "Yamara")
print(motos[1])

# trupla não pode ser modificada
#motos[1]= "Bis110"
#print(motos[1]) erro

x=range(0,100,2) #criando uma lista de 0 a 100 de dois em dois
#Uma string é um arrey de caracteres em python vc pode exibi ele todo