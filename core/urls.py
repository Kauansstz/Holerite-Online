from django.urls import path
from .views import home, menu, holerite, configuracao, cadastro, rendimento
from django.contrib.auth import views




# from .views import index

urlpatterns = [
    path('', home, name='index'),
    path('menu/',menu, name='menu'),
    path('cadastro',cadastro, name='cadastro'),
    path('configuracao', configuracao, name='configuracao'),
    path('holerite',holerite, name='holerite'),
    path('rendimento',rendimento, name='rendimento'),
    path('logout/', views.LogoutView.as_view(next_page='index'), name='logout'),
    
    
    # static('index', index, name='index')
]