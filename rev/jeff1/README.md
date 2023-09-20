# jeff1

I made a flag verifier! Tell me the flag and I will let you know if it's correct or not. 

You may find the debugger program [gdb](https://www.sourceware.org/gdb/) and its very informative extension [gef](https://hugsy.github.io/gef/) useful. 

## Solution

I first opened the file in Ghidra and and found "00101256" was right before it said "yay that is the flag". Then after running gdb with "layout asm" I saw that corresponded to main+273. With gef installed with gdb I set the break point with this command: "b *(main+273)". I then runned the program with "run" and put some input for it to run. gef than showed the flag in the "$rsp" register to be "gigem{dynamic_rev_hehe}". It was also shown in other locations.

flag:
`gigem{dynamic_rev_hehe}`
