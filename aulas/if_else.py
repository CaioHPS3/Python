a = 15
b=20
resp=0

op="3"
if op=="+":
    resp=a+b
elif op=="-":
    resp=a-b
elif op=="*":
    resp=a*b
elif op=="/":
    resp=a/b
else:
    print("Nem uma operação valida")

clima="Sol"
transporte="Bicicleta"
lugar=""
#and==&(expressão em C)==e
#or==||(expressão em C)==ou
if clima=="Sol" and transporte=="Bicicleta":
    lugar="Escola"
print(lugar)
"""
if a:
    print("Deu certo")
else:
    print("Não deu")

if a==False:
    b=14
else:
    b=15
if a<b:
    print("Deu certo")
else:
    print("Não deu")
"""