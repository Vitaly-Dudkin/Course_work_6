from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    """
    Контроллер для просмотра объектов Blog
    """
    model = Blog


class BlogDetailView(DetailView):
    """
     Контроллер для просмотра отдельного объекта Blog
     """
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_number += 1
        self.object.save()

        return self.object


class BlogDeleteView(DeleteView):
    """
    Контроллер для удвления объекта Blog
    """
    model = Blog

    success_url = reverse_lazy('blog:blog')


class BlogCreateView(CreateView):
    """
      Контроллер для создания объекта Blog
      """
    model = Blog

    form_class = BlogForm
    success_url = reverse_lazy('blog:blog')


class BlogUpdateView(UpdateView):
    """
    Контроллер для изменения объекта Blog
    """
    model = Blog

    success_url = reverse_lazy('blog:blog')
    form_class = BlogForm
