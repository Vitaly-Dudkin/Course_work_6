from django.contrib import admin

from mailing.models import Client, Message, MailingSettings, MailingLog


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'comment', 'phone')
    search_fields = ('full_name', 'email')
    list_filter = ('full_name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'body')
    search_fields = ('subject',)
    list_filter = ('subject',)


@admin.register(MailingSettings)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'interval', 'status', 'message')
    search_fields = ('start_time', 'end_time', 'interval', 'status', 'message')
    list_filter = ('start_time', 'end_time', 'interval', 'status', 'message')


@admin.register(MailingLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status', 'server_response', 'client', 'mailing')
    search_fields = ('last_try', 'status', 'server_response')
    list_filter = ('last_try', 'status', 'server_response')
