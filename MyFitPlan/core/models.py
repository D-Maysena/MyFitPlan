from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    NIVELES_CONDICION = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    username = models.CharField(max_length=150, unique=True)  # No debe ser único    
    edad = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    nivelCondicion = models.CharField(
        max_length=12,
        choices=NIVELES_CONDICION,
        default='Principiante'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
        # Personalizar el related_name para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  # Cambia 'usuario_set' a otro nombre que prefieras
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',  # Cambia 'usuario_set' a otro nombre que prefieras
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Ejercicio(models.Model):
    NIVEL_DIFICULTAD = [
        ('facil' ,'Facil'),
        ('medio','Medio'),
        ('dificil','Dificil')
    ]
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_url = models.URLField(max_length=500)
    musculo_objetivo = models.CharField(max_length=100)
    nivel_dificultad = models.CharField(
        max_length=100,
        choices=NIVEL_DIFICULTAD,
        default='Facil'
    )
    
    def __str__(self):
        return self.nombre

class EjercicioRutina(models.Model):
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE, related_name='ejercicio_rutina')
    video_url = models.URLField(blank=True)
    repeticiones = models.IntegerField()
    series = models.IntegerField()
    descanso = models.DurationField()

    def __str__(self):
        return f"{self.ejercicio.nombre} - Reps: {self.repeticiones} Series: {self.series}"
    
class RutinaPersonalizada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='rutinas')
    nombre_rutina = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    equipo_disponible = models.CharField(max_length=100, blank=True)
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"{self.nombre_rutina} - {self.usuario.nombre}"
    
class RutinaEjercicio(models.Model):
    id = models.AutoField(primary_key=True)
    rutina = models.ForeignKey(RutinaPersonalizada, on_delete=models.CASCADE, related_name='rutina_ejercicios')
    ejercicio_rutina = models.ForeignKey(EjercicioRutina, on_delete=models.CASCADE, related_name='rutina_ejercicios')

    def __str__(self):
        return f"{self.rutina.nombre_rutina} - {self.ejercicio_rutina.ejercicio.nombre}"

class Progreso(models.Model):
    rutina_ejercicio = models.ForeignKey(RutinaEjercicio, on_delete=models.CASCADE, related_name='progresos')
    fecha = models.DateField()
    repeticiones_completadas = models.IntegerField()
    ejercicio_completado = models.BooleanField(default=False)
    tiempo_dedicado = models.DurationField()

    def __str__(self):
        return f"Progreso en {self.rutina_ejercicio.ejercicio_rutina.ejercicio.nombre} - {self.fecha}"
    
class Estadistica(models.Model):
    rutina = models.ForeignKey(RutinaPersonalizada, on_delete=models.CASCADE, related_name='estadisticas')
    calorias_quemadas = models.IntegerField()
    tiempo_entrenamiento = models.DurationField()
    progreso_general = models.DecimalField(max_digits=5, decimal_places=2)
    peso_actual = models.FloatField()

    def __str__(self):
        return f"Estadísticas de {self.rutina.nombre_rutina}"