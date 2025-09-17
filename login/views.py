from django.shortcuts import render
from django.http import HttpResponse
from . import templates 

# Create your views here.
def hola (request):
    return HttpResponse("<h1> Hola Mundo desde Django </h1>")

def login (request):
    return render(request, 'login.html')

def crear_usuario (request):
    return render(request, 'crear-user.html')

def recuperar_contrasena (request):
    return render(request, 'recup-pass.html')

def validar_codigo (request):
    return render(request, 'newcode.html')

def nueva_contrasena (request):
    return render(request, 'newpass.html')

def admin_panel (request):
    return render(request, 'admin_panel.html')





