#tratamento de de erro 
#Se ocorre um erro no meu "try" ele vai executa a mensagem de erro que vai ser colocada no
#except
try:
    print(x)
except:
    print("Erro x não definido")
#o else vai se executado caso não aja erro
else:
    print("Programa estar de boa")
#o finally vai ser executado independente 
finally:
    print("Fim do problema")