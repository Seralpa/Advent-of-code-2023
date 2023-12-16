from dataclasses import dataclass
import os

repl_opts = [".", "#"]


def get_arrangements(s: str, groups: list[int]) -> int:
	if not "?" in s:
		return int([len(g) for g in s.split(".") if g != ""] == groups)

	arrangements = 0
	for r in repl_opts:
		arrangements += get_arrangements(s.replace("?", r, 1), groups)
	return arrangements


@dataclass
class SpringRow:
	springs: str
	groups: list[int]

	def get_arrangements(self) -> int:
		return get_arrangements(self.springs, self.groups)


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [SpringRow(l.split(" ")[0], list(map(int, l.split(" ")[1].split(",")))) for l in f.read().splitlines()]

print(sum(sr.get_arrangements() for sr in data))
