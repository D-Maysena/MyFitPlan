from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet, EjercicioViewSet, EjercicioRutinaViewSet
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'ejercicios', EjercicioViewSet, basename='ejercicios')
router.register(r'ejerciciorutina', EjercicioRutinaViewSet, basename='ejerciciorutina')

urlpatterns = [
    path('api/v1/', include(router.urls)),  
    path('api/v1/login/', UsuarioViewSet.as_view({'post': 'login'}), name='usuario-login'),
    path('api/v1/register/', UsuarioViewSet.as_view({'post': 'register'}), name='usuario-register'),
    path("docs/", include_docs_urls(title="MyFitPlan API")),
]
