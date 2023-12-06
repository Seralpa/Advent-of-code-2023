import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	times, distances = [[int(n) for n in line.split(" ")[1:] if n] for line in f.read().splitlines()]

total = 1
for t, d in zip(times, distances):
	options = 0
	for ht in range(t):
		dist = ht * (t - ht)
		if dist > d:
			options += 1
	total *= options
print(total)
