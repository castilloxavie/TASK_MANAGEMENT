from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Task
from .form  import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"
    
class TaskCreateView(CreateView):
    model = Task
    template_name = "task/task_form.html"
    success_url =  reverse_lazy("task_list")

class TaskUpdateView(UpdateView):
    model  = Task
    template_name = "task/task_form.html"
    form_name = TaskForm
    success_url =   reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")