from rest_framework import serializers
from .models import Usuario, Ejercicio, RutinaEjercicio, RutinaPersonalizada, EjercicioRutina, Estadistica, Progreso

class UsuarioSerializer(serializers.ModelSerializer):
    confirmar_contraseña = serializers.CharField(write_only=True)  
    
    class Meta:
        model = Usuario
        fields = ['id', 'username','first_name', 'last_name', 'email','password','confirmar_contraseña', 'edad', 'peso', 'altura', 'nivelCondicion', 'fecha_creacion']
        extra_kwargs = {
            'password': {'write_only': True}, 
            'confirmar_contraseña': {'write_only': True}, 
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirmar_contraseña']:
            raise serializers.ValidationError({"confirmar_contraseña": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirmar_contraseña')
        usuario = Usuario.objects.create(**validated_data)
        return usuario
        
class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'
        
class EjercicioRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EjercicioRutina
        fields = '__all__'
        
class RutinaEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaEjercicio
        fields = '__all__'
class RutinaPersonalizadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaPersonalizada
        fields = '__all__'
        
class EstadisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica
        fields = '__all__'

class ProgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progreso
        fields = '__all__'
        
        