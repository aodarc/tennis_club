from django.contrib.auth.models import User
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Image(models.Model):
    img = models.ImageField(blank=False,upload_to='images/%Y/%m')
    name = models.CharField(max_length=30, verbose_name='Опис', help_text='Цей текст буде вставлений до атрибуту alt')

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=25, blank=False, db_index=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class News(models.Model):
    author = models.ForeignKey(to=User, blank=False)

    blog_news_img = models.ForeignKey(to=Image, related_name='news')

    title = models.CharField(max_length=150, blank=False, db_index=True, unique=True, verbose_name='Заголовок')
    content = RichTextUploadingField(blank=False, verbose_name='Наповнення')
    description = models.CharField(max_length=255, blank=False, verbose_name='Опис')

    created = models.DateField(auto_now_add=True, verbose_name='Дата створення')

    tags = models.ManyToManyField(to=Tag, blank=True, verbose_name='Теги')

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ('-created',)

    def __str__(self):
        return self.title_uk


class Comment(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=30, blank=False, verbose_name="Ім'я")
    massage = models.TextField(max_length=1000, blank=False, verbose_name='Відгук')
    created = models.DateTimeField(auto_now_add=True, blank=False, verbose_name='Створений')
    is_approve = models.BooleanField(default=False, blank=False, db_index=True, verbose_name='Відображати?')
    # TODO overide on_delete method
    post = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ('-created',)

    def __str__(self):
        return self.email + ' ' + self.name
