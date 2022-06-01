carro=float(input("Qual o valor do carro ? "))
moto=float(input("Qual o valor do moto ? "))
barco=float(input("Qual o valor do barco ? "))


if(carro<=moto<=barco):
    print("Comprar carro")
elif(moto<=carro<=barco):
    print("Comprar moto")
elif(barco<=moto<=carro):
    print("Comprar barco")  