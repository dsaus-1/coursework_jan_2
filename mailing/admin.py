from django.contrib import admin
from mailing.models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fio', 'comment',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', )
    list_filter = ('title',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'frequency', 'status', 'message',)
    list_filter = ('frequency', 'status', 'message',)


@admin.register(Send_message)
class Send_messageAdmin(admin.ModelAdmin):
    list_display = ('sending_time', 'status', 'server_response', 'settings_pk',)
    list_filter = ('status', 'server_response', )