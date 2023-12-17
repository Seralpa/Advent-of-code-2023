import os

coord_t = tuple[int, int]


def gen_coords_in_dir(s: coord_t, d: coord_t, data: list[str], rolling: set[coord_t]) -> coord_t:
	curr = s
	while True:
		new = (curr[0] + d[0], curr[1] + d[1])
		if not (0 <= new[0] < len(data) and 0 <= new[1] < len(data[0])) or data[new[0]][new[1]] == "#" or new in rolling:
			return curr
		curr = new


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().splitlines()

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # nwse
rolling = {(i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == "O"}
states = []

while rolling not in states:
	states.append(rolling)
	for d in directions:
		rolling_sorted = sorted(list(rolling), key = lambda x: x[1 if d[0] == 0 else 0], reverse = sum(d) > 0)
		rolling = set()
		for ri, rj in rolling_sorted:
			rolling.add(gen_coords_in_dir((ri, rj), d, data, rolling))

target = 1_000_000_000
cycle_start = states.index(rolling)
cycle_len = len(states) - cycle_start
print(sum(len(data) - i for i, _ in states[((target - cycle_start) % cycle_len) + cycle_start]))
