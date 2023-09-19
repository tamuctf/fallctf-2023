FROM debian:buster-slim

ARG name

RUN apt-get update -y; apt-get install -y build-essential
ADD $name.c /tmp/$name.c
ADD Makefile /tmp/Makefile
RUN cd /tmp;make all
