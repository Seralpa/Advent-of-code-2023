with open("input.txt", "r") as f:
	data = f.read().splitlines()

total = 0
for line in data:
	n = 0
	for c in line:
		if c.isdigit():
			n += int(c) * 10
			break
	for c in reversed(line):
		if c.isdigit():
			n += int(c)
			break
	total += n
print(total)
