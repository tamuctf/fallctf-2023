FROM python:3.8-slim-buster

ARG port
ARG flag

COPY src/ /app

RUN apt update -y && \
    apt install -y sqlite3 build-essential libsqlite3-dev && \
    pip install flask pysqlite3 lxml && \
    echo ${flag} > /app/flag.txt && \
    sqlite3 /app/users.db < /app/setup.sql && \
    chown -R www-data:www-data /app

USER www-data
WORKDIR /app

ENV PORT=${port}

ENTRYPOINT ["python3", "app.py"]
