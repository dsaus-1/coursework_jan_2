from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomLoginView, CustomRegisterView, UserEditProfileView, CustomPasswordChangeView, \
    activate_user, page_after_registration, CustomPasswordResetView, CustomPasswordResetConfirmView, \
    password_reset_send_mail, CustomPasswordResetCompleteView, UserListView, change_user_status

app_name = UsersConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(extra_context='/blog/home'), name='logout'),
    path('registration/', CustomRegisterView.as_view(), name='registration'),
    path('page_after_registration/<str:token>/', page_after_registration, name='page_after_registration'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='password'), # пытался сделать урл change_password, но что-то как-то сложно...
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_send_mail/', password_reset_send_mail, name='password_reset_send_mail'),
    path('password_reset_complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('activate/<str:token>/', activate_user, name='activate'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('status/<int:pk>/', change_user_status, name='status'),
    # path('repeat_message/<str:token>/', repeat_message, name='repeat_message'),
    # path('reset_password/', ..., name='reset_password'),

]