import datetime

from django.conf import settings
from django.core.mail import send_mail

from mailing.models import MailingSettings, MailingLog


def _send_email(mailing_settings, client):
    result = send_mail(
        subject=mailing_settings.message.subject,
        message=mailing_settings.message.body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client.email],
        fail_silently=False
    )

    MailingLog.objects.create(
        status=MailingLog.STATUSES[0][0] if result else MailingLog.STATUSES[1][0],
        mailing=mailing_settings,
        client=client,
        server_response=result
    )


def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_setting in MailingSettings.objects.exclude(status=MailingSettings.STATUSES[2][0]):
        if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):
            for mailing_client in mailing_setting.clients.all():

                mailing_log = MailingLog.objects.filter(client=mailing_client,
                                                        mailing=mailing_setting)
                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_try').first().last_try

                    if mailing_setting.interval == MailingSettings.choice_period[0][0]:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_email(mailing_setting, mailing_client)
                    elif mailing_setting.interval == MailingSettings.choice_period[1][0]:
                        if (datetime_now - last_try_date).days >= 7:
                            _send_email(mailing_setting, mailing_client)
                    elif mailing_setting.interval == MailingSettings.choice_period[2][0]:
                        if (datetime_now - last_try_date).days >= 30:
                            _send_email(mailing_setting, mailing_client)

                else:
                    _send_email(mailing_setting, mailing_client)
