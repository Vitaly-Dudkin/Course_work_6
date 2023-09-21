from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingSettingsView, MailingSettingsCreateView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingSettingsView.as_view(), name='home'),
    path('create/', MailingSettingsCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MailingSettingsUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', MailingSettingsDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete'),
]
