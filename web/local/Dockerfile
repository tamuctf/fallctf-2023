FROM php:7.2-apache

COPY src/ /var/www/html

ARG flag
ARG port

RUN echo ${flag} >> /tmp/flag.txt && \
    mkdir /var/www/html/uploads && \
    sed -i 's@Listen 80@Listen '"${port}"'@g' /etc/apache2/ports.conf && \
    sed -i 's@\*:80@\*:'"${port}"'@g' /etc/apache2/sites-enabled/000-default.conf && \
    docker-php-ext-install exif && \
    chown -R www-data:www-data /var/www/
