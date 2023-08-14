from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth import login, authenticate
import banco
from cx_Oracle import IntegrityError
from aut.autenticacao import OtherSystemAuthBackend




# Create your views here.
cache.clear()
# Identificar se o usuário existe

def home(request ):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = OtherSystemAuthBackend.authenticate('', 
                                                        request, 
                                                        username=username.strip(), 
                                                        password=password, 
                                                        backend='autenticacao.criar_usuario.OtherSystemAuthBackend')
        print(user)
        if user is not None:
        # Authenticates the user in the admin session
            # login(request, user)
            return render(request, 'menu.html')
        else:
            return render(request, 'index.html', {'error_message': 'Usuário ou senha incorreto.'})
    else:  
        return render(request, 'index.html')

    


def cadastro(request):
    if request.method == 'POST' and  request.user.is_authenticated:
        # Verificar se não tem login e email duplicado
        # Verificar se não tem login e email duplicado
        nome = request.POST.get('nome')
        login = request.POST.get('nickname')
        senha = request.POST.get('pass')
        email = request.POST.get('email')
        print(nome)
        
        try:
            banco.sql_inserir(f"""INSERT INTO tb_login
                        ( nome_completo,
                            email,
                            login,
                            senha)
                        VALUES(
                            '{nome.upper()}',
                            '{email.upper()}',
                            '{login.upper()}',
                            '{senha.upper()}'
                        )""")
            
            print(login)
            return render(request, 'index.html', {'error_message':'Usuário cadastrado!' })
           
        except IntegrityError:
            return render(request, 'cadastro.html', {'error_message': 'login ou email já cadastrado!'})
    else:
        return render(request, 'cadastro.html')

# Identificar se o usuário existe
# Configuração do Menu
def menu(request):
    try:
        if request.user.is_authenticated:
            logado = request.session.get()
            print(logado)
    except UnboundLocalError:
        if logado is None:
            request.session.clear()
            return render(request, 'index.html')
        else:
            return render(request, 'menu.html')

def rendimento(request):
    if request.user.is_authenticated:
        logado = request.session.get('username')
        
        print(logado)
    if logado  is None:
        request.session.clear()
        return render(request, 'index.html')
    else:
        
        return render(request, 'rendimento.html')

def holerite(request):
        if request.user.is_authenticated:
                username = home('username')
                user = authenticate(request, username=username)
                if user is not None:
                    result = banco.sql_query(f"""SELECT COUNT(*) FROM TB_LOGIN WHERE login = '{username}'""")
                    print('result')
                    if result == 1:
                        return render(request, 'holerite.html')

                else:
                    return render(request, 'index.html')
# Configuração do Menu

# voltar
def voltar(request):
    request.session.clear()
    return render(request, 'index.html')
# voltar



