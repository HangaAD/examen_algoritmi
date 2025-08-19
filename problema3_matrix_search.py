# Problema 3 – Căutare într-o matrice sortată (15p)
from typing import List

def search_sorted_matrix(mat: List[List[int]], x: int) -> bool:
    found=False
    row=len(mat)
    col=len(mat[0])
    i=0
    j=col-1
    while i < row and j>=0:
        if mat[i][j]==x:
            found=True
            break
        elif mat[i][j]>x:
            j=j-1
        else:
            i=i+1
    return found

if __name__ == "__main__":
    mat = [
        [1, 4, 7],
        [2, 5, 9],
        [3, 6, 10]
    ]
    print(search_sorted_matrix(mat, 5))
#Codul incepe de la coltul drepta sus si daca vede ca elementul curent e mai mare inseamca ca ma mut pe o coloana cu elemente mai mic deci la stanga si daca vede ca elementul e mai mic 
#se duce pe urmatoarea linie unde sunt elemnte mai mari decat cel curent 
