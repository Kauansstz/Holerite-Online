from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

# Identificar se o usuário existe
def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        user = User.objects.get(username=username)
        
        

    if user:
            return render(request, 'menu.html')

    else:
        return render(request, 'cadastro.html')
    

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.get(username=username)

        user = True
        if user:
         return render(request, 'cadastro.html')
        else:
            return render(request, 'index.html')

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

