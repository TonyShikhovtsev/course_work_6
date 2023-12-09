from mailings.models import Mailing, MAILING_PERIOD_CHOICES
from mailings.mailings_service.send_mail_and_log import cronjob_send_mail_and_log
from datetime import datetime, timedelta
import calendar
import pytz


def cron_task():
    print('cron_job worked')
    current_time = datetime.now().replace(tzinfo=pytz.UTC)
    current_time_str: str = datetime.now().strftime('%Y-%m-%d %H:%M')
    mailings = Mailing.objects.filter(status='enabled')

    for mailing in mailings:
        next_attempt_str: str = mailing.next_attempt.strftime('%Y-%m-%d %H:%M')

        if next_attempt_str == current_time_str:
            print('email sent')
            cronjob_send_mail_and_log(
                new_mailing=mailing,
                customers=mailing.customers.all(),
                user=mailing.user,
                current_time=datetime.now()
            )
            interval_mapping = {
                'every_minute': timedelta(minutes=1),
                'daily': timedelta(days=1),
                'weekly': timedelta(weeks=1),
                'monthly': timedelta(days=calendar.monthrange(current_time.year, current_time.month)[1]),
            }
            mailing.next_attempt = current_time + interval_mapping.get(mailing.interval, timedelta())
            mailing.save()
