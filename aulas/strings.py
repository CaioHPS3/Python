# para fazer comentarios simples em python usar o "#"
"""
para fazer comentarios mais extenso usar no ' "" ' no começo e no final 
"""

"""
funções que vc pode usa srings 
"""



nome="Caio Henrique"

print(nome)
#ou um caracter especifico
print(nome[3])
#ou uma parte espefica
print(nome[0:4])
# a função len mostra o tamanho de uma string 
print("Tamanho ="+str(len(nome)))
# a função  .strip retira os espaço desnecesarios de uma string
print(nome.strip())
#a função .lower converte a string para minusculo
print(nome.lower())
#a função .upper converte a string para maiusculo
print(nome.upper)
#a função .reclace troca uma string por outra
print(nome.replace("Caio","Kaio"))
# a função .split corta o caracter desejado
nome2= nome.split("i")
print(nome2)
# onde foi cortado o resto da string vão vira "Caracteres"
print(nome2[0])
print(nome2[1])
print(nome2[2])
# vc pode armazena as modificaçoes em outras variaveis
#exemplo= nome2= nome.split("i")
#Voce pode fazer uma busca dentro de uma strigs usando o "In"(dentro)
res="Henrique" in nome
#A palavra henrique esta dentro da variavel nome ? A resposta vem em True 
# podesse usar o "not in" 
res= "Henrique" in nome
#A palavra henrique 'não está' em dentro de nome ? False
nome3="Caio"
res=nome3 in nome 
#pode fazer isso também
