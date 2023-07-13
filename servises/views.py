from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from servises.forms import ClientCreateForm
from servises.models import Client


def start_page(request):
    context = {
        'title': 'Стартовая',
    }
    return render(request, 'servises/index.html', context=context)


def test_view(requests):
    return render(requests, 'servises/test.html')


def main_page(requests):
    return render(requests, 'servises/main_page.html')


class ClientsListView(ListView):
    model = Client
    template_name = 'servises/clients/client_list.html'


class ClientsDetailView(DetailView):
    model = Client
    template_name = 'servises/clients/client_detail.html'


class ClientsCreateView(CreateView):
    model = Client
    template_name = 'servises/clients/client_create.html'
    form_class = ClientCreateForm
    success_url = reverse_lazy('servises:clients')


class ClientsUpdateView(UpdateView):
    model = Client
    template_name = 'servises/clients/client_create.html'
    form_class = ClientCreateForm
    success_url = reverse_lazy('servises:clients')


class ClientsDeleteView(DeleteView):
    model = Client
    template_name = 'servises/clients/client_delete.html'
    success_url = reverse_lazy('servises:clients')





