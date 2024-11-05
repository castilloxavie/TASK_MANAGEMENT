"""
    Modelo que representa una etiqueta que puede ser asignada a múltiples tareas.

    Atributos:
    name (CharField): Nombre de la etiqueta, máximo 50 caracteres.
    tasks (ManyToManyField): Relación de muchos a muchos con el modelo Task; permite 
    asociar múltiples tareas a una etiqueta y múltiples etiquetas a una tarea.

    Métodos:
    __str__(): Devuelve el nombre de la etiqueta.
"""

from django.db import models
from tasks.models import Task

class Tag(models.Model):
    name = models.CharField(max_length=50)
    tasks = models.ManyToManyField(Task, related_name='tags')
    
    def __str__(self):
        return self.name
