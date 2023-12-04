import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[nums.split(" ") for nums in l.split(": ")[1].split(" | ")] for l in f.read().splitlines()]

n_copies = [1] * len(data)
for i, card in enumerate(data):
	winning = {int(n) for n in card[0] if n != ""}
	have = {int(n) for n in card[1] if n != ""}
	matches = len(winning & have)
	for i2 in range(i + 1, i + matches + 1):
		n_copies[i2] += n_copies[i]

print(sum(n_copies))
