# no str

no str. just rev.

Author: Bode

## Solution

The challenge gives us a binary, which when we run, asks us for a password. Most likely, the goal of this challenge is going to be to obtain the password required in the binary.
If we try to run the binary "strings", which returns all human-readable strings in the binary, we do not get any results which look like either a flag, or a password. As such, we need to reverse engineer the binary to understand how its code is working.

Using Ghidra, we can see that the binary adds several bytes into the stack, and then runs "puts" to prompt for the password; the binary then prompts input with "fgets", and then runs "strncmp" to compare the entered result with the hex bytes entered into the stack. As such, if we convert the characters being moved into the stack into ASCII and combine them, we should get the password required for the binary.

There are many ways to convert hexadecimal to ASCII. I decide to convert using CyberChef, an online tool, and use the "From Hex" operation.
If we take each hexadecimal byte from the assembly and convert it into ASCII, we obtain the flag of the challenge.

We can verify the solution by entering the flag as the password for the binary, which will then return the output "Correct!". 

flag:
`gigem{st4tically_r3ved}`
