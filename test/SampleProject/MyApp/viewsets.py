from rest_framework import viewsets
from . import models
from . import serializers
class GuncelkonularViewset(viewsets.ModelViewSet):
    queryset=models.Guncelkonular.objects.all()
    serializer_class=serializers.GuncelkonularSerializer