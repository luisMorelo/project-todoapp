from rest_framework import routers
from django.urls import path
from .import views

urlpatterns = [
    path('', views.iniciar_sesion, name='iniciar-sesion'),
    path('registro', views.registrarse, name='registro-usuario'),

    path('api/crear/', views.TaskCreate.as_view(), name='crear-tarea'),
    path('api/listar/', views.TaskList.as_view(), name='listar-tarea'),
    path('api/actualizar/<int:pk>', views.TaskUpdate.as_view(), name='actualizar-tarea'),
    path('api/eliminar/', views.TaskDelete.as_view(), name='eliminar-tarea'),
    path('api/task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]