from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name='home'),
    path('client_detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('add_client/', views.AddClientView.as_view(), name='add_client'),
    path('edit_client/<int:pk>/', views.EditClientView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>/', views.DeleteClientView.as_view(), name='delete_client')
]