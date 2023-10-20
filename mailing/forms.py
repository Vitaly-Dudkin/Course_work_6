from django import forms
from django.forms import ModelChoiceField

from mailing.models import MailingSettings, Client, Message


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user.is_superuser:
            self.fields['clients'].queryset = Client.objects.all()
        elif user:
            self.fields['clients'].queryset = Client.objects.filter(owner=user)
        else:
            self.fields['clients'].queryset = Client.objects.none()

    class Meta:
        model = MailingSettings
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
