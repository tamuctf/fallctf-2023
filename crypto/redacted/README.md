# redacted

Someone spilled their coffee all over this matrix encrypted flag. However, not all hope is lost since Python random uses the Mersenne Twister, which is known to be cryptographically insecure. 

Here are some tools you might find helpful:

- https://github.com/icemonster/symbolic_mersenne_cracker
- https://github.com/twisteroidambassador/mt19937-reversible
- https://docs.sympy.org/latest/guides/solving/solve-matrix-equation.html

## Solution

We want to recover the matrix A. The word size of MT is 32 bits, so each matrix entry is worth 256 bits / 32 bits per word = 8 words. Thus, we need to call `submit` on the cracker 8 times for each matrix entry. For redacted entries, we don't know any of the bits, so each of the 8 words will be 32 unknown bits. For unredacted entries, we can see that subsequent words form the more significant bits of `getrandbits`'s return value by reading the [CPython MT implementation](https://github.com/python/cpython/blob/main/Modules/_randommodule.c#L524), so we start submitting from the least-significant word. After recovering the state, we can rewind it with the reversible MT code, then regenerate A. Then, we just need to solve the system Ax = b for x to recover the flag. See `solve.py` for details.

flag:
`gigem{lmao}`
