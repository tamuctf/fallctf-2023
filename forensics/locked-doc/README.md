# Locked Doc

I have received a top secret doc containing information about a flag. Could you crack the lock?

## Solution

Since the docx file was password protected I used office to john to get the hash.

office2john UnlockMe.docx > hash.txt

I then used john to crack the hash with rockyou.

sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

This showed that the password was "goldfish". I then used that password to open the document. There was an image in the docx file but I saw there was one word so I deleted the image and I saw the flag.

flag:
`gigem{l0ck_p1ck_m4st3r}`
