from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now

from apscheduler.schedulers.background import BackgroundScheduler

from servises.models import Settings, Logs

CHOICES = {
    'Раз в минуту': {'minute': "*/1"},
    'Раз в день':   {'day': "*/1"},
    'Раз в неделю': {'week': '*/1'},
    'Раз в месяц':  {'month': '*/1'},
}


def help_mixin(data: Settings, command, status) -> None:
    Logs.objects.create(
        title=f'{command}: {data.mailing_name}',
        date_last=now(),
        status=f'{status}',
        answer='good',
        settings=data,
    )


class AutoMail:

    scheduler = BackgroundScheduler()
    __objects = []

    def __init__(self, data):
        self.data: Settings = data
        self.setting = Settings.objects.get(mailing_name=self.data.mailing_name)

    def create_automail(self):
        """Создание задания"""
        if len(AutoMail.scheduler.get_jobs()) > 0:
            AutoMail.scheduler.pause()

        AutoMail.scheduler.add_job(
            self.__preparation_sending,
            trigger='cron',
            **(CHOICES.get(self.data.periodicity)),
            start_date=self.data.date_mailing,
            id=self.data.mailing_name,
            max_instances=10,
        )
        if len(AutoMail.scheduler.get_jobs()) == 1:
            AutoMail.scheduler.start()
        else:
            AutoMail.scheduler.resume()

        self.setting.status = 'Активирована'
        self.setting.save()
        help_mixin(self.data, 'Создана задача', 'Рассылка активирована')

    def __preparation_sending(self):
        """"""
        self.setting.status = 'Активна'
        self.setting.save()

        if now() < self.data.date_end_mailing:
            self.mail_to()
        else:
            self.break_mailing(self.data.mailing_name)

    def mail_to(self):
        """Отправка сообщений по адресам"""

        for client in self.data.client_name.all():
            send_mail(
                self.data.message.theme,
                self.data.message.body,
                settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
            )

            help_mixin(self.data,  f'Письмо отправлено {client.email}', 'Отправлено')

    def break_mailing(self, id_job):
        self.setting.status = 'Завершена'
        self.setting.save()

        AutoMail.scheduler.remove_job(job_id=id_job)
        help_mixin(self.data, 'Рассылка завершена', 'Good')

        if len(AutoMail.scheduler.get_jobs()) == 0:
            AutoMail.scheduler.shutdown()

    @classmethod
    def get_mailing_count(cls):
        return len(cls.scheduler.get_jobs())
