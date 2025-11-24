from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirige la raíz a lista_tareas
    path('', RedirectView.as_view(url='lista_tareas/', permanent=False), name='home'),
    
    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    
    # Tareas
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('agregar_tarea/', views.agregar_tarea, name='agregar_tarea'),
    path('detalle_tarea/<int:tid>/', views.detalle_tarea, name='detalle_tarea'),
    path('eliminar_tarea/<int:tid>/', views.eliminar_tarea, name='eliminar_tarea'),
]