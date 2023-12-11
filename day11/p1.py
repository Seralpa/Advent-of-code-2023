import os
import itertools as itt

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

blank_rows = list()
blank_cols = list()
for i, l in enumerate(data):
	if not "#" in l:
		blank_rows.append(i)
for j, r in enumerate(zip(*data)):
	if not "#" in r:
		blank_cols.append(j)

for i in reversed(blank_rows):
	data.insert(i, ["."] * len(data[i]))
for j in reversed(blank_cols):
	for l in data:
		l.insert(j, ".")

galaxies = list()
for i, l in enumerate(data):
	for j, c in enumerate(l):
		if c == "#":
			galaxies.append((i, j))

print(sum(abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in itt.combinations(galaxies, 2)))
