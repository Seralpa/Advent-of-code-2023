from dataclasses import dataclass
import os


@dataclass
class MapRange:
	dst: int
	src: int
	size: int

	def convert(self, r: tuple[int, int]) -> tuple[int, int] | None:
		if self.src < r[0] + r[1] and r[0] < self.src + self.size:
			return self.dst + max(r[0], self.src) - self.src, r[1] - max((self.src - r[0]), 0) - max(((r[0] + r[1]) - (self.src + self.size)), 0)
		return None


def convert(r: tuple[int, int], map_: list[MapRange]) -> list[tuple[int, int]]:
	ranges = []
	for mr in map_:
		if (dst := mr.convert(r)) != None:
			ranges.append(dst)
	return ranges


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/test.txt") as f:
	almanac = f.read().split("\n\n")

seeds = list(map(int, almanac[0].split(": ")[1].split(" ")))
maps = [[MapRange(*map(int, r.split(" "))) for r in m.splitlines()[1:]] for m in almanac[1:]]
# add implicit mapranges
for i, m in enumerate(maps):
	prev_end = 0
	m.sort(key = lambda x: x.src)
	new_map = m[:]
	for mr in m:
		if prev_end < mr.src:
			new_map.append(MapRange(prev_end, prev_end, mr.src - prev_end))
		prev_end = mr.src + mr.size
	new_map.append(MapRange(prev_end, prev_end, 999999999))  # placeholder for integer infinity
	maps[i] = new_map

seed_ranges = zip(seeds[::2], seeds[1::2])
for m in maps:
	new_seed_ranges = []
	for r in seed_ranges:
		new_seed_ranges += convert(r, m)
	seed_ranges = new_seed_ranges
print(min(seed_ranges, key = lambda x: x[0])[0])
