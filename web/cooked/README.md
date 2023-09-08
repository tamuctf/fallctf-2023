# Cooked

Try not to overheat. You might burn yourself out.

## Solution

base64 decoding the cookie will reveal {"username":"guest","uid":69}, looking at the code on the page we can see that if our username is admin and uid is 0 we get the flag. So all we need to do is change guest to admin and uid to 0, base64 encode it and then send a get request to / with that as our cookie and we get the flag.

flag:
`gigem{c00ki3s_ar3_c00l}`
