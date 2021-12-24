import random
row = random.randint(1,8)
col = random.randint(1,8)
hv = random.randint(0,1)
if hv==0:
    p=row-1
    randomValue=col
else:
    p=col-1
    randomValue=row
d1=[[randomValue for j in range(1)] for i in range(3)]

for i in range(len(d1)):
    d2=d1[i]
 
    d2.insert(hv,p)
    p=p+1
    
print(d1)

       
