# Problema 2 – Căutare liniară (15p)

from typing import List, Any

def linear_search(a: List[Any], x: Any) -> bool:
    found=False
    for el in a:
        if el==x:
            found=True
        
    return found

if __name__ == "__main__":
    arr = [4, 7, 1, 9]
    print(linear_search(arr, 7))  # True
