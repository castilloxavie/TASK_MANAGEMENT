from django.shortcuts import render
from django.http import HttpResponse
from activite_log.models import ActiviteLog


def actividades_usuarios(request):
    usuarios = ActiviteLog.objects.all()
    return render(request, "actividades_usuarios.html", {"usuarios":  usuarios})
