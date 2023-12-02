import os
from math import prod


def create_dict(s: str) -> dict[str, int]:
	d = dict()
	for color in s.split(", "):
		n, c = color.split(" ")
		d[c] = int(n)
	return d


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.split(": ")[1].split("; ") for l in f.read().splitlines()]

total = 0
for g in data:
	max_vals = {
	    "red": 0,
	    "green": 0,
	    "blue": 0,
	}
	g_dict = [create_dict(pull) for pull in g]
	for pull in g_dict:
		for k, v in pull.items():
			if v > max_vals[k]:
				max_vals[k] = v
	total += prod(max_vals.values())
print(total)
