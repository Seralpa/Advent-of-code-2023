from itertools import cycle
import os

coord_t = tuple[int, int]


def gen_coords_in_dir(s: coord_t, d: coord_t, data: list[list[str]], rolling: set[coord_t]) -> coord_t:
	curr = s
	while True:
		new = (curr[0] + d[0], curr[1] + d[1])
		if not (0 <= new[0] < len(data) and 0 <= new[1] < len(data[0])) or data[new[0]][new[1]] == "#" or new in rolling:
			return curr
		curr = new


def print_state(data, rolling):
	for i, l in enumerate(data):
		for j, c in enumerate(l):
			if (i, j) in rolling:
				print("O", end = "")
			else:
				print("#" if c == "#" else ".", end = "")
		print()
	print()


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

# nwse
directions = cycle([(-1, 0), (0, -1), (1, 0), (0, 1)])
rolling = {(i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == "O"}
states = []

n = 0
while rolling not in states:
	states.append(rolling)
	n += 1
	for _ in range(4):
		d = next(directions)
		roll_l = sorted(list(rolling), key = lambda x: x[1 if d[0] == 0 else 0], reverse = sum(d) > 0)
		new_rolling = set()
		for ri, rj in roll_l:
			i2, j2 = gen_coords_in_dir((ri, rj), d, data, new_rolling)
			new_rolling.add((i2, j2))
		rolling = new_rolling

target = 1_000_000_000
start = states.index(rolling)
cycle_len = len(states) - start
print(sum(len(data) - i for i, _ in states[((target - start) % cycle_len) + start]))
