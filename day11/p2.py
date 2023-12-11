import os
import itertools as itt

EXPANSION_RATE = 1000000


def get_distance(g1: tuple[int, int], g2: tuple[int, int], blank_rows: list[int], blank_cols: list[int]) -> int:
	delta_i = abs(g1[0] - g2[0]) + (EXPANSION_RATE - 1) * len([i for i in blank_rows if i in range(min(g1[0], g2[0]), max(g1[0], g2[0]))])
	delta_j = abs(g1[1] - g2[1]) + (EXPANSION_RATE - 1) * len([j for j in blank_cols if j in range(min(g1[1], g2[1]), max(g1[1], g2[1]))])
	return delta_i + delta_j


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

galaxies = list()
for i, l in enumerate(data):
	for j, c in enumerate(l):
		if c == "#":
			galaxies.append((i, j))

print(sum(get_distance(g1, g2, blank_rows, blank_cols) for g1, g2 in itt.combinations(galaxies, 2)))
