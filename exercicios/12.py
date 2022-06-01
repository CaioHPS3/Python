peso=float(input("Qual o peso do peixe ?\n"))
if(peso>50):
    excesso=peso-50
    multa=excesso*4
    print(f"Peso do peixe:{peso}\n Excesso:{excesso}\n Multa:{multa}")
else:
    print(f"Peso do peixe:{peso}")