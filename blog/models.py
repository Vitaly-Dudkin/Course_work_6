from django.db import models

# Create your models here.
from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='blog/', default='blog/image.png', verbose_name='Image')
    views_number = models.PositiveSmallIntegerField(default=0, verbose_name='Views number')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')

    def __str__(self):
        return f'{self.publication_date}: {self.title}'

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
