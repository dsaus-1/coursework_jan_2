from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import *

app_name = MailingConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('client/', ClientListView.as_view(), name='client'),
    path('settings/', SettingsListView.as_view(), name='settings'),
    path('create_settings/', SettingsCreateView.as_view(), name='create_settings'),
    path('update_settings/<int:pk>/', SettingsUpdateView.as_view(), name='update_settings'),
    path('delete_settings/<int:pk>/', SettingsDeleteView.as_view(), name='delete_settings'),
    path('detail_settings/<int:pk>/', SettingsDetailView.as_view(), name='detail_settings'),
    path('message/', MessageListView.as_view(), name='message'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('update_message/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),
    path('detail_message/<int:pk>/', MessageDetailView.as_view(), name='detail_message'),
    path('status/', Send_messageListView.as_view(), name='status'),
    path('delete_status/<int:pk>/', Send_messageDeleteView.as_view(), name='delete_status'),
    path('send/<int:pk>/', send, name='send'),

]