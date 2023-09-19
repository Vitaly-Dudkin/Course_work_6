from django.db import models


# Create your models here.
class MailingSettings(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Success'),
        (STATUS_FAILED, 'Error'),
    )

    time_of_sending = models.DateTimeField(auto_now_add=True, verbose_name='time_of_sending')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
    log_of_sending = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='Status')
    periodicity = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='periodicity')
    status = models.CharField(verbose_name='status')
    message = models.ForeignKey('MessageMailing', max_length=300, on_delete=models.CASCADE, verbose_name='message')


# class MailingLog:
#     STATUS_OK = 'ok'
#     STATUS_FAILED = 'failed'
#     STATUSES = (
#         (STATUS_OK, 'Success'),
#         (STATUS_FAILED, 'Error'),
#     )
#
#     last_try = models.DateTimeField(auto_now_add=True, verbose_name='Date of last try')
#     # client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Client')
#     settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Settings')
#     status = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='Status')
#
#     class Meta:
#         verbose_name = 'Log'
#         verbose_name_plural = 'Logs'
