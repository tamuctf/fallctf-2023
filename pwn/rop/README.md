# Rop

Instead of returning to a single win function, can you chain multiple functions together?

Author: Nathan

## Solution

We can see in the source code of the binary that function `gets` is called on a variable `buf` of size 8. Because `gets` does not have a limit on the number of characters which can be entered, we can enter 8 characters (to fill variable `buf`) and then another 8 characters (to fill the base pointer), and then the next characters will overwrite the stack pointer. 

The code has function which loads the flag variable `load_flag` and function which prints the flag variable `print_flag`. However, we need to use a `ret` gadget before going to `load_flag` in order to align the stack properly (otherwise the binary will just crash). 

As such, we can send a payload with 16 random characters, then the address to a `ret` gadtet, then the address of `load_flag` and then address of `print_flag`. 

flag:
`gigem{ret_is_just_pop_rip}`
