# ZipCrack

You can't get in my zip file. Right...

Author: Noam

## Solution

The zip folder is password protected preventing opening. Cracking the password is easy using `zip2john` to create the hash.

`zip2john folder.zip > hash.txt`

John can then be used to crack the file password.

`john --wordlist=rockyou.txt hash.txt`

Password: `rb=Pk;'LNl,[^iIN`

The included file is base64 encoded. When decoded, it reveals base32 encoded data. The flag is then recovered after decoding the base32 data.

`cat file | base64 -d | base32 -d`

flag:
`gigem{z1p2jh0n1sAg00dt0ol}`
