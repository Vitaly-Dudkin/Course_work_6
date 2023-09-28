from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import MailingSettings, Client, Message


# Create your views here.

class OnlyForOwnerOrSuperuserMixin:
    """Миксин на проверку доступа к чужой информации"""
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


def index(request):
    object_list = MailingSettings.objects.all()
    client_list = Client.objects.distinct()

    context = {'object_list': object_list,
               'active_mailings': object_list.filter(status=MailingSettings.STATUSES[1][0]),
               'clients_list': client_list,
               }

    return render(request, 'mailing/homepage.html', context)


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра всех клиентов"""
    model = Client

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            object_list = Client.objects.all()
        else:
            object_list = Client.objects.filter(owner=user)
        return object_list


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания клиентов"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения клиентов"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра отдельного клиента"""
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления клиентов"""
    model = Client
    success_url = reverse_lazy('mailing:client')


class MailingSettingsListView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра всех настроек рассылки"""
    model = MailingSettings

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            object_list = MailingSettings.objects.all()
        else:
            object_list = MailingSettings.objects.filter(owner=user)
        return object_list


def switch_status_newsletter(request, pk):
    """Контроллер для смены статуса рассылки"""
    mailing = MailingSettings.objects.get(pk=pk)
    if mailing.status == 'started':
        mailing.status = 'finished'
    elif mailing.status == 'finished':
        mailing.status = 'started'
    mailing.save()
    return redirect('mailing:main_mailing')


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания настроек рассылки"""
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailing:main_mailing')

    def form_valid(self, form):
        user = self.request.user
        self.object = form.save()
        self.object.owner = user
        self.object.save()
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['is_create'] = True
    #     return context_data


class MailingSettingsUpdateView(LoginRequiredMixin, OnlyForOwnerOrSuperuserMixin, UpdateView):
    """Контроллер для изменения настроек рассылки"""
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailing:main_mailing')


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра отдельной настройки рассылки"""
    model = MailingSettings


class MailingSettingsDeleteView(LoginRequiredMixin, OnlyForOwnerOrSuperuserMixin, DeleteView):
    """Контроллер для удаления настроек рассылки"""
    model = MailingSettings
    success_url = reverse_lazy('mailing:main_mailing')


class MessageView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра всех сообщений"""
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра деталий сообщения"""
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageUpdateView(LoginRequiredMixin,OnlyForOwnerOrSuperuserMixin, UpdateView):
    """Контроллер для изменения сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageDeleteView(LoginRequiredMixin,OnlyForOwnerOrSuperuserMixin, DeleteView):
    """Контроллер для удаления сообщения"""
    model = Message
    success_url = reverse_lazy('mailing:message')
