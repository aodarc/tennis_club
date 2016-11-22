import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
def gallery_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<gallery>/<filename>
    name = '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])
    return 'gallery/{0}/{1}'.format(instance.name, name)


def img_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<gallery>/<filename>
    name = '{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])
    return 'gallery/{0}/{1}'.format(instance.album.name, name)


class Album(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва альбому', blank=False, unique=True)
    main_img = models.ImageField(verbose_name='Обкладинка альбому', upload_to=gallery_path)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбоми'

    def __str__(self):
        return self.name


class Picture(models.Model):
    img = models.ImageField(verbose_name='Картинка', blank=False, upload_to=img_path)
    alt = models.CharField(max_length=255, blank=True)
    album = models.ForeignKey(to=Album, related_name='pictures', verbose_name='Альбом', null=False, blank=False)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return 'Альбом: {} ||| {}'.format(self.album.name, self.alt or self.pk)


class Video(models.Model):
    url = models.URLField(verbose_name='Посилання на відео',
                          blank=False,
                          help_text='Наприклад https://www.youtube.com/watch?v=lMinfVMfH9k')
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=False)
    description = RichTextUploadingField(verbose_name='Опис', blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Додано')

    @property
    def video_id(self):
        return self.url[self.url.find('v=') + 2:]

    def get_video_frame(self):
        return '<iframe class="embed-responsive-item" width="100%" height="500px" src="https://www.youtube.com/embed/{}" frameborder="0" allowfullscreen="true"></iframe>'.format(
            self.video_id)

    def get_thumbnail_video(self):
        return 'https://img.youtube.com/vi/{}/0.jpg'.format(self.video_id)

    def __str__(self):
        return self.title
