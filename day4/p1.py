import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[nums.split(" ") for nums in l.split(": ")[1].split(" | ")] for l in f.read().splitlines()]

total = 0
for win, have in data:
	win_s = {int(n) for n in win if n != ""}
	have_s = {int(n) for n in have if n != ""}
	matches = len(win_s & have_s)
	if matches > 0:
		total += 2**(matches - 1)

print(total)
