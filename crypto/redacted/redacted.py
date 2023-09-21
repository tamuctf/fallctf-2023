import numpy as np
import random

FLAG = open('flag.txt','r').read().strip()
length = len(FLAG)
A = np.empty(shape = (length,length),dtype=np.int64)
for i in range(length):
    for j in range(length):
        A[i][j] = random.getrandbits(48)-2**47
x = np.array([ord(c) for c in FLAG],dtype=np.int64)
b = A @ x
b = list(b)
A_redacted = np.ndarray.tolist(A)
for i in range(50):
    row = random.randint(0,length-1)
    col = random.randint(0,length-1)
    A_redacted[row][col] = "[REDACTED]"
output = open("redacted_results.txt","w")
output.write(f"A = {A_redacted}\n")
output.write(f"{b = }")
output.close()