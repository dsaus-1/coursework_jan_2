from django.contrib import admin
from mailing.models import *


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('frequency',)


@admin.register(Status_settings)
class Status_settingsAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Sending_status)
class Sending_statusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fio', 'comment',)
    search_fields = ('email', 'fio',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('mailing_time', 'frequency', 'status',)
    search_fields = ('status', )
    list_filter = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'settings', )
    search_fields = ('title', )
    #list_filter = ('addressee',)


@admin.register(Send_message)
class Send_messageAdmin(admin.ModelAdmin):
    list_display = ('sending_time', 'status', 'server_response', 'message', )
    search_fields = ('status', 'message', )
    list_filter = ('message', 'status', )