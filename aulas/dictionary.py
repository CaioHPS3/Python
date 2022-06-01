#Para criar um dictonary vc usa chaves {}
#você vai precisar de uma chave e de um valor (key:value) separados por dois pontos ":"
#Para adciona um novo item usar o virgula ","
bolacha={"Fabricante":"Lacta", "Sabor":"Negresco"}
#para imprimir um item especifico vc usa as a key (chave)
print(bolacha)
print(bolacha["Sabor"])
#teste
teste=str(input("O que vc quer consultar ? "))
print(bolacha[teste])
#podemos alterar a variaveis usando a chave
bolacha["Sabor"]= "Moça"
print(bolacha)
#teste1
teste1=str(input("O que vc deseja alterar ? "))
if teste1=="Fabricante":
    aux=str(input("Qual a irar ser a nova fabricante ?"))
    bolacha["Fabricante"]=aux
if teste1=="Sabor":
    aux=str(input("Qual a irar ser o novo sabor ?"))
    bolacha["Sabor"]=aux
print(bolacha)
#adicionando uma nova chave
bolacha["Unidades"]= 2
#Removendo uma chave
bolacha.pop("Unidades")
#ou 
del bolacha["Fabricante"]
#Maneiras de imprimir 
for x in bolacha:
    print(x) # print da chave
    print(bolacha[x]) #print dos conteudos
#Outra forma de imprimir
for x in bolacha:
    print((f"{x} = {bolacha[x]}"))

#####################################################################
#podemos criar um Dictionary dentro de outro dictionary seria tipo uma string
#so que em python

carros={
    "Carro1":{
        "Fabricante": "Volkswagem",
        "Modelo": "Gol" 
    },
    "Carro2":{
        "Fabricante": "Ford",
        "Modelo": "Focus"
    },
    "Carro3":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    }
}
#para acessar e como se force uma matriz
print(carros)
print(carros["Carro1"])
print(carros["Carro2"]["Fabricante"])
print(carros["Carro3"]["Modelo"])