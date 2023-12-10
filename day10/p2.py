import os
import networkx as nx

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

g = nx.Graph()
start = (-1, -1)
n = "|LJS"
s = "|7FS"
w = "-J7S"
e = "-LFS"

for i, l in enumerate(data):
	for j, c in enumerate(l):
		if i > 0 and (c in n) and (data[i - 1][j] in s):
			g.add_edge((i, j), (i - 1, j))
		if i < len(data) - 1 and (c in s) and (data[i + 1][j] in n):
			g.add_edge((i, j), (i + 1, j))
		if j > 0 and (c in w) and (data[i][j - 1] in e):
			g.add_edge((i, j), (i, j - 1))
		if j < len(l) - 1 and (c in e) and (data[i][j + 1] in w):
			g.add_edge((i, j), (i, j + 1))
		if c == "S":
			start = (i, j)
loop = nx.node_connected_component(g, start)
g.remove_nodes_from(set(g) - loop)

g2 = nx.Graph()
for i in range(-1, len(data) + 1):
	for j in range(-1, len(data[0]) + 1):
		i5, j5 = i + .5, j + .5
		if not g.has_edge((i, j), (i, j + 1)):
			g2.add_edge((i5, j5), (i5 - 1, j5))
		if not g.has_edge((i, j), (i + 1, j)):
			g2.add_edge((i5, j5), (i5, j5 - 1))
		if not g.has_edge((i, j + 1), (i + 1, j + 1)):
			g2.add_edge((i5, j5), (i5, j5 + 1))
		if not g.has_edge((i + 1, j), (i + 1, j + 1)):
			g2.add_edge((i5, j5), (i5 + 1, j5))
		if (i, j) not in loop:
			g2.add_edge((i, j), (i5, j5))

inner_nodes = (set(g2.nodes) - nx.node_connected_component(g2, (-1, -1)))
print(len([(i, j) for i, j in inner_nodes if type(i) == int and type(j) == int]))
