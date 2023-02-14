import random

from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import *

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, SettingsForm
from mailing.models import *
from django.urls import reverse_lazy

# def home(request):
#     blog = Blog.objects.filter(publication_status=Blog.STATUS_ACTIVE)
#     blog_id = [item[0] for item in blog.values_list('id')]
#     random.shuffle(blog_id)
#     number_publication = 3
#
#     if len(blog_id) < 3:
#         number_publication = len(blog_id)
#
#     return render(request, 'mailing/home_page.html', {'blog':[blog.filter(id=blog_id[n]) for n in range(number_publication)]})


class ClientListView(UserPassesTestMixin, ListView):
    model = Client
    template_name = 'mailing/client/client_list.html'

    def test_func(self):
        return self.request.user.is_authenticated



class ClientCreateView(UserPassesTestMixin, CreateView):
    model = Client
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'
    form_class = ClientForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(ClientCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

class ClientUpdateView(UserPassesTestMixin, UpdateView):
    model = Client
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_form.html'
    form_class = ClientForm

    def test_func(self):
        client = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == client.owner

class ClientDeleteView(UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client')
    template_name = 'mailing/client/client_confirm_delete.html'

    def test_func(self):
        client = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == client.owner


class SettingsListView(UserPassesTestMixin, ListView):
    model = Settings
    template_name = 'mailing/settings/settings_list.html'

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsCreateView(UserPassesTestMixin, CreateView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'
    form_class = SettingsForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(SettingsCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

class SettingsUpdateView(UserPassesTestMixin, UpdateView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_form.html'
    form_class = SettingsForm

    def test_func(self):
        settings = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == settings.owner

class SettingsDeleteView(UserPassesTestMixin, DeleteView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_confirm_delete.html'

    def test_func(self):
        settings = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == settings.owner

class SettingsDetailView(UserPassesTestMixin, DetailView):
    model = Settings
    success_url = reverse_lazy('mailing:settings')
    template_name = 'mailing/settings/settings_detail.html'

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.owner:
            return True
        return self.request.user.has_perm('mailing.view_settings')


class MessageListView(UserPassesTestMixin, ListView):
    model = Message
    template_name = 'mailing/message/message_list.html'

    def test_func(self):
        return self.request.user.is_authenticated

class MessageCreateView(UserPassesTestMixin, CreateView):
    model = Message
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'
    form_class = MessageForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(MessageCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

class MessageUpdateView(UserPassesTestMixin, UpdateView):
    model = Message
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_form.html'
    form_class = MessageForm

    def test_func(self):
        message = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == message.owner

class MessageDeleteView(UserPassesTestMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message')
    template_name = 'mailing/message/message_confirm_delete.html'

    def test_func(self):
        message = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == message.owner

class MessageDetailView(UserPassesTestMixin, DetailView):
    model = Message
    template_name = 'mailing/message/message_detail.html'

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.owner:
            return True
        return self.request.user.has_perm('mailing.view_message')


class Send_messageListView(UserPassesTestMixin, ListView):
    model = Send_message
    template_name = 'mailing/send/send_message_list.html'

    def test_func(self):
        return self.request.user.is_authenticated

class Send_messageDeleteView(UserPassesTestMixin, DeleteView):
    model = Send_message
    success_url = reverse_lazy('mailing:status')
    template_name = 'mailing/send/send_message_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser


def change_status_settings(request, pk):
    """Смена статуса настройки"""
    obj = get_object_or_404(Settings, pk=pk)
    if obj.status == Settings.STATUS_COMPLETED or obj.status == Settings.STATUS_CREATED:
        obj.status = Settings.STATUS_LAUNCHED
    elif obj.status == Settings.STATUS_LAUNCHED:
        obj.status = Settings.STATUS_COMPLETED
    obj.save()

    return redirect(request.META.get('HTTP_REFERER'))

