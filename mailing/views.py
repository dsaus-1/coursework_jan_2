from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from mailing.models import *
from django.urls import reverse_lazy, reverse

def home(request):
    return render(request, 'mailing/home_page.html')


class ClientListView(ListView):
    model = Client
    template_name = 'mailing/client/client_list.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'fio', 'comment')
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'

class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'fio', 'comment')
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_confirm_delete.html'


class SettingsListView(ListView):
    model = Settings
    template_name = 'mailing/settings/settings_list.html'

class SettingsCreateView(CreateView):
    model = Settings
    fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'

class SettingsUpdateView(UpdateView):
    model = Settings
    fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'

class SettingsDeleteView(DeleteView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_confirm_delete.html'

class SettingsDetailView(DetailView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_detail.html'


class MessageListView(ListView):
    model = Message
    template_name = 'mailing/message/message_list.html'

class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'text')
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'

class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text')
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'

class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_confirm_delete.html'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing/message/message_detail.html'


class Send_messageListView(ListView):
    model = Send_message
    template_name = 'mailing/send/send_message_list.html'

class Send_messageDeleteView(DeleteView):
    model = Send_message
    success_url = reverse_lazy('mailing:status')
    template_name = 'mailing/send/send_message_confirm_delete.html'


def send(request, pk):
    obj_mail = get_object_or_404(Message, pk=pk)
    # if obj_mail.settings.status == 'не доставлено':
    #     if obj_mail.settings.mailing_time
    mail_list = obj_mail.addressee.all()

    for num in range(len(mail_list)):

        send_mail(
            subject=obj_mail.title,
            message=obj_mail.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[mail_list[num].email],
        )

    return redirect(reverse('mailing:detail_message', kwargs={'pk':pk}))


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'mailing/register_form.html'
#     success_url = reverse_lazy('mailing:login')
