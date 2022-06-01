#trupla é a mesma coisa de uma lista só que vc não pode modificala
#não pode adiciona
nome=("Caio", "Davi", "Jocirleide", "Deuzimar")
# nome[1]="João" da erro
#trupla é entre parentezes
#uma vez definida não pode ser modificada
#Da para fazer uma ganbiara armazenando os dados da trupla em uma lista
listanome=list(nome)
#modificar a lista e depois copia para trupla
listanome[0]="Henrique"
nome=tuple(listanome)
for x in nome:
    print(x)