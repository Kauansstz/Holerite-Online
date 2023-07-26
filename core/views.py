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

        user = User.objects.get(username=username)
        # pas = User.objects.get(password=password)

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

def menu(request):
    return render(request, 'menu.html')
# Identificar se o usuário existe