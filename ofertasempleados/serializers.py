from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Empresa, Oferta, Usuario, Postulacion

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class PostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = '__all__'


class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'descripcion_perfil', 'identificacion', 'telefono', 'user_id']

class UsuarioTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()