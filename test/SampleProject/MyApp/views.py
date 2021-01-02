from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import random as rnd 
from .viewsets import GuncelkonularViewset

def hexadecimal(gelendeger):
    hexadecimal = gelendeger
    end_length = len(hexadecimal) * 4
    hex_as_int = int(hexadecimal, 16)
    hex_as_binary = bin(hex_as_int)
    padded_binary = hex_as_binary[2:].zfill(end_length)
    return(padded_binary)

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
            rand_Bit.insert(i, 0)
        else:
            rand_Bit.insert(i, 1)
        xExVal = xNewVal
    return rand_Bit

def xor(Work3, gelendeger, n): 
    print("gelendeger :",gelendeger)
    print("work 3 :",Work3)
    ans = ""
    for i in range(n): 
       
        if (Work3[i] == gelendeger[i]):  
            ans += "0"
        
        else:
            ans += "1"
            
    return ans 
# Create your views here.
@api_view(["POST"])
def Sayislem(sayi):
    
    try:
        body_unicode = sayi.body.decode('utf-8')
        body = json.loads(body_unicode)
        gelendeger=body['resimadi']
        
        y=gelendeger
        GuncelkonularViewset(sayi)
        return JsonResponse("Yeni sayi:"+y,safe=False)
        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
