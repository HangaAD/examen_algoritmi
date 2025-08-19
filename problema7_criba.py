# Problema 7 – Criba lui Eratostene (10p)

from typing import List

def sieve(n: int) -> List[int]:
    prim = [True] * (n + 1)
    prim[0] = False
    prim[1] = False
    p = 2
    while p * p <= n:
        if prim[p] == True:
            for i in range(p * p, n + 1, p):
                prim[i] = False
        p += 1
    return [i for i, is_prim in enumerate(prim) if is_prim]

if __name__ == "__main__":
    print(sieve(20))
#pentru sieve(30) [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
