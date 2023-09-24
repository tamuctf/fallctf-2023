import numpy as np
import random

FLAG = open('flag.txt','r').read().strip()
length = len(FLAG)
A = np.empty(shape = (length,length),dtype="object")
for i in range(length):
    for j in range(length):
        A[i][j] = random.getrandbits(256)
x = np.array([ord(c) for c in FLAG],dtype="object")
b = A @ x
b = list(b)
A_redacted = np.ndarray.tolist(A)
for i in range(3):
    row = random.randrange(length)
    col = random.randrange(length)
    A_redacted[row][col] = "[REDACTED]"
output = open("redacted_results.txt","w")
output.write(f"A = {A_redacted}\n")
output.write(f"{b = }")
output.close()