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
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[:50]


