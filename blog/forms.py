from blog.models import Blog
from mailing.forms_mixins import StyleFormMixin
from django import forms


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('header', 'content', 'image_preview', )