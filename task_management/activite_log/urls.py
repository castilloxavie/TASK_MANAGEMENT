from django.urls import path
from .views import ActiviteLogListView, ActiviteLogCreateView, ActiviteLogUpdateView, ActiviteLogDeleteView

urlpatterns = [
    path('', ActiviteLogListView.as_view(), name='activite_log_list'),
    path('create/', ActiviteLogCreateView.as_view(), name='activite_log_create'),
    path('update/<int:pk>/', ActiviteLogUpdateView.as_view(), name='activite_log_update'),
    path('delete/<int:pk>/', ActiviteLogDeleteView.as_view(), name='activite_log_delete'),
]
