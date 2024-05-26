from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .import views


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Para obtener tokens

    path('', views.user_login, name='iniciar-sesion'),
    path('registro', views.user_signup, name='registro-usuario'),

    path('api/crear/', views.TaskCreate.as_view(), name='crear-tarea'),
    path('api/listar/', views.TaskList.as_view(), name='listar-tarea'),
    path('api/actualizar/<int:pk>', views.TaskUpdate.as_view(), name='actualizar-tarea'),
    path('api/eliminar/', views.TaskDelete.as_view(), name='eliminar-tarea'),
    path('api/task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
]