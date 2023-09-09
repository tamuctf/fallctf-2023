FROM debian:buster-slim as build

ARG name

RUN apt-get update -y; apt-get install -y build-essential
ADD $name.c /tmp/$name.c
ADD Makefile /tmp/Makefile
RUN cd /tmp;make all

FROM debian:buster-slim

ARG name
ARG port

RUN apt-get update -y; apt-get install -y socat
COPY --from=build /tmp/$name /pwn/$name
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

RUN echo "exec socat -s TCP-LISTEN:$port,reuseaddr,fork EXEC:/pwn/$name,stderr" > /docker_entrypoint.sh

ENTRYPOINT ["sh", "/docker_entrypoint.sh"]
