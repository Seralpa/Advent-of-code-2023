import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().split(",")

total = 0
for ins in data:
	curr = 0
	for c in ins:
		curr += ord(c)
		curr *= 17
		curr %= 256
	total += curr
print(total)
