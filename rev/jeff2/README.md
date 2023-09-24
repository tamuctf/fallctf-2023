# jeff2

I was so close to solving the challenge when I found a text file with the flag, I implemented my decipher algorithm but was sidetracked by a very urgent question: If I had five cookies and zero friends, how many cookies could I give to each friend? However, my program crashed before I could get an answer! Please help me retrieve and decipher the flag.

Note: You do not need to have completed jeff1 to do jeff2! However, make sure you have the tools mentioned in jeff1: [gdb](https://www.sourceware.org/gdb/) and its very informative extension [gef](https://hugsy.github.io/gef/). You should additionally consider using [ghidra](https://ghidra-sre.org/)

Author: Stella

## Dev Notes

Ensure that the zip includes both the program binary and the core dump. 

## Solution

This challenge provides a binary and core dump. To analyze this core dump with gdb, we can run: `gdb ./jeff2 ./core.jeff2.25832`

When gdb starts we can use a backtrace (`bt`) to determine which function caused the crash.

As shown below, the program crashed in the function `g()`.

```
#0  0x00000000004016d8 in g () at jeff2.c:8
#1  0x000000000040174e in a () at jeff2.c:22
#2  0x000000000040175f in l () at jeff2.c:26
#3  0x0000000000401770 in f () at jeff2.c:30
#4  0x0000000000401781 in main () at jeff2.c:34
```

Now opening the binary in ghidra, we can open the `g()` function and see that the program is opening a file called `real_flag.txt` then reading the contents of that file to a buffer and xoring the content with the key `0x6666316a`.

Going back to gdb and running `disas g` we can view the assembly code that the program is actually running. Looking at the `fread` shows the parameters being used in the 4 `mov` instructions above it. This is because the calling convention for x86 asm is `%rdi, %rsi, %rdx, %rcx`. `%rdi` is the first parameter and is set to `%rax` which is defined earlier as `%rbp-0x40`. This means that the buffer containing the encrpyted flag is located at the address of `%rbp-0x40`. We also know the length of the flag in memory because the second parameter of fread is the number of bytes to read, and `%rsi` is set to `0x1d`.

We can now read `0x1d` bytes of memory at `%rbp-0x40` using the command `x/30x $rbp-0x40`

```
0x7ffe97e75080: 0x0d    0x58    0x01    0x03    0x07    0x4a    0x05    0x56
0x7ffe97e75088: 0x18    0x54    0x39    0x02    0x1f    0x5c    0x16    0x55
0x7ffe97e75090: 0x0e    0x6e    0x0b    0x1f    0x35    0x57    0x0a    0x52
0x7ffe97e75098: 0x0d    0x00    0x1e    0x57    0x17    0x00
```

We can now xor this data with `0x6666316a` (little endian) to get the flag.

flag:
`gigem{c0re_dump3d_my_fl4g1x1}`
