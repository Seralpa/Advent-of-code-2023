from dataclasses import dataclass
from functools import total_ordering
import os
from typing import Self


@dataclass
@total_ordering
class MapRange:
	dst: int
	src: int
	size: int

	def convert(self, r: tuple[int, int]) -> tuple[int, int] | None:
		if self.src <= r[0] + r[1] and r[0] < self.src + self.size:
			return self.dst + max(r[0], self.src) - self.src, r[1] - max((self.src - r[0]), 0) - max(((r[0] + r[1]) - (self.src + self.size)), 0)
		return None

	def __lt__(self, other: Self):
		return self.src < other.src

	def __eq__(self, other: Self):
		return self.src == other.src


def convert(r: tuple[int, int], map_: list[MapRange]) -> list[tuple[int, int]]:
	ranges = []
	for mr in map_:
		if (dst := mr.convert(r)) != None:
			ranges.append(dst)
	return ranges


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	almanac = f.read().split("\n\n")

seeds = list(map(int, almanac[0].split(": ")[1].split(" ")))
seeds = list(zip(seeds[::2], seeds[1::2]))
maps = [sorted([MapRange(*map(int, r.split(" "))) for r in m.splitlines()[1:]]) for m in almanac[1:]]
# add implicit mapranges
for m in maps:
	prev_end = 0
	l = len(m)
	for i, mr in enumerate(m):
		if i >= l:
			break
		if prev_end < mr.src:
			m.append(MapRange(prev_end, prev_end, mr.src - prev_end))
		prev_end = mr.src + mr.size
	m.append(MapRange(prev_end, prev_end, 999999999))

location_ranges = []
for sr in seeds:
	srl = [sr]
	for m in maps:
		srl_aux = []
		for r in srl:
			srl_aux += convert(r, m)
		srl = srl_aux
	location_ranges += srl
print(min(location_ranges, key = lambda x: x[0])[0])
