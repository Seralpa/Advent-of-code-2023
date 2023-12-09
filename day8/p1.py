import os


def line2dict(s: str) -> tuple[str, tuple[str, str]]:
	k, v = s.split(" = ")
	v1, v2 = v.replace("(", "").replace(")", "").split(", ")
	return k, (v1, v2)


rl2int = {"R": 1, "L": 0}

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	instr = [rl2int[c] for c in f.readline().strip()]
	data = dict([line2dict(l) for l in f.read().strip().splitlines()])

curr = "AAA"
i = 0
while curr != "ZZZ":
	curr = data[curr][instr[i % len(instr)]]
	i += 1
print(i)
