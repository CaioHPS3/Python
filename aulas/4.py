nome=str(input("Qual o nome ? "))
salario=float(input("Qual o salario ? "))
idade=int(input("Qual a idade ? "))
sexo=str(input("Qual o genero  ? "))
estadoC=str(input("Qual o estado civil ? "))

if(len(nome)>3):
    print("nome e maior que 3")
if(salario>0):
    print("Salario maior 0")
if(idade>=0 and idade<=150):
    print("Idade valida")
if(sexo=="f"):
    print("Feminino")
elif(sexo=="m"):
    print("Masculino")
else:
    print("Invalido")
