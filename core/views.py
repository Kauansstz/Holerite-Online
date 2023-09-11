from django.shortcuts import render
from django.core.cache import cache
from  database import banco
from aut.autenticacao import OtherSystemAuthBackend




# Create your views here.
cache.clear()
# Identificar se o usuário existe

def home(request ):
    if request.method == 'POST':
        registration = request.POST.get('registration')
        password = request.POST.get('password')

        user = OtherSystemAuthBackend.authenticate('', 
                                                        request, 
                                                        registration=registration.strip(), 
                                                        password=password, 
                                                        backend='autenticacao.criar_usuario.OtherSystemAuthBackend')
        print(user)
        if user is not None:
        # Authenticates the user in the admin session
            # login(request, user)
            return render(request, 'menu.html')
        else:
            return render(request, 'index.html', {'error_message': 'Mátricula ou senha incorreto.'})
    else:  
        return render(request, 'index.html')

    




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
            return render(request, 'rendimento.html')
       

def holerite(request):
        
        return render(request, 'holerite.html')

                
# Configuração do Menu

# voltar
def voltar(request):
    request.session.clear()
    return render(request, 'index.html')
# voltar



