import os


def find_reflection(pat: list[list[str]]) -> int | None:
	for i in range(1, len(pat)):
		reflection_len = min(i, len(pat) - i)
		found = True
		for j in range(reflection_len):
			if pat[i - 1 - j] != pat[i + j]:
				found = False
				break
		if found:
			return i
	return None


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[list(l) for l in pat.split("\n")] for pat in f.read().split("\n\n")]

total = 0
for pat in data:
	href = find_reflection(pat)
	vref = find_reflection(list(zip(*pat)))
	total += (vref if vref != None else 0) + 100 * (href if href != None else 0)
print(total)
