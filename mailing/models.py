from django.db import models


class Client(models.Model):

    email = models.EmailField(unique=True, max_length=60, verbose_name='Email')
    full_name = models.CharField(max_length=150, verbose_name='Full_name')
    comment = models.TextField(null=True, blank=True, verbose_name='Comments')

    phone = models.CharField(max_length=35, verbose_name='Phone number', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='image', null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} {self.email}"

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ('full_name',)


class Message(models.Model):

    subject = models.CharField(default='No subject', max_length=100, verbose_name='Title')
    body = models.TextField(null=True, blank=True, verbose_name='Message')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


# Create your models here.
class MailingSettings(models.Model):

    choice_period = [
        (1, 'once in a day'),
        (7, 'once in a week'),
        (31, 'once in a month'),
    ]

    STATUSES = (
        ('created', 'created'),
        ('started', 'started'),
        ('finished', 'finished')
    )

    start_time = models.DateTimeField(verbose_name='Start time')
    end_time = models.DateTimeField(null=True, blank=True, verbose_name='End time')
    interval = models.PositiveSmallIntegerField(choices=choice_period, verbose_name='interval')
    status = models.CharField(choices=STATUSES, default='created', verbose_name='status')

    clients = models.ManyToManyField(Client, verbose_name='Clients')  # ManyToManyField?
    message = models.ForeignKey(Message, null=True, blank=True, on_delete=models.CASCADE, verbose_name='message')
    # log =

    def __str__(self):
        return f'{self.message}: {self.status} ({self.interval})'

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class MailingLog(models.Model):

    STATUSES = (
        ('successful', 'Success'),
        ('error', 'Error')
    )

    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Last_try')
    status = models.CharField(max_length=10, choices=STATUSES, verbose_name='Status_of_sending')
    server_response = models.CharField(null=True, blank=True, verbose_name='Server_response')

    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Newsletter')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')

    def __str__(self):
        return f'{self.last_try}: {self.server_response}, {self.status}'

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
