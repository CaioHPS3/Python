from re import U


termo=-1
while termo < 0:
    termo = int(input("Digite o n-enésimo termo da sequencia de fibonacci ?\n"))
penultimo=0
ultimo=1
for i in range(0, termo):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        atual= ultimo + penultimo
        print(atual)
        penultimo=ultimo
        ultimo=atual
salario=[1,2,3]
print(salario[1])