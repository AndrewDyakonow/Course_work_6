FROM python:3.11.5-slim-bullseye
LABEL authors="blendi"

RUN apt-get update && apt-get install nano

WORKDIR /django_app/

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["sh", "/django_app/entrypoint.sh"]