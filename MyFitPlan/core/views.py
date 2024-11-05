from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Usuario, Ejercicio, EjercicioRutina
from .serializers import UsuarioSerializer, EjercicioSerializer, EjercicioRutinaSerializer
from rest_framework.authtoken.models import Token

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer  

    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        usuario = serializer.instance  # Esto debe ser el usuario que se acaba de crear
        token = Token.objects.create(user=usuario)
                        
        return Response({
            "token": token.key,
            "usuario": serializer.data
        }, status=status.HTTP_201_CREATED)    
    
    def login(self, request):
        email = request.data.get('email')
        contraseña = request.data.get('password')
        
        try:
            usuario = Usuario.objects.get(email=email)  
        
            if usuario.password == contraseña:
                token, created = Token.objects.get_or_create(user=usuario)
                print(token)
                serializer = UsuarioSerializer(instance=usuario)
                return Response({"message": "Inicio de sesión exitoso.", "token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciales inválidas."}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Usuario.DoesNotExist:
            return Response({"error": "No se encontró un usuario con ese correo electrónico."}, status=status.HTTP_404_NOT_FOUND)
        
class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()  
    serializer_class = EjercicioSerializer  
    
class EjercicioRutinaViewSet(viewsets.ModelViewSet):
    queryset = EjercicioRutina.objects.all()
    serializer_class = EjercicioRutinaSerializer