from django.urls import path

from servises.views import start_page, test_view, main_page, ClientsListView

app_name = 'servises'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('test/', test_view, name='test_view'),
    path('start/', main_page, name='main_page'),
    path('clients/', ClientsListView.as_view(), name='clients'),
]
