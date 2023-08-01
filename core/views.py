from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import login

# Create your views here.

# Identificar se o usuário existe
def home(request):
    # try:
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
       
        
    user = authenticate(request, username=username, password=password)
        
    if user is not None:
            # Se o usuário e a senha estiverem corretos, faça o login do usuário
        login(request, user)
        return render(request, 'menu.html')
    else:
            # Se o usuário ou a senha estiverem incorretos, renderize o template de login novamente
        return render(request, 'index.html', {'error_message': 'Usuário ou senha incorreto.'})
    
        
def cadastro(request):
   return render(request, 'cadastro.html')
        
def login(request):
    nv_usuario = login()
    nv_usuario.nome = request.POST.get('nome')
    nv_usuario.email = request.POST.get('email')
    nv_usuario.user = request.POST.get('nickname')
    nv_usuario.password = request.POST.get('pass')
    nv_usuario.save()
# Identificar se o usuário existe
# Configuração do Menu
def menu(request):
    return render(request, 'menu.html')

def cartegoria(request):
    return render(request, 'cartegoria.html')

def configuracao(request):
    return render(request, 'configuracao.html')

def usuario(request):
    return render(request, 'usuario.html')
# Configuração do Menu

# Cadastramento
def voltar(request):
    return render(request, 'index.html')

# Cadastramento

