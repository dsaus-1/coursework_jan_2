from django import forms

from mailing.forms_mixins import StyleFormMixin
from mailing.models import Client, Message, Settings


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text',)
        exclude = ('owner',)


class SettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        owner = kwargs.get('owner')
        super().__init__(*args, **kwargs)


        self.fields['addressee'].queryset = Client.objects.filter(owner=owner)
        self.fields['message'].queryset = Message.objects.filter(owner=owner)

