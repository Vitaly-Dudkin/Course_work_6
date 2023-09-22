from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import MailingSettings, Client, Message


# Create your views here.
class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client')


class MailingSettingsView(ListView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')


class MailingSettingsDetailView(DetailView):
    model = MailingSettings

    # def get_success_url(self):
    #     return reverse('mailing:home', args=[self.kwargs.get('pk')])


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:home')


class MessageView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
