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


def resimgonder():

    response = HttpResponse(content_type='resimler/')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('koala.jeg')

    response['X-Sendfile'] = smart_str('resimler/')
# It's usually a good idea to set the 'Content-Length' header too.
# You can also set any other required headers: Cache-Control, etc.
    return response
# Create your views here.
# def gonder():
#     img = Image.open('resimler/koala.jpeg')
#     content_type=mimetypes.guess_type('koala.jpeg')[0]  # Use mimetypes to get file type
#     response=HttpResponse(img,content_type=content_type)
#     response['Content-Length']=os.path.getsize(img)
#     # This works for most browsers, but IE will complain sometimes
#     response['Content-Disposition']="attachment;"
#     return response
@api_view(["POST"])
def Sayislem(sayi):

    try:
        # file = sayi.data['file']
        # image = objects.create(image=file)
        # gelen=sayi.data['gelendeger']
        # kaydet.kaydet(file_obj,'testrgba.png')
        # print(gelen,"geleneneenenen")
        # print(file_obj)

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
