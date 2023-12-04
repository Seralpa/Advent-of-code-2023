import os
import re
import itertools as itt

not_digit = re.compile(r"[^\d]")


def is_symbol(s: str) -> bool:
	return (not s.isdigit()) and s != "."


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = f.read().splitlines()

total = 0
for i, line in enumerate(data):
	line_iter = iter(enumerate(line))
	for j, c in line_iter:
		if c.isdigit():
			# calculate lenght of num
			match = not_digit.search(line[j:])
			n_len = match.start() if match else len(line)

			# get all chars around the part
			i2_start = i - 1 if i > 0 else i
			i2_end = i + 2 if i < len(data) - 1 else i + 1
			j2_start = j - 1 if j > 0 else j
			j2_end = j + 2 if i < len(line) - 1 else j + 1
			around = (data[i2][j2_start:j2_end] for i2 in range(i2_start, i2_end))

			if any(is_symbol(x) for x in around):
				total += int(line[j:j + n_len])

			# skip the rest of num
			next(itt.islice(line_iter, n_len - 1, None), '')
print(total)
