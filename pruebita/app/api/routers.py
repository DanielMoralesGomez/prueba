from rest_framework.routers import DefaultRouter
from ..usuario.views import *
from ..estudiante.views import *


router = DefaultRouter()

router.register(r'estudiante', EstudianteViewSet, basename='Estudiante')
router.register(r'usuario', UsuarioViewSet, basename='Usuario')


urlpatterns = router.urls