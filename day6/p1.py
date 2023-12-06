import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	times, distances = [[int(n) for n in line.split(" ")[1:] if n] for line in f.read().splitlines()]

total = 1
for t, d in zip(times, distances):
	total *= sum(int(ht * (t - ht) > d) for ht in range(t))
print(total)
