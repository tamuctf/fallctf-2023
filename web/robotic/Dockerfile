FROM nginx:latest

ARG port

COPY default.conf /etc/nginx/conf.d/default.conf
RUN printf "User-agent: *\nDisallow: /top-secret-dir/" > /usr/share/nginx/html/robots.txt && \
    mkdir /usr/share/nginx/html/top-secret-dir && \
    printf "gigem{d0nt_us3_r0bots_t0_hid3_fil3s}" > /usr/share/nginx/html/top-secret-dir/index.html && \
    sed -i "s@PORT@${port}@" /etc/nginx/conf.d/default.conf
