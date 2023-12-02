import os
from math import prod
from collections import defaultdict


def create_dict(s: str) -> defaultdict[str, int]:
	d = defaultdict(int)
	for color in s.split(", "):
		n, c = color.split(" ")
		d[c] = int(n)
	return d


def get_power(game: list[defaultdict[str, int]]) -> int:
	rgb = ["red", "green", "blue"]
	return prod([max([pull[c] for pull in game]) for c in rgb])


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[create_dict(pull) for pull in l.split(": ")[1].split("; ")] for l in f.read().splitlines()]

print(sum([get_power(game) for game in data]))
