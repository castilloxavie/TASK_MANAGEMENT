from django.views.generic import ListView, CreateView, DeleteView
from .models import Notification
from .forms import NotificationForm

class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications/notification_list.html'

class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notifications/notification_form.html'
    success_url = '/notifications/'

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notifications/notification_confirm_delete.html'
    success_url = '/notifications/'

