import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	time, distance = [int(line.split(":")[1]) for line in f.read().replace(" ", "").splitlines()]

print(sum(int(ht * (time - ht) > distance) for ht in range(time)))
