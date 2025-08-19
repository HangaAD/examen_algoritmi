# Problema 5 – A* (10p)
# a) Explicați algoritmul A* în comentarii
# b) Implementați A* pe un grid 3x3 cu obstacol în centru

from heapq import heappush, heappop

Grid = list[list[int]]

def heuristic(a, b):
    (x1, y1), (x2, y2) = a, b
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid: Grid, start: tuple[int,int], goal: tuple[int,int]):
    # TODO
    return []

if __name__ == "__main__":
    grid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    print(astar(grid, (0,0), (2,2)))
#A* este ceva intre greedy si Dijktra in sensul in care din nodul curent o sa caute toate nodurile posibile catre final dar se lasa ghidat de o euristica aproximativa 
# e un fel de cel mai bun drum pana aici, tinand cont ca urmatoarele probabil vor fi ok adica f= cost total daca mergi prin n, g cat a costat sa ajungi acolo si h cat crezi ca te va mai costa
# iar euristica aici e distanta dintre punctul meu si punctul final 
