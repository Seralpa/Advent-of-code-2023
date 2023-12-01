def get_first_digit(s: str) -> int:
	for c in s:
		if c.isdigit():
			return int(c)
	raise ValueError(f"No digits in string {s}")


def get_cal_value(s: str) -> int:
	return get_first_digit(s) * 10 + get_first_digit(s[::-1])


with open("input.txt", "r") as f:
	print(sum([get_cal_value(l) for l in f]))
