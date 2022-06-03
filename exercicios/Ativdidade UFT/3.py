import random
from re import X
v1=[]
v2=[]
v3=[]
for a in range(10):
    v=random.randint(10, 100)
    v1.append(v)
    vv=random.randint(10, 100)
    v2.append(vv)
print(v1)
print(v2)
for a in range(0, 10):
    v3.append(v1[a]+v2[a])
print(v3)