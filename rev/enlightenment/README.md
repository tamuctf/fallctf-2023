# Enlightenment

You should achieve zen before you reach for enlightenment.
When you do, remember: sometimes, we must change our surroundings before we can achieve true inner peace.

## Hints

<details>
<summary>
Hint 1
</summary>

If you've not already completed `zen`, then this will not be doable. Seriously :)

</details>

<details>
<summary>
Hint 2
</summary>

How do we know who to trust?
I've heard /etc/ssl/certs is a good place to start.

</details>

## Solution

This challenge is very similar to `zen`. I tried the same solve which worked for `zen`, however, there was no HTTP request, only TLS traffic. I assumed that this meant that the binary was making requests via HTTPS rather than HTTP. To try to read the contents of the request, I would need the keys used to encrypt the traffic. Unfortunately, discord's CDN does not leak their private key.

To be able to intercept HTTPS traffic, we need to make the binary reach out to my ssl server, and not discord's server. The first step of this, is setting the domain `cdn.discordapp.com` to `127.0.0.1` in `/etc/hosts`.

After setting the target server, the certs can be created to successfully complete an HTTPS request. I used openssl to create the certs and placed them in `/etc/ssl/` to make sure they were trusted at the system level. 

`ssl.conf`
```nginx
server {
    listen 80;
    listen [::]:80;
    return 301 https://$host$request_uri;
}

server {
    listen 443 http2 ssl;
    listen [::]:443 http2 ssl;

    ssl_certificate /etc/ssl/certs/nginx.crt;
    ssl_certificate_key /etc/ssl/private/nginx.pem;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;

    ssl_protocols TLSv1.3;# Requires nginx >= 1.13.0 else use TLSv1.2
    ssl_prefer_server_ciphers on;
    ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
    ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
    ssl_session_timeout  10m;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off; # Requires nginx >= 1.5.9
    ssl_stapling on; # Requires nginx >= 1.3.7
    ssl_stapling_verify on; # Requires nginx => 1.3.7
    resolver 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;
    # Disable preloading HSTS for now.  You can use the commented out header line that includes
    # the "preload" directive if you understand the implications.
    #add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";

    root /usr/share/nginx/html;

    location / {
    }

    error_page 404 /404.html;
	location = /404.html {
    }

    error_page 500 502 503 504 /50x.html;
    	location = /50x.html {
    }
}
```

Certificate generation
```bash
openssl req -x509 -config config.cfg -newkey rsa:2048 -keyout nginx.pem -out nginx.crt -nodes
```

Once, Nginx is running correctly, the binary can be executed, and the HTTPS request will show up in the Nginx access log.

`127.0.0.1 - - [21/Sep/2023:10:50:57 -0500] "GET /attachments/1145319627933626503/1151963309818531953/c2c98fd47cd48ae3b6687a7ded56ac347b3f965dcf87874b2bfbec55b6026bc437c2d5673b5e4fbe1a6a55270ac0b3972f19fe62b66c225831ba0a5bb470a716 HTTP/1.1" 404 153 "-" "-"`

Navigating to this file on Discord's CDN provides the flag as shown below.

flag:
`gigem{7ru5t_n0_0n3_n07_3veN_yourself}`
