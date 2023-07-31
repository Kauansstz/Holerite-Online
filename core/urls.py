from django.urls import path
from .views import home, menu, cartegoria, configuracao, cadastro, voltar
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings

# from .views import index

urlpatterns = [
    path('', home, name='index'),
    path('menu',menu, name='menu'),
    path('cadastro',cadastro, name='cadastro'),
    path('configuracao', configuracao, name='configuracao'),
    path('cartegoria',cartegoria, name='cartegoria'),
    # path('menu',voltar, name='voltar'),
    path('logout/', views.LogoutView.as_view(next_page='index'), name='logout'),
    
    
    # static('index', index, name='index')
]