num1=int(input("Qual o numero num1\n"))
num2=int(input("Qual o numero num2\n"))
num3=int(input("Qual o numero num3\n"))
maior=""

if num1>=num2>=num3:
    maior=num1
elif num2>=num1>=num3:
    maior=num2
elif num3>=num2>=num1:
    maior=num3
print(f"O maior numero eh {maior}")
