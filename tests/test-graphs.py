#!/usr/bin/env python

from  grandalf.graphs import *

def  test_vertex():
    v1 = Vertex()
    assert v1.deg()==0
    assert len(v1.N())==0
    v2 = Vertex("v2")
    assert v2.data=="v2"
    assert v1.e_to(v2) is None
    assert v1.c is None and v2.c is None

def  test_edge():
    v1 = Vertex("a")
    v2 = Vertex("b")
    e1 = Edge(v1,v2,data="a->b")
    v1.e=[e1]
    v2.e=[e1]
    assert v1.deg()==v2.deg()==1
    assert v2 in v1.N()
    assert v1 in v2.N()
    assert len(v1.N(-1))==0
    assert len(v2.N(+1))==0
    assert v2.e_from(v1)==e1

def  test_graph():
    v = ('a','b','c','d')
    V = [Vertex(x) for x in v]
    D = dict(list(zip(v,V)))
    e = ['ab','ac','bc','cd']
    E = [Edge(D[xy[0]],D[xy[1]],data=xy) for xy in e]
    g1 = graph_core()
    assert g1.order()==0
    assert g1.norm()==0
    assert E[0].v[0]==V[0]
    assert V[0].data=="a"
    g1.add_single_vertex(E[0].v[0])
    assert g1.order()==1
    assert g1.norm()==0
    g1.add_edge(E[0])
    assert g1.order()==2
    assert g1.norm()==1
    assert V[0].c==V[1].c==g1
    g1.add_edge(E[2])
    assert g1.order()==3
    assert g1.norm()==2
    assert len(V[1].N())==2
    g1.add_edge(E[3])
    assert g1.order()==4
    assert g1.norm()==3
    g1.add_edge(E[1])
    assert g1.order()==4
    assert g1.norm()==4
    p = g1.path(V[0],V[3])
    assert '->'.join([x.data for x in p])=='a->c->d'
    for v in g1.sV: v.detach()
    #---------
    g2 = Graph(V,E)
    assert V[2] in g2
    p = g2.path(V[0],V[3])
    assert '->'.join([x.data for x in p])=='a->c->d'
    g2.add_edge(Edge(D['d'],D['a'],data='da'))
    rete = V[0].e_from(D['d'])
    assert p == g2.path(V[0],V[3],1)

def  test_remove():
    v1 = Vertex('a')
    v2 = Vertex('b')
    v3 = Vertex('c')
    e1 = Edge(v1,v2)
    e2 = Edge(v1,v3,w=2)
    g  = graph_core([v1,v2,v3],[e1,e2])
    try:
        cont = False
        g.remove_vertex(v1)
    except ValueError as i:
        cont = True
        assert i.args[0]==v1
    assert cont
    assert v1 in g.sV
    assert e1 in g.sE
    assert e2 in g.sE
    g.remove_vertex(v3)
    assert e2 not in g.sE
    v4,v5 = Vertex(4),Vertex(5)
    g = Graph([v1,v2,v3,v4],[e1,e2])
    g.add_edge(Edge(v4,v5))
    g.add_edge(Edge(v3,v5))
    assert len(g.C)==1
    g.remove_vertex(v1)
    assert len(g.C)==2
    assert ''.join([v.data for v in g.C[0].sV])=='b'
    assert [v.data for v in g.C[1].sV]==['c',4,5]


def  test_cycles():
    v = ('a','b','c','d','e','f','g','h')
    V = [Vertex(x) for x in v]
    D = dict(list(zip(v,V)))
    e = ['ab','bc','cd','be','ef','ea','fg','cg','gf','dh','hg','hd','dc','bf']
    E = [Edge(D[xy[0]],D[xy[1]],data=xy) for xy in e]
    g1 = graph_core(V,E)
    scs = g1.get_scs_with_feedback([V[0]])
    assert len(scs)==3
    assert [v.data for v in scs[0]] == ['g', 'f']
    assert [v.data for v in scs[1]] == ['c', 'd', 'h']
    assert [v.data for v in scs[2]] == ['a', 'b', 'e']
    return g1

test_vertex()
test_edge()
test_graph()
test_remove()
test_cycles()
