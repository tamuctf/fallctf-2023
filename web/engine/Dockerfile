FROM nginx:latest

ARG port
ARG flag

COPY default.conf /etc/nginx/conf.d/default.conf
COPY src/ web/

RUN apt update -y && apt install -y php && mkdir /tmp/uploads && \
    sed -i "s@PORT@${port}@" /etc/nginx/conf.d/default.conf && \
    echo ${flag} > /tmp/flag.txt && \
    echo "cd /web && php -S 127.0.0.1:1337 &" > /docker-entrypoint.d/start_php.sh && \
    chmod +x /docker-entrypoint.d/start_php.sh
