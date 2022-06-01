#lista são geradas com =[]
carro=["BMW", "Gol", "Fiat", "Jeep", "Siena"]
#Imprime todos os elementos
print(carro)
#imprime a posição especifica
print(carro[3])
#vc pode impremir de traz para frente
print(carro[-1])
#pode fazer a modificação de lista
carro[2]="Uno"
#função ".append" adiciona novos item a lista
carro.append("Selta")
carro.append("Fusca")
carro.append("Combi")
print(carro)
#Função len mostra o tamanho da lista
print(f"A quantidade de carros na lista eh {len(carro)}")
#Função .remove remove item da lista
carro.remove(carro[2])
print(f"A quantidade de carros na lista eh {len(carro)}")
carro.append("Fiat")
# OU
carro.remove("Gol")
print(f"A quantidade de carros na lista eh {len(carro)}")
#Função pop remove o ultimo item da lista
print(carro)
carro.pop
print(carro)
carro.append("Combi")
#Função "del" remove os item ate a indexação 
del carro[2]
# vai remover de 0 ate o item 2 da lista
#fazer a copia de uma lista para outra so usar o list() 
carro2=list(carro)
#para junta duas lista
carro3=carro+carro2
