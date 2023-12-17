import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [list(l) for l in f.read().splitlines()]

for i, l in enumerate(data):
	for j, c in enumerate(l):
		if c != "O":
			continue
		data[i][j] = "."

		for i2 in range(i, -2, -1):
			if i2 == -1 or data[i2][j] != ".":
				data[i2 + 1][j] = "O"
				break

print(sum(l.count("O") * (len(data) - i) for i, l in enumerate(data)))
