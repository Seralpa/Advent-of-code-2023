word2num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("input.txt", "r") as f:
	data = f.read().splitlines()

total = 0
for line in data:
	n = 0
	numids = {9999999: -14}
	for k, v in word2num.items():
		if k in line:
			numids[line.index(k)] = v
	nid = min(numids.keys())
	nv = numids[nid]
	flag = False
	for i, c in enumerate(line):
		if c.isdigit():
			if i < nid:
				flag = True
				n += int(c) * 10
			break
	if not flag:
		n += nv * 10

	line = "".join(reversed(line))
	numids = {999999: -14}
	for k, v in word2num.items():
		if "".join(reversed(k)) in line:
			numids[line.index("".join(reversed(k)))] = v
	nid = min(numids.keys())
	nv = numids[nid]
	flag = False
	for i, c in enumerate(line):
		if c.isdigit():
			if i < nid:
				n += int(c)
				flag = True
			break
	if not flag:
		n += nv
	total += n
print(total)
