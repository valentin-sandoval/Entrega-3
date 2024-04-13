from django.urls import path

from .views import (
    home_view, 
    detail_view, 
    list_view, 
    search_view,
    search_with_form_view,
    create_with_form_view,
    create_clase_with_form_view,
    detail_clase_view,
    clase_list_view,
    clase_delete_view,
    clase_update_view,
    search_clase_view,
    # VBC
    ClaseListView,
    ClaseDetailView,
    ClaseDeleteView,
    ClaseUpdateView,
    ClaseCreateView
)


urlpatterns = [
    path("", home_view),
    path("detail/<Reserve_Class_id>", detail_view),
    path("list/", list_view, name="Reserve_Class-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="zzz"),
    path("crear-reserva-con-formulario/", create_with_form_view, name="yyy"),
    path("clase/create/", create_clase_with_form_view, name="clase-create"),
    path("clase/detail/<clase_id>", detail_clase_view, name="clase-detail"),
   
   path("clase/list/", clase_list_view, name="clase-list"),
    path("clase/delete/<clase_id>", clase_delete_view, name="clase-delete"),
    path("clase/update/<clase_id>", clase_update_view, name="clase-update"),
    path("clase/buscar/", search_clase_view, name="clase-search"),
    # Vistas basadas en clases "VBC"
    path('clase/vbc/list', ClaseListView.as_view(), name='vbc_clase_list'),
    path('clase/vbc/create/', ClaseCreateView.as_view(), name='vbc_clase_create'),
    path('clase/vbc/<int:pk>/detail', ClaseDetailView.as_view(), name='vbc_clase_detail'),
    path('clase/vbc/<int:pk>/update/', ClaseUpdateView.as_view(), name='vbc_clase_update'),
    path('clase/vbc/<int:pk>/delete/', ClaseDeleteView.as_view(), name='vbc_clase_delete'),
]