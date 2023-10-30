from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages
from django.http import Http404

# Create your views here.
cache.clear()
# Identificar se o usuário existe


def home(request):
    try:
        register_form_data = request.session.get("register_form_data", None)
        data = RegisterForm(register_form_data)
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return (request, "pages/panel.html")
            else:
                return render(
                    request,
                    "pages/home.html",
                    {"error_message": "Email ou senha incorreto."},
                )
        else:
            return render(request, "pages/home.html", {"form": data})
    except:
        raise Http404("Ocorreu algo inesperado, Favor entrar em contato com a TI")


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
