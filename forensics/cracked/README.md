# Cracked

I like keeping my passwords safe, so I hashed mine with SHA256 to keep people from knowing what it is.

The flag format is: `gigem{<password>}`

SHA256: `5d829dd477e60d86dffd06f1a70257a2ab03e84b14879bedb7763f0241664ca9`

## Solution

We are given a hash which we are told is of type SHA-256. We can use tool `john` to crack the hash. We can use command `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=Raw-SHA256` to crack the hash and get the correct password.

flag:
`gigem{Lets you update your FunNotes and more!}`
