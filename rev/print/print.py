import random

def xor(x, y):
    return bytes([a ^ b for a, b in zip(x, y)])

random.seed(69)
ct = bytes.fromhex("74583247dddca49fb28ed0be21a09750bbe52e162eeb0017")
key = bytes([random.randrange(256) for _ in range(len(ct))])
flag = xor(ct, key).decode()
guess = input("Enter your guess for the flag:\n> ")

if guess == flag:
    print("That's the flag!")
