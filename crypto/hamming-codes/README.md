# Hamming Codes

In 1950, Richard W. Hamming invented [Hamming codes](https://en.wikipedia.org/wiki/Hamming_code) as a way of automatically correcting errors introduced by punched card readers. Hamming codes can detect one bit and two bit errors, or correct one-bit errors without detection of uncorrection errors. Now it's your turn to decode these codes.

Author: Joseph

## Hint

Be mindful of implementation quirks when using online solvers.

## Solution

Since each code takes in 4 bits of data and results in 8 bits of encoded information, this is an extended (8-4) Hamming code. While attempting to paste the output into [dcode.fr](https://www.dcode.fr/hamming-error-correction), I noticed that the decoding was incorrect, so I tried encoding the letter `g` with the provided Python code (with the randomized corruption removed):

```py
# top half of g
print(gen_hamming(0b0110))
# botttom half of g
print(gen_hamming(0b0111))
```
```
11001100
00011110
```

However, on dcode.fr, the bits are rotated right once:
```
01100110
00001111
```

Reading the description closer, I found this:

> The last bit added records the parity of the entire message, it is usually stored in position 1.

The provided implementation follows the Wikipedia page, and the message parity bit is stored in the last position rather than the first position. After rotating the provided output bits to have the parity bit first, dcode.fr successfully decodes and corrects the bits. I copy-pasted the output into CyberChef to turn the binary back into ASCII to get the flag.

flag:
`gigem{h4mming_c0d3s_4r3_r34lly_1nt3r3st1ng}`
