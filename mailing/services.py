# import datetime
#
# from django.conf import settings
# from django.core.mail import send_mail
#
# from mailing.models import MailingSettings, MailingLog
#
#
# def _send_email(message_settings, message_client):
#     result = send_mail(
#         subject=message_settings.message.subject,
#         message=message_settings.message.message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[message_client.client.email],
#         fail_silently=False
#     )
#
#     MailingLog.objects.create(
#         status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
#         settings=message_settings,
#         client_id=message_client.client_id,
#         server_response=result
#     )
#
#
# def send_mails():
#     datetime_now = datetime.datetime.now(datetime.timezone.utc)
#     for mailing_setting in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
#         if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):
#             for mailing_client in mailing_setting.mailingclient_set.all():
#
#                 mailing_log = MailingLog.object.filter(client=mailing_client.client,
#                                                        settings=mailing_setting)
#                 if mailing_log.exists():
#                     last_try_date = mailing_log.order_by('-last_try').first().last_try
#
#                     if mailing_log.period == MailingSettings.PERIOD_DAILY:
#                         if (datetime_now - last_try_date).days >= 1:
#                             _send_email(mailing_setting, mailing_client)
#                     elif mailing_log.period == MailingSettings.PERIOD_WEEKLY:
#                         if (datetime_now - last_try_date).days >= 7:
#                             _send_email(mailing_setting, mailing_client)
#                     elif mailing_log.period == MailingSettings.PERIOD_MONTHLY:
#                         if (datetime_now - last_try_date).days >= 30:
#                             _send_email(mailing_setting, mailing_client)
#
#                 else:
#                     _send_email(mailing_setting, mailing_client)
