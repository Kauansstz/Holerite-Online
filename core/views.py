from django.shortcuts import render
from django.contrib.auth import authenticate
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

    
        
def cadastro(request):
    if request.method == 'POST':
        # Verificar se não tem login e email duplicado
        username = request.POST.get('username')
        mail = request.POST.get('email')
        consulta_user = banco.sql_query(f"""SELECT COUNT(*) FROM tabela_login WHERE login  = '{username.upper()}""")
        consulta_mail = banco.sql_query(f"""SELECT COUNT(*) FROM tabela_login WHERE email = '{mail.upper()}'""")
        # Verificar se não tem login e email duplicado
        nome = request.POST.get('name')
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        print(username)
        if consulta_user[0][0] == 1:
            return render(request, 'cadastro.html', {'error_menssage': 'Usuário ja cadastrado'})
        if consulta_mail[0][0] == 1:
            return render(request, 'cadastro.html', {'error_menssage': 'Email já cadastrado'})
        else:
            banco.sql_inserir(f"""INSERIR INTO tabela_login
                      ( nome,
                        email,
                        login,
                        senha)
                      VALUES(
                        {nome.upper()},
                        {email.upper()},
                        {login.upper()},
                        {senha.upper()}
                      )""")
            
    else:
        return render(request, 'cadastro.html')

   
# def incluir(nome, email, login, senha):
#     banco.sql_inserir(f"""INSERIR INTO tabela_login
#                       ( nome,
#                         email,
#                         login,
#                         senha)
#                       VALUES(
#                         {nome},
#                         {email},
#                         {login},
#                         {senha}
#                       )""")

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

