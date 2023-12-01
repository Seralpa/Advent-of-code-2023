word2num = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def get_first_digit(s: str) -> int:
	for c in s:
		if c.isdigit():
			return int(c)
	raise ValueError(f"No digits in string {s}")


def get_cal_value(s: str) -> int:
	for k, v in word2num.items():
		s = s.replace(k, v)
	return get_first_digit(s) * 10 + get_first_digit(s[::-1])


with open("input.txt", "r") as f:
	print(sum([get_cal_value(l) for l in f]))
