from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

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
    pass


class ClientsCreateView(CreateView):
    pass


class ClientsUpdateView(UpdateView):
    pass


class ClientsDeleteView(DeleteView):
    pass
