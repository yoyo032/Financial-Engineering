#!/usr/bin/env python
# coding: utf-8

# In[3]:


#固定價格計算Ytm,Spot Rate,Forward Rate
import numpy as np 
from decimal import *

B=int(input("請輸入債券價格"))  
PVA=int(input("請輸入票面金額"))    
CR=float(input("請輸入票面利率"))/100   
Peri=int(input("請輸入期數"))
N=int(input("請輸入每年付息次數"))
print(" ")
C=float(CR*PVA/N)
Peri=Peri*N
spot1=[]
ytm=[]
CA2=float(0)

for i in range(0,Peri,1):
    Coupon=[C for a in range (0,i)]  
    Cf=[C+PVA]  
    CA=[-B]+Coupon+Cf
    spot.append(np.irr(CA))
    if i < 2:
        spotrate1=np.irr(CA)
        spot1.append(spotrate1)
        ytm.append(spotrate1)
    else:
        for a in range (0,i,1):
            CA2=CA2+(C/((1+spot1[a])**(a+1)))
            #print(CA2,i)
        spotrate=(((B-CA2)/Cf[0])**(-(1/(i+1)))-1)
        spot1.append(spotrate)
        ytm.append(np.irr(CA))
        CA2=0
print("YTM Form")
print(" ")
b=1
for i in ytm:
    print("第"+str(b/N)+"年ytm為"+"\t"+str(i),end='\n')
    b+=1
print(" ")
print("Spot Rate Form")
print(" ")
a=1
for i in spot1:
    print("第"+str(a/N)+"年spot rate為"+"\t"+str(i),end='\n')
    a+=1
print(" ")

print("Forward Rate Form")
print(" ")
for i in range(0,Peri,1):
    if i < Peri-1:
        print("Y"+str((i+1)/N),end="\t")
    else:
        print("Y"+str((i+1)/N),end='\n')

for i in range(0,Peri,1):
    for j in range(0,Peri,1):
        if i >= j :
            print('x',end="\t")
        elif j < Peri-1 :
            print((Decimal(((1+spot1[j])**(j+1)/(1+spot1[i])**(i+1))**(1/(j-i))-1).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)),end='\t')
        else :         
            print((Decimal(((1+spot1[j])**(j+1)/(1+spot1[i])**(i+1))**(1/(j-i))-1).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)),end='\n')


# In[ ]:




