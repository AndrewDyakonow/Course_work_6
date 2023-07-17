from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now

from apscheduler.schedulers.background import BackgroundScheduler

from servises.models import Settings


CHOICES = {
    'Раз в минуту': {'minute': "*/1"},
    'Раз в день':   {'day': "*/1"},
    'Раз в неделю': {'week': '*/1'},
    'Раз в месяц':  {'month': '*/1'},
}


class AutoMail:

    def __init__(self, data):
        self.scheduler = BackgroundScheduler()
        self.data: Settings = data
        self.__create_automail()
        self.scheduler.start()

    def __create_automail(self):
        """Создание задания"""
        self.assd = self.scheduler.add_job(
            self.__preparation_sending,
            trigger='cron',
            **(CHOICES.get(self.data.periodicity)),
            start_date=self.data.date_mailing,
        )

    def __preparation_sending(self):
        """"""
        setting = Settings.objects.get(mailing_name=self.data.mailing_name)
        setting.status = 'Активна'
        setting.save()

        if now() < self.data.date_end_mailing:
            self.mail_to()
        else:
            setting.status = 'Завершена'
            setting.save()
            self.assd.remove()

    def mail_to(self):
        """Отправка сообщений по адресам"""
        for client in self.data.client_name.all():
            send_mail(
                self.data.message.theme,
                self.data.message.body,
                settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
            )
