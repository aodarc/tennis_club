import uuid

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
