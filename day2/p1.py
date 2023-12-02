import os


def create_dict(s: str) -> dict[str, int]:
	d = dict()
	for color in s.split(", "):
		n, c = color.split(" ")
		d[c] = int(n)
	return d


max_vals = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(": ")[1].split("; ") for l in f.read().splitlines()]

total = 0
for i, g in enumerate(data):
	g_dict = [create_dict(pull) for pull in g]
	valid = True
	for pull in g_dict:
		for k, v in pull.items():
			if v > max_vals[k]:
				valid = False
				break
	if valid:
		total += i + 1
print(total)
