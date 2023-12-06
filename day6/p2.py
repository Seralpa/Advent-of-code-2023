import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	time, distance = [int(line.split(":")[1]) for line in f.read().replace(" ", "").splitlines()]

options = 0
for ht in range(time):
	dist = ht * (time - ht)
	if dist > distance:
		options += 1
print(options)
