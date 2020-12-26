import random as rnd
# import the library module 
import sys 
import hashlib 
def randomMillion_Bit(wp2Out):
    xExVal=wp2Out
    randomSize=100
    rand_Bit=list()
    for i in range(randomSize):
        xNewVal = xExVal*(1 - xExVal)*4
        if(xNewVal < 0.5):   
            rand_Bit.insert(i, 0)
        else:
            rand_Bit.insert(i, 1)
        xExVal = xNewVal
    return rand_Bit
 
work_P2=list()
for i in range(12):
    rnd_Number=rnd.random()
    work_P2.append(rnd_Number)
    print(rnd_Number)
    
def Work_Package(workP2Out,height,width,isColor):
    if(isColor==True):
        size = 3*height*width*8  #ip5 paketi resim boyutu
    if(isColor==False):
        size = height*width*8
    print('toplam çıktı:'+ str(size))

    tempWork3=[]
    Work3=[]
    while(True):
        if(size > len(tempWork3)):
          tempWork3.extend((randomMillion_Bit(work_P2[int(rnd.random())])))
        else:
            break
        
    for i in range(size):
        Work3.append(tempWork3[i])
        
    print('son liste:' + str(len(Work3)))
    return Work3
   
gelendeger=[0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0]
def xor(Work3, gelendeger, n): 
    #print("gelendeger :",gelendeger)
    #print("work 3 :",Work3)
    ans = ""
    for i in range(n): 
       
        if (Work3[i] == gelendeger[i]):  
            ans += "0"
            
        else:
            ans += "1"
            
    return ans 

#(Work_Package(workP2Out, 1, 1,True))
print("-------------------------------XOR----------------------------------------")
print(xor(Work_Package(work_P2, 1, 1,True), gelendeger,24 ))
            