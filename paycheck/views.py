from django.shortcuts import render
from django.core.cache import cache
from database import banco

# from aut.autenticacao import OtherSystemAuthBackend
# from django.contrib.sessions import base_session


# Create your views here.
cache.clear()
# Identificar se o usuário existe


def home(request):
    if request.method == "POST":
        return render(request, "pages/panel.html")
    # else:
    #     return render(
    #         request,
    #         "pages/home.html",
    #         {"error_message": "Matrícula ou senha incorreto."},
    else:
        return render(request, "pages/home.html")


# Identificar se o usuário existe
# Configuração do Menu
def menu(request):
    return render(request, "pages/panel.html")


def rendimento(request):
    return render(request, "pages/performance.html")


def holerite(request):
    return render(request, "pages/holerite.html")


# Configuração do Menu


# voltar
def voltar(request):
    request.session.clear()
    return render(request, "index.html")


# voltar
