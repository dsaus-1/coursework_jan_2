from django.db import models



class Frequency(models.Model):
    frequency = models.CharField(max_length=60, verbose_name='периодичность')

    def __str__(self):
        return f'{self.frequency}'

class Status_settings(models.Model):
    status = models.CharField(max_length=60, verbose_name='статус')

    def __str__(self):
        return f'{self.status}'

class Sending_status(models.Model):
    status = models.CharField(max_length=60, verbose_name='статус')

    def __str__(self):
        return f'{self.status}'


class Client(models.Model):

    email = models.EmailField(max_length=60, verbose_name='Email')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'{self.email} {self.fio}'


class Settings(models.Model):

    mailing_time = models.TimeField(verbose_name='Время рассылки')
    frequency = models.ForeignKey(Frequency, on_delete=models.PROTECT)
    status = models.ForeignKey(Status_settings, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

    def __str__(self):
        return f'{self.mailing_time}, {self.frequency}'


class Message(models.Model):

    title = models.CharField(max_length=80, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Тело письма')
    settings = models.ForeignKey(Settings, on_delete=models.PROTECT, verbose_name='Настройки')

    addressee = models.ManyToManyField(Client, verbose_name='Адреса')


    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'

    def __str__(self):
        return f'{self.title} {self.text}'

class Send_message(models.Model):

    sending_time = models.DateTimeField(verbose_name='Время рассылки')
    status = models.ForeignKey(Sending_status, on_delete=models.PROTECT)
    server_response = models.CharField(blank=True, max_length=100, verbose_name='Ответ сервера')

    message = models.ForeignKey(Message, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытка рассылки'

    def __str__(self):
        return f'{self.sending_time} {self.status} {self.server_response}'






