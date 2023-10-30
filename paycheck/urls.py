from django.urls import path
from .views import home, menu, holerite, rendimento
from django.contrib.auth import views


# from .views import index

urlpatterns = [
    path("", home, name="home"),  # type: ignore
    path("menu/", menu, name="panel"),
    path("holerite/", holerite, name="holerite"),
    path("rendimento/", rendimento, name="rendimento"),
    path("logout/", views.LogoutView.as_view(next_page="index"), name="logout"),
    # static('index', index, name='index')
]
