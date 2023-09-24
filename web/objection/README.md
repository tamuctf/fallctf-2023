# Objection

I object to your objectification of my PHP objects.

Author: Bode

## Solution

By looking at index.php you can see the code setting user to none and uid to 420 as well as it wanting to be set to admin and the uid being 0.

The current cookie (base64 decoded):
O:7:"Session":2:{s:8:"username";s:4:"none";s:3:"uid";i:420;}

I changed the cookie to:
Tzo3OiJTZXNzaW9uIjoyOntzOjg6InVzZXJuYW1lIjtzOjU6ImFkbWluIjtzOjM6InVpZCI7aTowO30=
O:7:"Session":2:{s:8:"username";s:5:"admin";s:3:"uid";i:0;}

I changed the username to admin as well as 4 to 5 for charters as well as the uid to 0.

When loading Session.php and then going back to index.php the flag, gigem{h0w_cl4ssy}, was shown.

flag:
`gigem{h0w_cl4ssy}`
