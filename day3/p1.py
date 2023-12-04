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
for i, l in enumerate(data):
	l_iter = iter(enumerate(l))
	for j, c in l_iter:
		if c.isdigit():
			# calculate lenght of num
			match = not_digit.search(l[j:])
			n_len = match.start() if match else len(l)

			# check if there is a symbol around
			n_pre = j - 1 if j > 0 else j
			n_post = j + n_len + 1 if match else j + n_len
			if i > 0:
				n = data[i - 1][n_pre:n_post]
			else:
				n = []
			if i < len(data) - 1:
				s = data[i + 1][n_pre:n_post]
			else:
				s = []
			w = l[j - 1] if j > 0 else "."
			e = l[j + n_len] if match else "."

			if any(is_symbol(x) for x in itt.chain(n, s, (w, e))):
				total += int(l[j:j + n_len])

			# skip the rest of num
			next(itt.islice(l_iter, n_len - 1, None), '')
print(total)
