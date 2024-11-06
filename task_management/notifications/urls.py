from django.urls import path
from .views import NotificationListView, NotificationCreateView, NotificationDeleteView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('create/', NotificationCreateView.as_view(), name='notification_create'),
    path('delete/<int:pk>/', NotificationDeleteView.as_view(), name='notification_delete'),
]
