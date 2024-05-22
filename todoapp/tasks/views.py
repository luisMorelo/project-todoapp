from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import generics
from .models import Task
from .serializers import taskSerializer

# Create your views here.

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            # Mensaje de error si la autenticación falla
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')
    

def registrarse(request):
    return render(request, 'register.html')
