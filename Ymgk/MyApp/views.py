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
from . import emine
from . import fatih
import cv2
import numpy as np
# Create your views here.
@api_view(["POST"])
def Sayislem(sayi):
    
    try:
        body_unicode = sayi.body.decode('utf-8')
        body = json.loads(body_unicode)
        gelendeger=body['gelendeger']
        print(gelendeger,"geldi")
        y=emine.randomsayi(gelendeger)
        demo = cv2.imread("MyApp/koala.jpeg")

        fatih.resim(y,demo)

        return JsonResponse("Yeni sayi:",safe=False)
        
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
