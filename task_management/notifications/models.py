"""
    Modelo que representa una notificación relacionada con una tarea.

    Atributos:
    task (ForeignKey): Relación con el modelo Task; indica a qué tarea está asociada la notificación.
    message (CharField): Mensaje de la notificación, máximo 255 caracteres.
    created_at (DateTimeField): Fecha y hora en que se creó la notificación, se establece automáticamente.

    Métodos:
    __str__(): Devuelve el mensaje de la notificación.
"""

from django.db import models
from tasks.models import  Task


class Notification(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message

