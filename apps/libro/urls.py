from django.urls import path, include
from apps.libro.views import index_biblioteca, index_dashboard, LibroRegistrar, LibroListar, LibroUpdate, LibroDelete, LibroLiteratura,LibroMatematica, LibroComunicación, LibroHistoria, LibroVarios

urlpatterns = [
    path('', index_biblioteca, name='index_biblioteca'),
    path('biblioteca/dashboard', index_dashboard, name='index_dashboard'),

    path('registrar/', LibroRegistrar.as_view(), name='libro_registrar'),
    path('listar/', LibroListar.as_view(), name='libro_listar'),
    path('editar/<pk>/', LibroUpdate.as_view(), name='libro_editar'),
    path('eliminar/<pk>/', LibroDelete.as_view(), name='libro_eliminar'),

    path('listarL/', LibroLiteratura, name='libro_listar_Literatura'),
    path('listarM/', LibroMatematica, name='libro_listar_Matematica'),
    path('listarC/', LibroComunicación, name='libro_listar_Comunicacion'),
    path('listarH/', LibroHistoria, name='libro_listar_Historia'),
    path('listarV/', LibroVarios, name='libro_listar_Varios'),
    
]