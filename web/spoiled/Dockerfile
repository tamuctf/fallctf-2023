FROM debian@sha256:b86bfc1dd2fb1820fea6c1e0b6e23d155198b518b3a506f6edad71bf6e9a8cef

COPY flag.txt /flag.txt

ENV PHP_INI_DIR=/usr/local/etc/php
ENV PHPIZE_DEPS="autoconf dpkg-dev file g++ gcc libc-dev make pkg-config re2c bison"
ARG PHP_URL=https://github.com/php/php-src/archive/c730aa26bd52829a49f2ad284b181b7e82a68d7d.tar.gz
ARG name
ARG port

RUN PHP_URL=https://github.com/php/php-src/archive/c730aa26bd52829a49f2ad284b181b7e82a68d7d.tar.gz /bin/sh -c set -eux && \
    mkdir -p $PHP_INI_DIR/conf.d && \
    savedAptMark="$(apt-mark showmanual)" && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends ${PHPIZE_DEPS} ca-certificates curl wget libargon2-dev libcurl4-openssl-dev libedit-dev libonig-dev libsodium-dev libsqlite3-dev libssl-dev libxml2-dev zlib1g-dev && \
    mkdir -p /usr/src && \
    cd /usr/src && \
    curl -#SL ${PHP_URL} | tar xz --strip-components=1 && \
    gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" && \
    debMultiarch="$(dpkg-architecture --query DEB_BUILD_MULTIARCH)" && \
    if [ ! -d /usr/include/curl ]; then \
      ln -sT "/usr/include/$debMultiarch/curl" /usr/local/include/curl; \
    fi && \
    ./buildconf && \
    ./configure --build="$gnuArch" --with-config-file-path="$PHP_INI_DIR" --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" --enable-option-checking=fatal --with-mhash --with-pic --enable-ftp --enable-mbstring --enable-mysqlnd --with-password-argon2 --with-sodium=shared --with-pdo-sqlite=/usr --with-sqlite3=/usr --with-curl --with-libedit --with-openssl --with-zlib $(test "$gnuArch" = 's390x-linux-gnu' && echo '--without-pcre-jit') --with-libdir="lib/$debMultiarch" && \
    make -j "$(nproc)" && \
    make install && \
    find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true && \
    make clean && \
    cd / && \
    apt-mark auto '.*' > /dev/null && \
    [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark && \
    find /usr/local -type f -executable -exec ldd '{}' ';' | awk '/=>/ { print $(NF-1) }' | sort -u | xargs -r dpkg-query --search | cut -d: -f1 | sort -u | xargs -r apt-mark manual 		&& \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    php --version && \
    rm -rf /usr/src/* && \
    mkdir -p /var/www/html && \
    cd / && chown www-data:www-data -R /var/www && chmod +r /flag.txt

USER www-data
WORKDIR /var/www/html

COPY src/ .
RUN echo -n "php -S 0.0.0.0:$port" > /var/www/docker_entrypoint.sh
ENTRYPOINT ["sh", "/var/www/docker_entrypoint.sh"]
