from dataclasses import dataclass
from enum import Enum
from functools import total_ordering
from collections import Counter
import os
from typing import Self

card2value = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}


class HandType(Enum):
	HIGH_CARD = 0
	PAIR = 1
	TWO_PAIR = 2
	TRIO = 3
	FULL_HOUSE = 4
	POKER = 5
	REPOKER = 6


@dataclass
@total_ordering
class Hand:
	cards: str
	bid: int

	@property
	def type(self) -> HandType:
		match Counter(self.cards).most_common():
			case [(_, 5), *_]:
				return HandType.REPOKER
			case [(_, 4), *_]:
				return HandType.POKER
			case [(_, 3), (_, 2), *_]:
				return HandType.FULL_HOUSE
			case [(_, 3), (_, 1), *_]:
				return HandType.TRIO
			case [(_, 2), (_, 2), *_]:
				return HandType.TWO_PAIR
			case [(_, 2), (_, 1), *_]:
				return HandType.PAIR
			case _:
				return HandType.HIGH_CARD

	def __eq__(self, other: Self):
		return other.cards == self.cards

	def __lt__(self, other: Self):
		if self.type != other.type:
			return self.type.value < other.type.value
		for sc, oc in zip(self.cards, other.cards):
			if sc != oc:
				return card2value[sc] < card2value[oc]


cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [Hand(l.split(" ")[0], int(l.split(" ")[1])) for l in f.read().splitlines()]

data.sort()
print(sum((i + 1) * h.bid for i, h in enumerate(data)))
