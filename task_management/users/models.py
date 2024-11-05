"""
    Modelo que representa el perfil del usuario extendiendo el modelo User.
    
    Atributos:
    user (OneToOneField): Relación uno a uno con el modelo User.
    bio (TextField): Biografía del usuario, texto opcional con un máximo de 500 caracteres.
    is_active (BooleanField): Valida si esta activo el Usuario
    
    Métodos:
    __str__(): Devuelve el nombre de usuario asociado.
"""
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.user.username
