# https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/kelwnwq/

import networkx as nx
from networkx.classes.function import path_weight

with open("input.txt") as f:
    ls = f.read().strip().split()

N, M = len(ls), len(ls[0])
s, t = (0, 1), (N - 1, M - 2)

prev = {">": (0, -1), "<": (0, 1), "^": (1, 0), "v": (-1, 0)}
G1 = nx.grid_2d_graph(N, M, create_using=nx.DiGraph)
G2 = nx.grid_2d_graph(N, M)
for i, l in enumerate(ls):
    for j, x in enumerate(l):
        p = (i, j)
        if x == "#":
            G1.remove_node(p)
            G2.remove_node(p)
        elif dp := prev.get(x):
            di, dj = dp
            G1.remove_edge(p, (i + di, j + dj))

# Part 1
print(max(map(len, nx.all_simple_edge_paths(G1, s, t))))
