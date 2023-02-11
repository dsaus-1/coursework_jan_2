from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    ordering = ['-date_created']

class BlogCreateView(UserPassesTestMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user
            self.object.save()
        return super(BlogCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'


    def test_func(self):
        post = self.get_object()
        if self.request.user.has_perm('blog.change_blog'):
            return True
        return self.request.user == post.owner

#
class BlogDetailView(UserPassesTestMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.number_of_views += 1
        obj.save()

        return obj

    def test_func(self):
        return self.request.user.is_authenticated

def change_post_status(request, pk):
    """Смена статуса поста"""
    obj = get_object_or_404(Blog, pk=pk)
    if obj.publication_status == Blog.STATUS_MODERATION:
        obj.publication_status = Blog.STATUS_ACTIVE
    else:
        obj.publication_status = Blog.STATUS_MODERATION
    obj.save()

    return redirect(request.META.get('HTTP_REFERER'))

