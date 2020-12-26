
import random as rnd 
import fatih
def Work_Package(workP2Out,isColor,uzunluk):
    if(isColor==True):
        size = 8*3*uzunluk  #ip5 paketi resim boyutu
    if(isColor==False):
        size = 3*8*uzunluk
    print('toplam çıktı:'+ str(size))
    tempWork3=[]
    Work3=[]
    while(True):
        if(size > len(tempWork3)):
          tempWork3.extend((randomMillion_Bit(workP2Out[int(rnd.random())])))
        else:
            break
        
    for i in range(size):
        Work3.append(tempWork3[i])
        
    print('son liste:' + str(len(Work3)))
    return Work3
   
    

def randomMillion_Bit(wp2Out):
    xExVal=wp2Out
    randomSize=100
    rand_Bit=list()
    for i in range(randomSize):
        xNewVal = xExVal*(1 - xExVal)*4
        if(xNewVal < 0.5):   
            rand_Bit.insert(i, rnd.randint(0,128))
        else:
            rand_Bit.insert(i, rnd.randint(128,255))
        xExVal = xNewVal
    return rand_Bit

def xor(Work3, gelendeger, n): 
    #print("gelendeger :",gelendeger)
    #print("work 3 :",Work3)
    ans = []
    for i in range(n): 
       
        ans.append(Work3[i] ^ gelendeger[i])
            
            
    return ans 
# Create your views here.

def randomsayi(gelendeger):  
    #gelendeger=[107,116,61,144,204,8,62,225,191,177,84,158,51,46,207,216,15,231,107,69,37,37,198,18,246,254,37,234,71,77,245,134]
    print(gelendeger,"gelendeger")
    i=0
    workP2Out=list()
    
    while(i<12):
        rnd_Number=rnd.random()
        workP2Out.append(rnd_Number)
        print(rnd_Number)
        i=i+1
    uzunluk=len(gelendeger)
    y=xor(Work_Package(workP2Out,True,uzunluk), gelendeger,len(gelendeger))
    print("xorlanmış",y)
    fatih.resim(y)
       
        
