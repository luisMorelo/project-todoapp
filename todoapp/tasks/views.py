from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions
from .models import Task
from .serializers import taskSerializer
from django.contrib.auth.decorators import login_required
from .forms import LoginForms, SingUpForm, TaskForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requiere autenticación





#Iniciar sesión
def user_login(request):
    if request.method == 'GET':
        form = LoginForms()
        return render(request, 'login.html', {"form": form})
    else:
        form = LoginForms(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {"form": form, "error": "El usuario o la contraseña son incorrectos"})
        else:
            return render(request, 'login.html', {"form": form, "error": "Por favor, corrija los errores del formulario"})
    

#Crear una nueva tarea
@login_required
def crear_tarea(request):

    form = TaskForm()

    if request.method == "GET":
        return render(request, 'crear-tarea.html', {"form": form})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'crear-tarea.html', {"form": form, "error": "Error al crear tarea."})

    

#Editar tarea
@login_required
def editar_tarea(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == "GET":
        form = TaskForm(instance=task)
        return render(request, 'editar-tarea.html', {"form": form, "task": task})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'editar-tarea.html', {"form": form, "task": task, "error": "Error al editar tarea."})



#Eliminar tarea
def eliminar_tarea(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('dashboard')  # redirige a la lista de tareas después de eliminar

    return render(request, 'eliminar-tarea.html', {'task': task})


#Lista de tareas y dashboart
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'index.html', { 'tasks': tasks })





#registrarse
def user_signup(request):

    form = SingUpForm()
    if request.method == 'GET':
        return render(request,'register.html', {
            'form': form
        })
    else:
        if request.method == 'POST':

            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                user.save()
                login(request, user)
                
                return render(request, 'register.html', {'form': form, 'exito': '¡El usuario fue creado exitósamente!'})
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Las contraseñas no coinciden, verifica e intentalo de nuevo'})
