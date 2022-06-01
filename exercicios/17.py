notaP1=float(input("Qual a nota do aluno no primeiro Bimestre\n"))
notaP2=float(input("Qual a nota do aluno no segundo Bimestre\n"))
notaP3=float(input("Qual a nota do aluno no terceiro Bimestre\n"))
notaP4=float(input("Qual a nota do aluno no quarto Bimestre\n"))
media=(notaP1+notaP2+notaP3+notaP4)/4

print(f"A media da nota do aluno {media}\n E vc foi:")

if media==10:
    print("Aprovado")

elif media<7:
    print("Reprovado")
    

elif media>=7:
    print("Aprovado")
