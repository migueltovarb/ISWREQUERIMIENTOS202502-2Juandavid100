from django.contrib import admin
from django.urls import path
from academico.views import (
    registrar_usuario, login_usuario,
    panel_estudiante, panel_profesor, panel_admin
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Registro y Login
    path('registro/', registrar_usuario, name='registro'),
    path('', login_usuario, name='login'),

    # Paneles para cada rol
    path('panel/estudiante/', panel_estudiante, name='panel_estudiante'),
    path('panel/profesor/', panel_profesor, name='panel_profesor'),
    path('panel/admin/', panel_admin, name='panel_admin'),
]

