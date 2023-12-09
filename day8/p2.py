import os
import math


def line2dict(s: str) -> tuple[str, tuple[str, str]]:
	k, v = s.split(" = ")
	v1, v2 = v.replace("(", "").replace(")", "").split(", ")
	return k, (v1, v2)


rl2int = {"R": 1, "L": 0}

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	instr = [rl2int[c] for c in f.readline().strip()]
	data = dict([line2dict(l) for l in f.read().strip().splitlines()])

curr_l = [s for s in data.keys() if s.endswith("A")]
loop_lens = []
for curr in curr_l:
	i = 0
	# this works because inputs are nice, every path has only one endpoint
	# and it loops back to the point right after start
	while not curr.endswith("Z"):
		curr = data[curr][instr[i % len(instr)]]
		i = (i + 1)
	loop_lens.append(i)
print(math.lcm(*loop_lens))
