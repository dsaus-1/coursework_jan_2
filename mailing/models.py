from django.db import models

class Client(models.Model):

    email = models.EmailField(max_length=60, verbose_name='Email')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'{self.email} {self.fio}'


class Message(models.Model):

    title = models.CharField(max_length=80, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'

    def __str__(self):
        return f'{self.title}'


class Settings(models.Model):
    FREQUENCY = (
        ('day', 'раз в день'),
        ('week', 'раз в неделю'),
        ('month', 'раз в месяц'),
    )
    FREQUENCY_DAY = 'day'
    FREQUENCY_WEEK = 'week'
    FREQUENCY_MONTH = 'month'

    STATUS = (
        ('completed', 'завершена'),
        ('created', 'создана'),
        ('launched', 'запущена'),
    )
    STATUS_COMPLETED = 'completed'
    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'

    mailing_time = models.TimeField(verbose_name='Время рассылки')
    frequency = models.CharField(max_length=25, default=FREQUENCY_DAY, choices=FREQUENCY, verbose_name='Периодичность')
    status = models.CharField(max_length=25, default=STATUS_CREATED, choices=STATUS, verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')

    addressee = models.ManyToManyField(Client, verbose_name='Адреса')

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return f'{self.mailing_time}, {self.frequency}'


class Send_message(models.Model):
    STATUS = (
        ('delivered', 'доставлено'),
        ('not_delivered', 'не доставлено'),
    )
    STATUS_DELIVERED = 'delivered'
    STATUS_NOT_DELIVERED = 'not_delivered'

    sending_time = models.DateTimeField(verbose_name='Время рассылки')
    status = models.CharField(max_length=25, default=STATUS_DELIVERED, choices=STATUS, verbose_name='Статус')
    server_response = models.CharField(blank=True, max_length=100, verbose_name='Ответ сервера')

    settings_pk = models.ForeignKey(Settings, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытка рассылки'

    def __str__(self):
        return f'{self.sending_time} {self.status} {self.server_response} '






