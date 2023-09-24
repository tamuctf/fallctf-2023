# XOR

I heard the one-time pad is unbreakable, so I used it twice to encrypt a picture of the flag for extra security. Can you figure out the original flag?

Author: Nathan

## Solution

We can see from the given `gen_image.py` script exactly how the given images `c1.png` and `c2.png` are generated. 

It appears that the flag is written into two different images, `m1` and `m2`, and the images are XORed with a one-time pad which is randomly generated and placed into variable `key`. Because the one-time-pad is used twice, it is no longer secure. 

Since `m1 XOR key = c1` and `m2 XOR key = c2`, we can perform the operation `c1 XOR c2` which will result in `m1 XOR key XOR m2 XOR key = m1 XOR m2 XOR key XOR key = m1 XOR m2 = original message`, since XORing two of the same value results in the XOR not changing the original value. 

All we need to do is create a Python script which will successfully XOR `c1.png` and `c2.png`, resulting in the original message. 

flag:
`gigem{back_to_the_drawing_board}`
