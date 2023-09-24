from pathlib import Path
from untwist import Untwister
import random
from mersenne_twister import MT19937
from sympy.matrices import Matrix
import numpy as np

exec(Path("redacted_results.txt").read_text())

ut = Untwister()
n = len(b)
k = 8

for row in A:
    for full in row:
        if full == "[REDACTED]":
            for _ in range(k):
                ut.submit("?" * 32)
        else:
            bits = f"{full:0256b}"
            for i in reversed(range(0, 256, 32)):
                s = bits[i:i + 32]
                ut.submit(s)

rng = ut.get_random()
mt = MT19937()
output_for_cloning = [rng.getrandbits(mt.w) for _ in range(mt.n)]
mt.clone_state_from_output_and_rewind(output_for_cloning)
mt.rewind(n * n * k)

def get_256(mt):
    ret = 0
    xs = [mt.get_next_random() for _ in range(k)]
    for x in reversed(xs):
        ret <<= 32
        ret |= x
    return ret

recovered = [[get_256(mt) for _ in range(n)] for _ in range(n)]
A = Matrix(recovered)
b = Matrix(b)
x = A.solve(b)
print("".join(chr(c) for c in x))