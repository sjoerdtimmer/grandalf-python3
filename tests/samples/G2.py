#!/usr/bin/env python
from grandalf.graphs import Vertex,Edge

# define a larger graph found in paper ???
v = list(range(30))
V = [Vertex(x) for x in map(str,v)]
D = dict(list(zip(v,V)))
e = [(0,5), (0,29), (0,6), (0,20), (0,4),
     (17,3), (5,2), (5,10), (5,14), (5,26), (5,4), (5,3),
     (2,23), (2,8), (14,10), (26,18), (3,4),
     (23,9), (23,24), (10,27), (18,13),
     (1,12), (24,28), (24,12), (24,15),
     (12,9), (12,6), (12,19),
     (6,9), (6,29), (6,25), (6,21), (6,13),
     (29,25), (21,22),
     (25,11), (22,9), (22,8),
     (11,9), (11,16), (8,20), (8,16), (15,16), (15,27),
     (16,27),
     (27,19), (27,13),
     (19,9), (13,20),
     (9,28), (9,4), (20,4),
     (28,7)
    ]
E = [Edge(D[x],D[y]) for x,y in e]
G2= (V,E)
