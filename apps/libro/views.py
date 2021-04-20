from django.shortcuts import render
from django.urls import reverse_lazy
from apps.libro.models import Libro
from apps.libro.forms import LibroModelForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

def index_biblioteca(request):
    return render(request, 'libro/index.html')

def index_dashboard(request):
    return render(request, 'libro/dashboard.html')

def LibroLiteratura(request):
    libroT = Libro.objects.filter(tema="Literatura")
    contexto = {'libroT':libroT}
    return render(request, 'libro/libro_list.html', contexto)

def LibroMatematica(request):
    libroT = Libro.objects.filter(tema="Matemática")
    contexto = {'libroT':libroT}
    return render(request, 'libro/libro_list.html', contexto)

def LibroComunicación(request):
    libroT = Libro.objects.filter(tema="Comunicación")
    contexto = {'libroT':libroT}
    return render(request, 'libro/libro_list.html', contexto)

def LibroHistoria(request):
    libroT = Libro.objects.filter(tema="Historia")
    contexto = {'libroT':libroT}
    return render(request, 'libro/libro_list.html', contexto)

def LibroVarios(request):
    libroT = Libro.objects.filter(tema="Varios")
    contexto = {'libroT':libroT}
    return render(request, 'libro/libro_list.html', contexto)



class LibroRegistrar(CreateView):
    model = Libro
    form_class = LibroModelForm
    template_name = 'libro/libro_form.html'
    success_url = reverse_lazy('libro_listar')

class LibroListar(ListView):
    model = Libro
    template_name = 'libro/libro_list_admin.html'

class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroModelForm
    template_name = 'libro/libro_form.html'
    success_url = reverse_lazy('libro_listar')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'libro/libro_delete.html'
    success_url = reverse_lazy('libro_listar')



