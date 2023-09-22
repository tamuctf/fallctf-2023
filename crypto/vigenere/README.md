# Vigenere

We found this ciphertext while buying baguettes in France, but we only know that the key length is 4 (whatever that means):

```
rugsx{keh_lzohsqr_ccugwyml_qsmlzpzgs}
```

Can you figure out what it means?

## Solution

I used the Vigenere plugin in cyberchef to get the flag. It is known that the first part of the flag is `gigem`, so plugging that into the key section reveals that the key is `lmao`.

flag:
`gigem{yet_another_original_challenge}`
