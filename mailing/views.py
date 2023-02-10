from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from mailing.models import *
from django.urls import reverse_lazy, reverse

def home(request):
    return render(request, 'mailing/home_page.html')


class ClientListView(UserPassesTestMixin, ListView):
    model = Client
    template_name = 'mailing/client/client_list.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated



class ClientCreateView(UserPassesTestMixin, CreateView):
    model = Client
    fields = ('email', 'fio', 'comment')
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class ClientUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    fields = ('email', 'fio', 'comment')
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_confirm_delete.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated


class SettingsListView(UserPassesTestMixin, ListView):
    model = Settings
    template_name = 'mailing/settings/settings_list.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsCreateView(UserPassesTestMixin, CreateView):
    model = Settings
    fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsUpdateView(UserPassesTestMixin, UpdateView):
    model = Settings
    fields = ('mailing_time', 'frequency', 'status', 'message', 'addressee')
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsDeleteView(UserPassesTestMixin, DeleteView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_confirm_delete.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsDetailView(UserPassesTestMixin, DetailView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_detail.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated


class MessageListView(UserPassesTestMixin, ListView):
    model = Message
    template_name = 'mailing/message/message_list.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class MessageCreateView(UserPassesTestMixin, CreateView):
    model = Message
    fields = ('title', 'text')
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class MessageUpdateView(UserPassesTestMixin, UpdateView):
    model = Message
    fields = ('title', 'text')
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_confirm_delete.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class MessageDetailView(UserPassesTestMixin, DetailView):
    model = Message
    template_name = 'mailing/message/message_detail.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated


class Send_messageListView(UserPassesTestMixin, ListView):
    model = Send_message
    template_name = 'mailing/send/send_message_list.html'
    login_url = '/users/login'

    def test_func(self):
        return self.request.user.is_authenticated

class Send_messageDeleteView(DeleteView):
    model = Send_message
    success_url = reverse_lazy('mailing:status')
    template_name = 'mailing/send/send_message_confirm_delete.html'

#
# def send(request, pk):
#     obj_mail = get_object_or_404(Message, pk=pk)
#     # if obj_mail.settings.status == 'не доставлено':
#     #     if obj_mail.settings.mailing_time
#     mail_list = obj_mail.addressee.all()
#
#     for num in range(len(mail_list)):
#
#         send_mail(
#             subject=obj_mail.title,
#             message=obj_mail.text,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[mail_list[num].email],
#         )
#
#     return redirect(reverse('mailing:detail_message', kwargs={'pk':pk}))
#

# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'mailing/register_form.html'
#     success_url = reverse_lazy('mailing:login')
