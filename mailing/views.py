from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailing.forms import MailingForm, ClientForm, MessageForm
from mailing.models import MailingSettings, Client, Message


# Create your views here.

class OnlyForOwnerOrSuperuserMixin:

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
    model = Client

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            object_list = Client.objects.all()
        else:
            object_list = Client.objects.filter(owner=user)
        return object_list


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client')


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            object_list = MailingSettings.objects.all()
        else:
            object_list = MailingSettings.objects.filter(owner=user)
        return object_list


def switch_status_newsletter(request, pk):
    mailing = MailingSettings.objects.get(pk=pk)
    if mailing.status == 'started':
        mailing.status = 'finished'
    elif mailing.status == 'finished':
        mailing.status = 'started'
    mailing.save()
    return redirect('mailing:main_mailing')


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
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
    model = MailingSettings
    form_class = MailingForm
    success_url = reverse_lazy('mailing:main_mailing')


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingSettingsDeleteView(LoginRequiredMixin, OnlyForOwnerOrSuperuserMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:main_mailing')


class MessageView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageUpdateView(LoginRequiredMixin,OnlyForOwnerOrSuperuserMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message')


class MessageDeleteView(LoginRequiredMixin,OnlyForOwnerOrSuperuserMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
