"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_aplicacion import views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('registrar-arbol/', views.registrar_arbol, name='registrar_arbol'),
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('detalle-arbol/<int:arbol_id>/', views.detalle_arbol, name='detalle_arbol'),

    path('registrar-arbol/', views.registrar_arbol, name='registrar_arbol'),
    path('editar-arbol/<int:arbol_id>/', views.editar_arbol, name='editar_arbol'),

    
    path('listar-arboles/', views.listar_arboles, name='listar_arboles'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


