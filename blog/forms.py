from blog.models import Blog
from mailing.forms_mixins import StyleFormMixin
from django import forms


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('header', 'content', 'image_preview', )

    def clean_header(self):
        header = self.cleaned_data['header']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'алкоголь', 'сигареты', 'табак']

        for word in stop_word:
            if word in header:
                raise forms.ValidationError('Данная тема противоречит политике сайта')

        return header

    def clean_content(self):
        content = self.cleaned_data['content']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'алкоголь', 'сигареты', 'табак']

        for word in stop_word:
            if word in content:
                raise forms.ValidationError('Контент содержит слова, противоречащие политике сайта')

        return content