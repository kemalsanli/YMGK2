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
from . import kemal
from . import base64
import cv2
import numpy as np
import os
from rest_framework.parsers import FormParser,MultiPartParser
from PIL import Image
from django.core.files.storage import FileSystemStorage
import mimetypes
from django.utils.encoding import smart_str
from django.http import HttpResponse
from PIL import Image


@api_view(["POST"])
def Sayislem(sayi):

    try:


        gelendeger=sayi.data['hash']
        folder='resimler/'
        resim = sayi.data['image']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(resim.name, resim)
        SHASH = gelendeger
        path = "resimler/"+filename

        kemal.ymgk2xor(path,SHASH)
        # img = Image.open('temp/sonuc.png')
        with open('temp/sonuc.png', "rb") as img:
            return HttpResponse(img.read(), content_type='image/png')

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
