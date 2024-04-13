from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reserva, Clase
from  .forms import ReservaCreateForm, ReservaSearchForm, ClaseCreateForm

def create_with_form_view(request):
    contexto = {"create_form": ReservaCreateForm() }
    return render(request, "Reserve_Class/form-create.html", contexto)


def create_clase_with_form_view(request):
    if request.method == "GET":
        contexto = {"LUISMIGUEL": ClaseCreateForm()}
        return render(request, "Reserve_Class/form-create-clase.html", contexto)
    elif request.method == "POST":
        form = ClaseCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            capacidad = form.cleaned_data['capacidad']
            descripcion = form.cleaned_data['descripcion']
            nueva_clase = Clase(nombre=nombre, disponible=disponible, capacidad=capacidad, descripcion=descripcion)
            nueva_clase.save()
            return detail_clase_view(request, nueva_clase.id)


def home_view(request):
    return render(request, "Reserve_Class/home.html")


def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'todas_las_reservas': reservas}
    return render(request, "Reserve_Class/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "Reserve_Class/list.html", contexto_dict)


def search_with_form_view(request):
    if request.method == "GET":
        form = ReservaSearchForm()
        return render(request, "Reserve_Class/form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
        reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"todas_las_reservas": reservas_del_usuario}
        return render(request, "Reserve_Class/list.html", contexto_dict)


def detail_view(request, Reserve_Class_id):
    reserva = Reserva.objects.get(id=Reserve_Class_id)
    contexto_dict = {"reserva": reserva}
    return render(request, "Reserve_Class/detail.html", contexto_dict)


def detail_clase_view(request, clase_id):
    clase = Clase.objects.get(id=clase_id)
    contexto_dict = {"clase": clase}
    return render(request, "Reserve_Class/detail-clase.html", contexto_dict)

# CRUD

def clase_list_view(request):
    todas_las_clases = Clase.objects.all()
    contexto = {"SANTIAGOMOTORIZADO": todas_las_clases}
    return render(request, "Reserve_Class/clase/list.html", contexto)


def clase_delete_view(request, clase_id):
    clase_a_borrar = Clase.objects.filter(id=clase_id).first()
    clase_a_borrar.delete()
    return redirect("clase-list")


def clase_update_view(request, clase_id):
    clase_a_editar = Clase.objects.filter(id=clase_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": clase_a_editar.nombre,
            "disponible": clase_a_editar.disponible,
            "capacidad": clase_a_editar.capacidad,
            "descripcion": clase_a_editar.descripcion
        }
        formulario = ClaseCreateForm(initial=valores_iniciales)
        contexto = {
            "ENRIQUE": formulario,
            "OBJETO": clase_a_editar
        }
        return render(request, "Reserve_Class/clase/form_update.html", contexto)
    elif request.method == "POST":
        form = ClaseCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            capacidad = form.cleaned_data['capacidad']
            descripcion = form.cleaned_data['descripcion']
            clase_a_editar.nombre = nombre
            clase_a_editar.disponible = disponible
            clase_a_editar.capacidad = capacidad
            clase_a_editar.descripcion = descripcion
            clase_a_editar.save()
            return redirect("clase-detail", clase_a_editar.id)


def search_clase_view(request):
    return HttpResponse("not implemented!")



from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, SearchView

class ClaseListView(ListView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_list.html'
    context_object_name = 'ADRIANDARGELOS'


class ClaseDetailView(DetailView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_detail.html'
    context_object_name = 'GUSTAVOCERATI'


class ClaseCreateView(CreateView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_form.html'
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    success_url = reverse_lazy('vbc_clase_list')


class ClaseUpdateView(UpdateView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_form.html'
    fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
    context_object_name = 'clase'
    success_url = reverse_lazy('vbc_clase_list')


class ClaseDeleteView(DeleteView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_confirm_delete.html'
    success_url = reverse_lazy('vbc_clase_list')

class ClaseSearchView(SearchView):
    model = Clase
    template_name = 'Reserve_Class/vbc/clase_search.html'
    success_url = reverse_lazy('vbc_clase_search')
