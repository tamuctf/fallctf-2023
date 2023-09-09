# ret2shellcode

You've heard of ret2win, now get ready for ret2shellcode.

## Solution

The goal of this challenge is to successfully overwrite the stack pointer to point to shellcode we have written. 

The first step of this challenge is to obtain the address of the variable 'password', which is printed out in the binary in the first printf function: "Welcome to the vault of <address>".
We need to parse out the address from this string and convert it into bytes we can send, so that we can use this address as part of our payload.

The next step is to create the payload. Because variable 'password' can write over 0x110 characters, while the actual variable is of size 0x100, we can overwrite the stack pointer with 16 additional bytes. As such, we can first write the shellcode, and then add a random character in order to fill up the remaining bytes until we begin to overflow the stack pointer. We then overwrite the stack pointer to be the address of variable 'password', which contains our shellcode at the beginning of the variable. As such, the binary will return to the shellcode in the variable and be executed, thus giving us a shell, allowing us to remotely execute commands on the machine. 

We can then run 'cat flag.txt' in order to print out the flag. 

flag:
`gigem{0n_a_dim3}`
