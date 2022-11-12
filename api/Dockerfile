FROM python:3.10.8

WORKDIR /code

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install -r requirements.txt --no-cache-dir --disable-pip-version-check