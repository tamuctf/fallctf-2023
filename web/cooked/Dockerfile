FROM ubuntu:20.04

ARG port

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip3 install flask

COPY src/ /app

RUN chmod 555 /app

USER 1000:1000

ENV PORT=$port

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
