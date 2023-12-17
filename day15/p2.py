import os


def get_hash(label: str) -> int:
	curr = 0
	for c in label:
		curr += ord(c)
		curr *= 17
		curr %= 256
	return curr


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().split(",")

boxes = [dict() for _ in range(256)]

for ins in data:
	if "=" in ins:
		label, n = ins.split("=")
		hash_ = get_hash(label)
		boxes[hash_][label] = int(n)
	elif "-" in ins:
		label = ins[:-1]
		hash_ = get_hash(label)
		if label in boxes[hash_]:
			del boxes[hash_][label]

print(sum(i * j * v for i, b in enumerate(boxes, start = 1) for j, v in enumerate(b.values(), start = 1)))
