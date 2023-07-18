from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from servises.forms import ClientCreateForm, SettingCreateForm, MessagesCreateForm
from servises.models import Client, Settings, Messages, Logs
from servises.utils.utils import AutoMail
from django.utils.timezone import now


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


class SettingsListView(ListView):
    model = Settings
    template_name = 'servises/settings/settings_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['data'] = {
            'status': 'Статус',
        }
        return context


class SettingsDetailView(DetailView):
    model = Settings
    template_name = 'servises/settings/settings_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['names'] = {
            'status': 'Статус',
            'start': 'Дата начала рассылки',
            'end': 'Дата окончания рассылки',
            'periodicity': 'Периодичность',
        }
        return context


class SettingsCreateView(CreateView):
    model = Settings
    template_name = 'servises/settings/settings_create.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('servises:setting_list')


class SettingsUpdateView(UpdateView):
    model = Settings
    template_name = 'servises/settings/settings_create.html'
    form_class = SettingCreateForm
    success_url = reverse_lazy('servises:setting_list')


class SettingsDeleteView(DeleteView):
    model = Settings
    template_name = 'servises/settings/settings_delete.html'
    success_url = reverse_lazy('servises:setting_list')


class MessageListView(ListView):
    model = Messages
    template_name = 'servises/messages/message_list.html'


class MessageDetailView(DetailView):
    model = Messages
    template_name = 'servises/messages/message_detail.html'


class MessageCreateView(CreateView):
    model = Messages
    template_name = 'servises/messages/message_create.html'
    success_url = reverse_lazy('servises:message_list')
    form_class = MessagesCreateForm


class MessageUpdateView(UpdateView):
    model = Messages
    template_name = 'servises/messages/message_create.html'
    success_url = reverse_lazy('servises:message_list')
    form_class = MessagesCreateForm


class MessageDeleteView(DeleteView):
    model = Messages
    template_name = 'servises/messages/message_delete.html'
    success_url = reverse_lazy('servises:message_list')


def start_mailing(request, pk):
    context = {'result': 'Рассылка запущена'}

    data = Settings.objects.get(id=pk)
    Logs.objects.create(
        title=f'Запуск: {data.mailing_name}',
        date_last=now(),
        status='Рассылка включена',
        answer='Без ответа',
        settings=data,
    )

    a = AutoMail(data)
    return render(request, 'servises/start_mailing.html', context=context)


class LogListView(ListView):
    model = Logs
    template_name = 'servises/logs/logs.html'
