#Jogo onde o sistema vai gerar um numero aleatorio e o jogador vai tentar adinhar esse numero
#Para isso teremos que importa a biblioteca que gera numeros aleatorios
import random

erros=0
#vai contabilizar o numero de erros
num_sorteado=random.randrange(0,10)
#vai gerar um numero de aleatorio com um tamanho entre 0 a 10
jogador=int(input("Qual o numero que vc deseja tentar ? "))
#numero que o jogador escolheu

#sistema do jogo
while num_sorteado!=jogador:
    if num_sorteado>jogador:
        print("Errou o numero é maior")
    elif num_sorteado<jogador:
        print("Errou o numero é menor")
    erros+=1
    jogador=int(input("Qual o numero que vc deseja tentar ? "))
print(f"Parabéns vc acertou o numero era {num_sorteado} e vc disse {jogador}, voce errou {erros} vezes")