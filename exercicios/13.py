quant=float(input("Quanto vc ganhar por hora trabalhada ? "))
horas=float(input("Quantas horas vc trabalhou esse mes ? "))
salarioB=quant*horas
ir=salarioB*0.11
inss=salarioB*0.08
sid=salarioB*0.05
salarioL=salarioB-ir-inss-sid
print(salarioB)
print(ir)
print(sid)
print(sid)
print(salarioL)
