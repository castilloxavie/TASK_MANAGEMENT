"""
    Modelo que representa una tarea asociada a un usuario.

    Atributos:
    user (ForeignKey): Relación con el modelo User; permite asignar la tarea a un usuario.
    title (CharField): Título de la tarea, máximo 200 caracteres.
    description (TextField): Descripción detallada de la tarea.
    priority (IntegerField): Prioridad de la tarea; opciones son: 
        1 (Alto), 2 (Medio), 3 (Bajo).
    status (IntegerField): Estado de la tarea; opciones son: 
        1 (Terminado), 2 (En proceso), 3 (Pendiente).
    created_at (DateTimeField): Fecha y hora de creación, se establece automáticamente al crear la tarea.

    Métodos:
    __str__(): Devuelve el título de la tarea.
"""

from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.IntegerField(choices=[
        (1, "Alto"), 
        (2, "Medio"), 
        (3, "Bajo")
    ])
    status =  models.IntegerField(choices=[
        (1, "Termidado"), 
        (2, "En proceso"),  
        (3, "Pendiente")
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def  __str__(self):
        return self.title


