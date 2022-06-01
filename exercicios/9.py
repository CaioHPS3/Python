op=str(input("O que vc gastria de converter ? "))
#F=fahrenheit C=Celsios 
if(op== 'F'):
    temp=float(input("Quantos fahrenheit vc gostaria de converter para celsius ? "))
    conv=5*((temp-32)/9)
    print(f"{temp} fahrenheit e o que vale a {conv} celsius")
if(op=='C'):
    temp=float(input("Quantos celsios vc gostaria de converter para fahrenheit ? "))
    conv=(temp*1.8)+32
    print(f"{temp}celsius e o que vale a {conv} fahrenheit")
else:
    print("Invalido")

