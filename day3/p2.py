from dataclasses import dataclass
from math import prod
import os
import re
import itertools as itt

not_digit = re.compile(r"[^\d]")
pos_t = tuple[int, int]


@dataclass(frozen = True)
class Part:
	num: int
	positions: tuple[pos_t, ...]


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().splitlines()

pos2part: dict[pos_t, Part] = dict()
for i, line in enumerate(data):
	l_iter = iter(enumerate(line))
	for j, c in l_iter:
		if c.isdigit():
			match = not_digit.search(line[j:])
			n_len = match.start() if match else len(line)
			positions = [(i, j2) for j2 in range(j, j + n_len)]
			p = Part(int(line[j:j + n_len]), tuple(positions))
			for pos in positions:
				pos2part[pos] = p
			# skip the rest of num
			next(itt.islice(l_iter, n_len - 1, None), '')

total = 0
for i, line in enumerate(data):
	for j, c in enumerate(line):
		if c == "*":
			# get all digits around cog
			i2_start = i - 1 if i > 0 else i
			i2_end = i + 2 if i < len(data) - 1 else i + 1
			j2_start = j - 1 if j > 0 else j
			j2_end = j + 2 if i < len(line) - 1 else j + 1
			digits = [(i2, j2) for i2 in range(i2_start, i2_end) for j2 in range(j2_start, j2_end)]
			parts = set(pos2part[pos] for pos in digits if data[pos[0]][pos[1]].isdigit())

			if len(parts) != 2:
				continue

			total += prod(p.num for p in parts)
print(total)
