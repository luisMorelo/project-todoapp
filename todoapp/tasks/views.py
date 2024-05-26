from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, permissions
from .models import Task
from .serializers import taskSerializer
from django.contrib.auth.decorators import login_required
from .forms import LoginFoms, SingUpForm
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



#Iniciar sesion
def user_login(request):
    if request.method == 'post':
        form = LoginFoms(request, data=request.post)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dasboard/')
    return render(request, 'login.html')


#pagina principal
def dashboard(request):
    if request.user.is_authenticate:
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'index.html', {'full_name': full_name})
    else:
        return HttpResponseRedirect('') #redirigir a login

#registrarse
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SingUpForm(request.POST)
            if form.is_valid():
                form.save()
                HttpResponseRedirect('/login/') #redirigir a login
        else:
            form = SingUpForm()
        return render(request, 'register.html', {'form': form})
    else:
        return HttpResponseRedirect('registro')


#cerrar cesión
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def registro(request):
    return render(request, 'register.html')