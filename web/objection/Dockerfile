FROM php:7.2-apache

ARG port

COPY src/ /var/www/html/
COPY flag.txt /var/www/flag.txt
RUN sed -i "s/Listen 80/Listen $port/" /etc/apache2/ports.conf
