from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    path("", views.home, name="home"),
    path("symbol_list", views.symbol_list, name="symbol_list"),
]