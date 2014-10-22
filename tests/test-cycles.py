#!/usr/bin/env python

from grandalf import *

g = utils.Dot().read('samples/cycles.dot')[0]
V = {}
for k,v in g.nodes.items():
    V[k]=graphs.Vertex(k)
    V[k].view = layouts.VertexViewer(10,10)
E = []
for e in g.edges:
    E.append(graphs.Edge(V[e.n1.name],V[e.n2.name]))

G = graphs.Graph(list(V.values()),E)

sg = layouts.SugiyamaLayout(G.C[0])
gr = sg.g

r = [x for x in gr.sV if len(x.e_in())==0]
L = gr.get_scs_with_feedback(r)

print('roots',[x.data for x in r])
for s in L:
  print([x.data for x in s])
