"""
    Modelo que registra las actividades realizadas por los usuarios en tareas.

    Atributos:
    user (ForeignKey): Relación con el modelo User; indica qué usuario realizó la acción.
    task (ForeignKey): Relación con el modelo Task; indica a qué tarea se refiere la acción.
    action (CharField): Descripción de la acción realizada, máximo 200 caracteres.
    timestamp (DateTimeField): Fecha y hora en que se registró la acción, se establece automáticamente.

    Métodos:
    __str__(): Devuelve una cadena con información sobre el usuario, la acción y la fecha de registro.
"""

from django.db import models
from django.contrib.auth.models import User
from tasks.models  import Task

class ActiviteLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Usuario:{self.user.username},  Accion: {self.action}, Fecha: {self.timestamp}"
