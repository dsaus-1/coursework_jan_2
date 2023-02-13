from django.db import models

from users.models import User

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):

    STATUSES = (
        ('active', 'активно'),
        ('moderation', 'модерация')
    )
    STATUS_ACTIVE = 'active'
    STATUS_MODERATION = 'moderation'

    header = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.CharField(max_length=900, verbose_name='Содержимое')
    image_preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Изображение')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_status = models.CharField(max_length=15, default=STATUS_MODERATION, choices=STATUSES, verbose_name='Статус публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)


    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

    def __str__(self):
        return f'{self.header}'