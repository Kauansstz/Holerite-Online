from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import login
import banco

# Create your views here.

# Identificar se o usuário existe
def home(request, ):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        resultado = banco.sql_query(f"""SELECT COUNT(*) FROM tabela_login WHERE login  = '{username.upper()}' and senha = '{password.upper()}'""")
        print(username, password)
        if resultado[0][0] == 1:
            return render(request, 'menu.html')
        else:
            return render(request, 'index.html', {'error_message': 'Usuário ou senha incorreto.'})
    else:  
        return render(request, 'index.html')


        
    # if request.method == 'GET':
    #     return render(request, 'index.html')
    # else:
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     print(username)
    #     print(password)
       
        
    # user = authenticate(request, username=username, password=password)
        
    # if user is not None:
    #         # Se o usuário e a senha estiverem corretos, faça o login do usuário
    #     login(request, user)
    #     return render(request, 'menu.html')
    # else:
    #         # Se o usuário ou a senha estiverem incorretos, renderize o template de login novamente
    #     return render(request, 'index.html', {'error_message': 'Usuário ou senha incorreto.'})
    
        
def cadastro(request):
    return render(request, 'cadastro.html')

   
def incluir(nome, email, login, senha):
    banco.sql_inserir(f"""INSERIR INTO tabela_login
                      ( nome,
                        email,
                        login,
                        senha)
                      VALUES(
                        {nome},
                        {email},
                        {login},
                        {senha}
                      )""")

# Identificar se o usuário existe
# Configuração do Menu
def menu(request):
    return render(request, 'menu.html')

def cartegoria(request):
    return render(request, 'cartegoria.html')

def configuracao(request):
    return render(request, 'configuracao.html')

# def usuario(request):
#     return render(request, 'usuario.html')
# Configuração do Menu

# Cadastramento
def voltar(request):
    return render(request, 'index.html')

# Cadastramento

