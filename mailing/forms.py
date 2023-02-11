from django import forms

from mailing.forms_mixins import StyleFormMixin
from mailing.models import Client, Message, Settings


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class SettingsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')