#!/usr/bin/env python

from  grandalf.graphs  import *
from  grandalf.layouts import *

import pdb

v = list(range(1001))
V = [Vertex(x) for x in v]
E = [Edge(V[x],V[x+1]) for x in range(1000)]

gr  = graph_core(V,E)
for  v in gr.V(): v.view = VertexViewer(10,10)
sug  = SugiyamaLayout(gr)
sug.init_all()
sug.draw(1)
