from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client
from django.urls import reverse_lazy


class ClientListView(ListView):
    model = Client
    template_name = 'home.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class AddClientView(CreateView):
    model = Client
    template_name = 'add_client.html'
    fields = '__all__'


class EditClientView(UpdateView):
    model = Client
    template_name = 'edit_client.html'
    fields = '__all__'


class DeleteClientView(DeleteView):
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('home')
