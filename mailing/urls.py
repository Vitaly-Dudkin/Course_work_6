from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView, ClientListView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView, MessageView, MessageDetailView, MessageCreateView, MessageUpdateView, \
    MessageDeleteView, index, switch_status_newsletter

app_name = MailingConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('main_mailing', MailingSettingsListView.as_view(), name='main_mailing'),
    path('create_mailing/', MailingSettingsCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingSettingsUpdateView.as_view(), name='update_mailing'),
    path('detail_mailing/<int:pk>/', MailingSettingsDetailView.as_view(), name='detail_mailing'),
    path('delete_mailing/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete_mailing'),

    path('client/', ClientListView.as_view(), name='client'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('detail_client/<int:pk>/', ClientDetailView.as_view(), name='detail_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageView.as_view(), name='message'),
    path('detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('switch_status_newsletter/<int:pk>/', switch_status_newsletter, name='switch_status_newsletter'),


]
