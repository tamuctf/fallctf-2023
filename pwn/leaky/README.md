# Leaky

Can you get the binary to print out the flag?

Author: Nathan

## Solution

Reviewing the source code shows two important lines.

1. `read(STDIN_FILENO, name, sizeof(name));`

2. `printf("hi %s\n", name);`

In the first line, user input is read from stdin to the name array. The sizeof operator determines how many characters to read in, and this is where the bug is.

This bug can be observed in printf. According to the printf manpage, printf will print the array values up to a null byte. This means that printf will continue to print past the oringinal 16 bytes if the last byte of the 16 byte array is not null.

Since the program allows us to write to all 16 bytes of the array, we can overwrite the null byte causing the flag to be leaked.

```
what's your name?
AAAAAAAAAAAAAAAA
hi AAAAAAAAAAAAAAAAgigem{nu11_byt3s_4r3_1mp0rt4nt!!!}
```

flag:
`gigem{nu11_byt3s_4r3_1mp0rt4nt!!!}`
