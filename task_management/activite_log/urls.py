from django.urls import path
from  . import views

urlpatterns = [
    path("actividades_usuarios/",  views.actividades_usuarios, name="actividades_usuarios"),
]