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


def is_valid(game: list[dict[str, int]]) -> bool:
	for pull in game:
		for k, v in pull.items():
			if v > max_vals[k]:
				return False
	return True


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[create_dict(pull) for pull in l.split(": ")[1].split("; ")] for l in f.read().splitlines()]

print(sum([i + 1 for i, g in enumerate(data) if is_valid(g)]))
