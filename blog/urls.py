
from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, change_post_status

app_name = BlogConfig.name

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('change_post_status/<int:pk>/', change_post_status, name='change_post_status'),
]