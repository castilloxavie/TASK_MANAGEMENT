from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ActiviteLog
from .form import ActiviteLogForm

class ActiviteLogListView(ListView):
    model = ActiviteLog
    template_name = 'activite_log/activite_log_list.html'

class ActiviteLogCreateView(CreateView):
    model = ActiviteLog
    form_class = ActiviteLogForm
    template_name = 'activite_log/activite_log_form.html'
    success_url = '/activite_log/'

class ActiviteLogUpdateView(UpdateView):
    model = ActiviteLog
    form_class = ActiviteLogForm
    template_name = 'activite_log/activite_log_form.html'
    success_url = '/activite_log/'

class ActiviteLogDeleteView(DeleteView):
    model = ActiviteLog
    template_name = 'activite_log/activite_log_confirm_delete.html'
    success_url = '/activite_log/'