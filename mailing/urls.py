from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingSettingsView, MailingSettingsCreateView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView, ClientListView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingSettingsView.as_view(), name='home'),
    path('create_mailing/', MailingSettingsCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingSettingsUpdateView.as_view(), name='update_mailing'),
    path('detail_mailing/<int:pk>/', MailingSettingsDetailView.as_view(), name='detail_mailing'),
    path('delete_mailing/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete_mailing'),

    path('client/', ClientListView.as_view(), name='client'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('detail_client/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

]
