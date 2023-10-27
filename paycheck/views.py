from django.shortcuts import render
from django.core.cache import cache
from database import banco
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
cache.clear()
# Identificar se o usuário existe


def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        result = banco.sql_query(
            f"""SELECT count(*) FROM TB_login email =  '{email}' and senha = '{password}' """
        )
        if result[0][0] == 1:
            # Authenticates the user in the admin session
            # login(request, user)
            register_form_data = request.session.get("register_form_data", None)
            form = RegisterForm(register_form_data)
            POST = request.POST
            request.session["register_form_data"] = POST
            form = RegisterForm(POST)
            return render(request, "panel.html")
        else:
            return render(
                request,
                "pages/home.html",
                {"error_message": "Email ou senha incorreto."},
            )
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
