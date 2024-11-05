# Generated by Django 5.1.3 on 2024-11-05 15:20

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen_url', models.URLField(max_length=500)),
                ('musculo_objetivo', models.CharField(max_length=100)),
                ('nivel_dificultad', models.CharField(choices=[('facil', 'Facil'), ('medio', 'Medio'), ('dificil', 'Dificil')], default='Facil', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('edad', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nivelCondicion', models.CharField(choices=[('principiante', 'Principiante'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], default='Principiante', max_length=12)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='usuario_set', related_query_name='usuario', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', related_query_name='usuario', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EjercicioRutina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(blank=True)),
                ('repeticiones', models.IntegerField()),
                ('series', models.IntegerField()),
                ('descanso', models.DurationField()),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ejercicio_rutina', to='core.ejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='RutinaEjercicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ejercicio_rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutina_ejercicios', to='core.ejerciciorutina')),
            ],
        ),
        migrations.CreateModel(
            name='Progreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('repeticiones_completadas', models.IntegerField()),
                ('ejercicio_completado', models.BooleanField(default=False)),
                ('tiempo_dedicado', models.DurationField()),
                ('rutina_ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progresos', to='core.rutinaejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='RutinaPersonalizada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rutina', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('equipo_disponible', models.CharField(blank=True, max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutinas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='rutinaejercicio',
            name='rutina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutina_ejercicios', to='core.rutinapersonalizada'),
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorias_quemadas', models.IntegerField()),
                ('tiempo_entrenamiento', models.DurationField()),
                ('progreso_general', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_actual', models.FloatField()),
                ('rutina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estadisticas', to='core.rutinapersonalizada')),
            ],
        ),
    ]
