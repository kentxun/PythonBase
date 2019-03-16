# !/usr/bin/env python
# -*- coding:utf-8 -*-


# __all__ = ['图(用邻接矩阵表示)',
#            'DFS非递归',
#            'Kruskal',
#            'Prim',
#            'Dijkstra',
#            'Floyd']


# 图(用邻接矩阵表示)
class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        # 检查方阵
        for x in mat:
            if len(x) != vnum:
                raise Exception('Empty!')
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    # 顶点数目
    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception(str(vi) + 'or' + str(vj) + 'is not valid!')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception(str(vi) + 'or' + str(vj) + 'is not valid!')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise Exception(str(vi) + 'is not valid!')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges


# DFS非递归
from 数据结构与算法.Stack_and_Queue import SStack
def DFS_graph(graph, v0):
    vnum = graph.vertex_num()
    visited = [0] * vnum
    visited[v0] = 1
    DFS_seq = [v0]
    st = SStack()
    st.push((0, graph.out_edges(v0)))
    while not st.is_empty():
        i, edges = st.pop()
        if i < len(edges):
            v, e = edges[i]
            st.push((i + 1, edges))
            if not visited[v]:
                DFS_seq.append(v)
                visited[v] = 1
                st.push((0, graph.out_edges(v)))
    return DFS_seq


# Kruskal
def Kruskal(graph):
    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()
    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == vnum - 1:
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


# Prim
from 数据结构与算法.BinTree import PrioQueue
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    cands = PrioQueue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst


# Dijkstra(v0到所有点的最短路径)
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 <= vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths


# Floyd
def all_shortest_paths(graph):
    vnum = graph.vertex_num()
    paths = [[graph.get_edge(i, j) for j in range(vnum)]
             for i in range(vnum)]
    nvertex = [[-1 if paths[i][j] == float('inf') else j for j in range(vnum)]
               for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if paths[i][j] > paths[i][k] + paths[k][j]:
                    paths[i][j] = paths[i][k] + paths[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return paths, nvertex
