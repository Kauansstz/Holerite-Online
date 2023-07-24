from django.urls import path
from .views import home
from django.conf.urls.static import static
from django.conf import settings

# from .views import index

urlpatterns = [
    path('', home, name='index'),
    path('usuarios/',home, name='menu'),
    # static('index', index, name='index')
]