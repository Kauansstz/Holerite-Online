from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)

        user = User.objects.get(username=username)

    if user:
        print('Ja existe')

    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
def menu(request):
    return render(request, 'menu.html')