from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.libro.views import index_biblioteca, index_dashboard, LibroRegistrar, LibroListar, LibroUpdate, LibroDelete, LibroLiteratura,LibroMatematica, LibroComunicación, LibroHistoria, LibroVarios

urlpatterns = [
    path('', index_biblioteca, name='index_biblioteca'),
    path('biblioteca/dashboard', login_required(index_dashboard), name='index_dashboard'),

    path('registrar/', login_required(LibroRegistrar.as_view()), name='libro_registrar'),
    path('listar/', login_required(LibroListar.as_view()), name='libro_listar'),
    path('editar/<pk>/', login_required(LibroUpdate.as_view()), name='libro_editar'),
    path('eliminar/<pk>/', login_required(LibroDelete.as_view()), name='libro_eliminar'),

    path('listarL/', LibroLiteratura, name='libro_listar_Literatura'),
    path('listarM/', LibroMatematica, name='libro_listar_Matematica'),
    path('listarC/', LibroComunicación, name='libro_listar_Comunicacion'),
    path('listarH/', LibroHistoria, name='libro_listar_Historia'),
    path('listarV/', LibroVarios, name='libro_listar_Varios'),
    
]