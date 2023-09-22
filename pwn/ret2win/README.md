# ret2win

Can you hijack control flow and get to the win function?

## Solution

In the source code for the binary, we can see a `win` function which prints the flag, and we can see that function `fgets` is called with an input size of 48, while the variable we are entering characters into, `buf`, is size 16. This means that if we fill 16 characters (to fill variable `buf`) and another 8 characters (for the base pointer), the next characters filled will overwrite the stack pointer, allowing us to change code execution.

As such, all we need to do is send a payload with 24 random characters, and then the address in bytes of function `win`. This will allow us to return to the `win` function, and thus print the flag. 

flag:
`gigem{how_did_we_get_here???}`
