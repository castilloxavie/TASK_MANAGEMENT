"""
    Modelo que representa un informe asociado a una tarea realizada por un usuario.

    Atributos:
    user (ForeignKey): Relación con el modelo User; indica qué usuario generó el informe.
    task (ForeignKey): Relación con el modelo Task; indica a qué tarea se refiere el informe.
    report_data (TextField): Contenido del informe, permite texto extenso.
    generated_at (DateTimeField): Fecha y hora en que se generó el informe, se establece automáticamente.

    Métodos:
    __str__(): Devuelve una cadena con información sobre la tarea, el usuario y la fecha de generación del informe.
"""

from django.db import models
from django.contrib.auth.models import User
from tasks.models import  Task

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    report_data = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report for task {self.task.id} by user {self.user.username} at {self.generated_at}"

