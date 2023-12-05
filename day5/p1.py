from dataclasses import dataclass
import os


@dataclass
class MapRange:
	dst: int
	src: int
	size: int

	def convert(self, n: int) -> int | None:
		if self.src <= n < self.src + self.size:
			return self.dst + n - self.src
		return None


def convert(n: int, map_: list[MapRange]) -> int:
	for mr in map_:
		if (dst := mr.convert(n)) != None:
			return dst
	return n


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	almanac = f.read().split("\n\n")

seeds = list(map(int, almanac[0].split(": ")[1].split(" ")))
maps = [[MapRange(*map(int, r.split(" "))) for r in m.splitlines()[1:]] for m in almanac[1:]]

locs = []
for s in seeds:
	for m in maps:
		s = convert(s, m)
	locs.append(s)
print(min(locs))
