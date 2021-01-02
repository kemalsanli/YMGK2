from rest_framework import serializers
from .models import Guncelkonular
class GuncelkonularSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guncelkonular
        fields='__all__'