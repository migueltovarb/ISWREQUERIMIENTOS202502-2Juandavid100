from django.contrib import admin
from django.urls import path

from academico.views import (
    login_usuario,
    registrar_usuario,
    panel_estudiante,
    panel_profesor,
    panel_admin,
    cerrar_sesion,
    registrar_notas,
    inscribir_cursos
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login y registro
    path('', login_usuario, name='login'),
    path('registro/', registrar_usuario, name='registro'),

    # Paneles según rol del usuario
    path('panel/estudiante/', panel_estudiante, name='panel_estudiante'),

    # INSCRIBIR CURSOS (NUEVO)
    path('estudiante/inscribir-cursos/', inscribir_cursos, name='inscribir_cursos'),

    path('panel/profesor/', panel_profesor, name='panel_profesor'),
    path('panel/admin/', panel_admin, name='panel_admin'),

    # Registrar notas
    path('profesor/registrar-notas/', registrar_notas, name='registrar_notas'),

    # Cerrar sesión
    path('logout/', cerrar_sesion, name='logout'),
]
