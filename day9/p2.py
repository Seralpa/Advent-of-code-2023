import os

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [[int(n) for n in l.split(" ")] for l in f.read().splitlines()]

total = 0
for l in data:
	l_aux = l[:]
	first_digits = []
	while any(l_aux):
		first_digits.append(l_aux[0])
		l_aux = [n2 - n1 for n1, n2 in zip(l_aux, l_aux[1:])]
	ext = 0
	for d in reversed(first_digits):
		ext = d - ext
	total += ext
print(total)
