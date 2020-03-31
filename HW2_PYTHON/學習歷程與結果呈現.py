#!/usr/bin/env python
# coding: utf-8

# HW2
# ========
# <font size=3>這次的作業主要為輸入價格、票面金額、票面利率、到期年間、每年付息次數來計算YTM,SPOT RATE,FORWARD RATE，並用Forward Form的形式將各期對應的Forward Rate呈現出來。</font>
# -------------------------------
# <font size=3>我的學習歷程依序為<br>
# ----------------------
# <font size=3>ytm計算機<br>
# -----------------
# <font size=3>Spot rate計算機<br>
# -------------
# <font size=3>Forward rate計算機<br>
# -------------
# <font size=3>固定價格一次計算個期ytm,spot rate,forward rate<br>
# --------------------------
# 首先為ytm 計算機，這是老師在課程投影片後段放的ytm計算範例，概念為輸入債券的相關條件，再用輸入的付息種類來判斷其數以及每期利息，並透過np.irr的套件計算出每期ytm，最後用Decimal套件將之四捨五入，並print出結果
# 

# In[2]:


#ytm 計算機
import numpy as np 
from decimal import *

B=int(input("請輸入債券價格"))  
PVA=int(input("請輸入票面金額"))    
CR=float(input("請輸入票面利率"))/100   
Peri=int(input("請輸入期數")) 
kind=input("請輸入種類(輸入Annually or Semi-annually or Quarterly)")
if kind == "Annually" :
    C=float(CR*PVA*1)
    Peri=Peri
elif kind == "Semi-annually":
    C=float(CR*PVA/2)
    Peri=Peri*2
else:
    C=float(CR*PVA/4)
    Peri=Peri*4     
Coupon=[C for i in range (1,Peri)]    
#print(Coupon)     
Cf=[C+PVA]     
CA=[-B]+Coupon+Cf    
#print(CA)
ytm=np.irr(CA)*100
print("ytm為",(Decimal(ytm).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)),"%")


# 再來是Spot Rate計算機，此為輸入債券到期年限與債券價格即可計算此年限的spot rate，而結果分為連續複利與不連續複利兩種，這裡假設債券面額為1。

# In[3]:


#Spot Rate 計算機
import numpy as np 
from decimal import *

peri=int(input("請輸入spot rate期間"))
bondprice=float(input("請輸入債券價格"))
y=(bondprice**(-1/peri)-1)*100
Y=((-1/peri)*np.log(bondprice))*100
y=(Decimal(y).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
Y=(Decimal(Y).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
print("五年期的spot rate of interest為",y,"%")
print("五年期spot force of interest為",Y,"%")



# 再來是Forward Rate計算機，此為輸入forward rate期間與duration和兩個不同年限的零息債券價格，即可求算出對應之forward rate之計算器。

# In[11]:


#Forward Rate計算機
y1=input("請輸入forward rate 期間")
num_y1=int(y1)
d=int(input("請輸入forward rate的duration"))
d2=str(d)
y2_num=num_y1+d
y2=str(y2_num)
p1=float(input("請輸入"+d2+"年的零息債券價格(面額為1)"))
p2=float(input("請輸入"+y2+"年的零息債券價格(面額為1)"))

f=(p1/p2)**(1/num_y1)
print(f-1)


# 最後一個是老師上課說的主要的作業，就是透過輸入債券價格、面額、票面利率、到期年限、每年付息次數，即可以求出一個不同ytm、spot rate、forward rate，並且將forward rate以form的形式print出來，這題花了很多時間，反覆看了多次投影片，才明白為何可以這樣求出，因為我們固定了債券價格，並且是假設每一個不同到期年限的債券價格都是我們一開始輸入的那一個債券價格，於是我們可以推出不同年限的ytm、spot rate、和forward rate，在這一題用了大量的for loop，因為在算spot rate的時候，必須將每一次的現金流以不同的spot rate去折現，此過程及需要透過for loop來完成，而在print出結果的時候，因為這次想不要投過dateframe的方式，而是較直覺的直接將結果print出，因此也用到了大量的for loop迴圈，最後因為forward rate若不四捨五入則會使得forward rate的表格不太雅觀，因此我透過Decimal的套件將其四捨五入至小數點第四位。

# In[12]:


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
spot=[]
spot1=[]
ytm=[]
CA2=float(0)
for i in range(0,Peri,1):
    Coupon=[C for a in range (0,i)]  
    #print(Coupon)
    Cf=[C+PVA]  
    #print(Cf)
    CA=[-B]+Coupon+Cf
    #print(CA)
    spot.append(np.irr(CA))
    if i < 2:
        spotrate1=np.irr(CA)
        spot1.append(spotrate1)
        ytm.append(spotrate1)
        #print(spotrate1,i)
    else:
        for a in range (0,i,1):
            CA2=CA2+(C/((1+spot1[a])**(a+1)))
            #print(CA2,i)
        spotrate=(((B-CA2)/Cf[0])**(-(1/(i+1)))-1)
        #print(B-CA2,Cf[0],i)
        #print(((B-CA2)/Cf[0]),i)
        #print((-(1/i+1)),i)
        #print(spotrate,i)
        spot1.append(spotrate)
        ytm.append(np.irr(CA))
        CA2=0
#print(spot1)
#print(ytm)
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

#for i in range(0,Peri-1,1):
    #print(((1+spot1[i+1]*2)**(i+2)/(1+spot1[i]*2)**(i+1))-1)
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

