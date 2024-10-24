from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Produto
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *

from django.contrib.auth import login,logout,authenticate


#Serve como um protetor no qual nao vai permitir interceptacoes no meio da requisicao do
#usuario
@login_required
@csrf_exempt
@require_http_methods(["GET"])
def buscar_todos_os_produtos(request):
    produtos = Produto.objects.all().values() #pegando todos os objetos Produto
    return render(request,'app/template_produto.html',{'lista_de_produtos':produtos})

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        formulario = ProdutoForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('rota_lista_de_produtos')
    else:
        formulario = ProdutoForm()
    
    return render(request,'app/cadastrar_produto.html', {'formulario_de_cadastrar_produto':formulario})        
   

@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        
        formulario_usuario = UserCreationForm(request.POST)
        
        if formulario_usuario.is_valid():
            formulario_usuario.save()
            
            return redirect('rota_login')
    else:
        formulario_usuario = UserCreationForm()
    
    return render(request,'app/cadastro_usuario.html', {'formulario_de_cadastro_do_usuario':formulario_usuario})

@login_required
def login_usuario(request):
    if request.method == 'POST':
        
        formulario_de_login = AuthenticationForm(data = request.POST)
        
        if formulario_de_login.is_valid():
            username = formulario_de_login.cleaned_data.get('username')
            senha = formulario_de_login.cleaned_data.get('password')
            
            usuario = authenticate(username = username, password = senha)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('rota_de_cadastrar_produto')
    else:
        formulario_de_login = AuthenticationForm()
        
    return render(request,'app/login_de_usuario.html', {'formulario_de_login':formulario_de_login})