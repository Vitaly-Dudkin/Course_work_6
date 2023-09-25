from django import forms
from blog.models import Blog


class BlogEntryForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('views_number', 'publication_date')
