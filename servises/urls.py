from django.urls import path

from servises.views import start_page, test_view, main_page, ClientsListView, ClientsDetailView, ClientsCreateView, \
    ClientsUpdateView, ClientsDeleteView

app_name = 'servises'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('test/', test_view, name='test_view'),
    path('start/', main_page, name='main_page'),
    path('clients/', ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientsDetailView.as_view(), name='client'),
    path('clients/new/', ClientsCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientsUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientsDeleteView.as_view(), name='client_delete'),
]
