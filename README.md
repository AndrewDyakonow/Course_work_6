
<h1 align="center">Mailing_service</h1>

<h2 align="center">Сервис для spam рассылок</h2>

<div align="center">
    
<div>
    <a href="https://pypi.org/project/psycopg2/2.9.6/"><img alt="Static Badge" src="https://img.shields.io/badge/psycopg2--binary-2.9.6-green?labelColor=red&color=blue"></a>
    <a href="https://www.djangoproject.com/"><img alt="Static Badge" src="https://img.shields.io/badge/django-4.2.3-darkgreen?labelColor=gray"></a>
    <a href="https://pypi.org/project/Pillow/10.0.0/"><img alt="Static Badge" src="https://img.shields.io/badge/pillow-10.0.0-darkblue?labelColor=lightgray"></a>
    <a href="https://pypi.org/project/python-dotenv/"><img alt="Static Badge" src="https://img.shields.io/badge/python--dotenv-1.0.0-darkred?labelColor=gray"></a>
    <a href="https://pypi.org/project/APScheduler/3.10.1/"><img alt="Static Badge" src="https://img.shields.io/badge/APScheduler-%203.10.1-darkgreen?labelColor=purple"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.postgresql.org/"><img width="48" height="48" src="https://img.icons8.com/color/48/postgreesql.png" alt="postgreesql"/></a>
    <a href="https://www.docker.com/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker"/></a>
    <a href="https://redis.io/"><img width="48" height="48" src="https://img.icons8.com/color/48/redis.png" alt="redis"/></a>
</div>

</div>

___
## Задачи
1. Реализовать CRUD-механизм для управления рассылками.
2. Реализовать скрипт рассылки, который работает по расписанию.
3. Добавить настройки конфигурации для периодического запуска задачи.

___
## Установка

1. Откройте проект с помощью Get from VCS.
2. Введите ссылку на удалённый репозиторий. 
```bash
    git@github.com:AndrewDyakonow/Mailing_service.git
```
3. Создайте и активируйте виртуальное окружение.
```bash
    python3 -m venv venv
    source venv/bin/activate
```
4. Установите зависимости.
```bash
    pip install -r requirements.txt
```

5. Сервис рекомендуется запускать в контейнерах Docker.
Для этого необходимо иметь установленное программное обеспечение <a href="https://www.docker.com/">Docker</a>.

Для работы потребуется получить доступ к внешнему SMTP-серверу, например к своему поставщику услуг
электронной почты.

После получения пароля для почтовой программы, необходимо вставить его в поле EMAIL_HOST_PASSWORD
файла .env.docker, заменив три звездочки

```
EMAIL_HOST_PASSWORD=***
```

После этого можно выполнить команду построения докер-контейнеров

```bash
docker-compose up
```

Сервис доступен по адресу 

```html
    http://127.0.0.1:8001/
```

___