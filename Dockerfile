FROM python:3.8-alpine

WORKDIR /srv/app

RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
    build-base \
    mariadb-dev \
    && pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
COPY Makefile .

RUN pipenv install --system

VOLUME ["/srv/app"]

CMD [ "tail", "-f", "/dev/null" ]
