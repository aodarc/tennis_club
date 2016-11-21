from datetime import date, timedelta
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

SEX = (
    ('m', 'Чоловіча'),
    ('f', 'Жіноча'),
    ('o', 'Інша')
)


class Member(models.Model):
    avatar = models.ImageField(blank=False, verbose_name='Аватарка', upload_to='members/avatars/')
    first_name = models.CharField(max_length=20, blank=False, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, blank=False, verbose_name='Прізвище')
    sex = models.CharField(max_length=1, default='0', choices=SEX, blank=False, verbose_name='Стать')
    birthday = models.DateField(blank=False, verbose_name='Дата народження')
    height = models.SmallIntegerField(verbose_name='Зріст',
                                      help_text='Зріст вказувати в СМ',
                                      validators=[
                                          MaxValueValidator(230),
                                          MinValueValidator(50)
                                      ])
    weight = models.SmallIntegerField(verbose_name='Вага',
                                      help_text='Вагу вказувати в КГ',
                                      validators=[
                                          MaxValueValidator(150),
                                          MinValueValidator(30)
                                      ])
    is_coach = models.BooleanField(default=False, verbose_name="Тренер")
    is_boss = models.BooleanField(default=False, verbose_name='Керівник клубу')
    rating = models.SmallIntegerField(verbose_name='Рейтинг', default=0)
    games = models.IntegerField(default=0, verbose_name='Зіграні ігри', validators=[MinValueValidator(0)])

    @property
    def is_child(self):
        return not (date.today() - self.birthday).days/365 < 18

    @property
    def get_rank_position(self):
        # TODO: find better way
        return list(Member.objects.order_by('-rating')).index(self) + 1

    def get_full_name(self):
        return ' '.join((self.first_name, self.last_name))

    def __str__(self):
        return self.get_full_name()
