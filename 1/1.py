# %% Cell 1
import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
# %% Cell 2
def f(x):
    return 5*x**2 - 4*x + 5 + 2*x**3
# %% Cell
xs = np.arange(-5,5,0.25)
ys = f(xs)
plt.plot(xs, ys)
# %% Cell
h = 0.0000000000001
x = 3.0
f(x+h)
# 19 min end of part
# %% Cell
class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grade = 0
        self._prev = set(_children)
        self._op = _op
        self.label= label

    def __repr__(self):
        return f"Value(data={self.data})"
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out

a = Value(2.0, label ='a')
b = Value(-3.0, label ='b')
c = Value(727, label = 'c')
d = (a*b+c) ; d.label='d'
k = Value(-2.0, label = 'k')
L = d*k ; L.label='L'
print(d)

# %%
from graphviz import Digraph

def trace(root):
    # builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})  # LR = left to right
    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node for it
        dot.node(name=uid, label="{ %s | data %.4f | grade %.4f }" % (n.label, n.data, n.grade), shape='record')
        if n._op:
            # if this value is a result of some operation, create an op node for it
            dot.node(name=uid + n._op, label=n._op)
            # and connect this node to it
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot
# %% Cell
dot = draw_dot(L)
dot.render('graph', format='svg')
# %%
L.grade=1
