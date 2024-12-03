from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Arbol

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')  # Renderiza el template

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


#def login_view(request):
#    if request.method == 'POST':
#        correo = request.POST.get('correo')
#        contrasena = request.POST.get('contrasena')
#
#        # Buscar usuario en la base de datos
#        try:
#            usuario = Usuario.objects.get(correo=correo, contrasena=contrasena)
#
#            # Verificar el grado del usuario
#            if usuario.grado.nombre == 'Especialista':
#                return redirect('/registro-arboles')  # Redirige a la página de registro de árboles
#            elif usuario.grado.nombre == 'Administrador':
#                return redirect('/gestion-usuarios')  # Redirige a la página de gestión de usuarios
#
#        except Usuario.DoesNotExist:
#            # Usuario no encontrado
#            messages.error(request, 'Correo o contraseña incorrectos')
#
#    return render(request, 'login.html')  # Renderizar nuevamente el login si falla


from django.shortcuts import render

def login_view(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        contrasena = request.POST.get("contrasena")

        usuario = Usuario.objects.filter(correo=correo).first()

        if usuario and usuario.contrasena == contrasena:
            # Autenticar manualmente al usuario
            request.session['usuario_id'] = usuario.id
            # Redirigir según el tipo de usuario
            if usuario.grado.nombre == "Especialista":
                return redirect('/registrar-arbol/')
            elif usuario.grado.nombre == "Administrador":
                return redirect('/gestion-usuarios/')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
            return render(request, 'login.html', {"error": "Correo o contraseña incorrectos."})

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from .models import Arbol
from django.contrib.auth.decorators import login_required


def registrar_arbol(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad_aproximada = request.POST.get('edad_aproximada')
        especie = request.POST.get('especie')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        descripcion = request.POST.get('descripcion')
        cuidados = request.POST.get('cuidados')
        riego_por_semana = request.POST.get('riego_por_semana')
        imagen = request.FILES.get('imagen')

        arbol = Arbol(
            nombre=nombre,
            edad_aproximada=edad_aproximada,
            especie=especie,
            latitud=latitud,
            longitud=longitud,
            descripcion=descripcion,
            cuidados=cuidados,
            riego_por_semana=riego_por_semana,
            imagen=imagen
        )
        arbol.save()

        return redirect('registrar_arbol')  # Redirige a la misma página para ver los árboles actualizados

    # Obtener todos los árboles registrados
    arboles = Arbol.objects.all()
    return render(request, 'registrar_arbol.html', {'arboles': arboles})

def dashboard(request):
    # Obtener los árboles desde la base de datos
    arboles = Arbol.objects.all()  # O personaliza tu consulta según sea necesario
    return render(request, 'dashboard.html', {'arboles': arboles})

def detalle_arbol(request, arbol_id):
    # Obtener el árbol por ID
    arbol = get_object_or_404(Arbol, id=arbol_id)
    # Convertir el árbol en un diccionario para enviarlo al template
    arbol_dict = model_to_dict(arbol)
    return render(request, 'detalle_arbol.html', {'arbol': arbol_dict})

def listar_arboles(request):
    # Recuperar todos los árboles de la base de datos
    arboles = Arbol.objects.all()
    
    return render(request, 'listar_arboles.html', {'arboles': arboles})

def editar_arbol(request, arbol_id):
    arbol = get_object_or_404(Arbol, id=arbol_id)

    if request.method == 'POST':
        arbol.nombre = request.POST.get('nombre')
        arbol.edad_aproximada = request.POST.get('edad')
        arbol.especie = request.POST.get('especie')
        arbol.latitud = request.POST.get('latitud')
        arbol.longitud = request.POST.get('longitud')
        arbol.descripcion = request.POST.get('descripcion')
        arbol.cuidados = request.POST.get('cuidados')
        arbol.riego_por_semana = request.POST.get('riego_por_semana')
        imagen = request.FILES.get('imagen')
        if imagen:
            arbol.imagen = imagen

        arbol.save()
        return redirect('registrar_arbol')  # Redirige a la página de registro para ver el árbol actualizado

    return render(request, 'editar_arbol.html', {'arbol': arbol})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


#IR AGREGANDO LAS VIEWS PARA AGREGAR ADMINISTRADORES, E INTENTAR INFORMAR QUE ESPECIALISTA DIO DE ALTA UN ARBOL