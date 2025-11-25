from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Perfil

# ==========================
#   REGISTRO DE USUARIO
# ==========================
def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        rol = request.POST.get("rol")

        if not username or not password or not rol:
            return render(request, "registro.html", {"mensaje": "Todos los campos son obligatorios"})

        if " " in username:
            return render(request, "registro.html", {"mensaje": "El nombre no puede tener espacios"})

        if User.objects.filter(username=username).exists():
            return render(request, "registro.html", {"mensaje": "Ese usuario ya existe"})

        # Crear usuario
        user = User.objects.create_user(username=username, password=password)

        # Crear perfil
        Perfil.objects.create(usuario=user, rol=rol)

        return redirect("login")

    return render(request, "registro.html")

# ==========================
#        LOGIN
# ==========================
def login_usuario(request):
    mensaje = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            rol = user.perfil.rol
            if rol == "estudiante":
                return redirect("panel_estudiante")
            elif rol == "profesor":
                return redirect("panel_profesor")
            else:
                return redirect("panel_admin")

        mensaje = "Usuario o contraseña incorrectos."

    return render(request, "login.html", {"mensaje": mensaje})

# ==========================
#        PANELES
# ==========================
def panel_estudiante(request):
    return render(request, "panel_estudiante.html")


def panel_profesor(request):
    return render(request, "panel_profesor.html")


def panel_admin(request):
    return render(request, "panel_admin.html")

# ================================================================
#   INSCRIBIR CURSOS (mínimo 3 – máximo 5)
# ================================================================
def inscribir_cursos(request):

    cursos = [
        "Matemáticas I",
        "Programación Básica",
        "Física I",
        "Inglés I",
        "Contabilidad",
        "Álgebra Lineal",
        "Deportes",
        "Humanidades"
    ]

    if request.method == "POST":
        seleccionados = request.POST.getlist("cursos")

        if len(seleccionados) < 3:
            return render(request, "inscribir_cursos.html", {
                "error": "Debes inscribir mínimo 3 cursos.",
                "cursos": cursos
            })

        if len(seleccionados) > 5:
            return render(request, "inscribir_cursos.html", {
                "error": "Solo puedes inscribir máximo 5 cursos.",
                "cursos": cursos
            })

        return render(request, "inscribir_ok.html", {"cursos": seleccionados})

    return render(request, "inscribir_cursos.html", {"cursos": cursos})

# ==========================
#      REGISTRAR NOTAS
# ==========================
def registrar_notas(request):
    return render(request, "registrar_notas.html")

# ==========================
#      CERRAR SESIÓN
# ==========================
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
