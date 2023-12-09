import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[int(n) for n in l.split(" ")] for l in f.read().splitlines()]

total = 0
for l in data:
	while any(l):
		total += l[-1]
		l = [n2 - n1 for n1, n2 in zip(l, l[1:])]
print(total)
