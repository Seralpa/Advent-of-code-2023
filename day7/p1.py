from dataclasses import dataclass
from functools import total_ordering
from collections import Counter
import os
from typing import Self

card2value = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}


@dataclass
@total_ordering
class Hand:
	cards: str
	bid: int

	@property
	def type(self) -> int:
		count = Counter(self.cards).most_common()
		if count[0][1] == 4:
			return 5  # poker
		if count[0][1] == 5:
			return 6  # repoker
		if count[0][1] == 1:
			return 0  # high card
		if count[0][1] == 2 and count[1][1] == 1:
			return 1  # pair
		if count[0][1] == 2:
			return 2  # 2 pair
		if count[0][1] == 3 and count[1][1] == 1:
			return 3  # trio
		# if count[0][1] == 3:
		return 4  # full house

	def __eq__(self, other: Self):
		return other.cards == self.cards

	def __lt__(self, other: Self):
		if self.type != other.type:
			return self.type < other.type
		for sc, oc in zip(self.cards, other.cards):
			if sc != oc:
				return card2value[sc] < card2value[oc]


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [Hand(l.split(" ")[0], int(l.split(" ")[1])) for l in f.read().splitlines()]

data.sort()
print(sum((i + 1) * h.bid for i, h in enumerate(data)))
