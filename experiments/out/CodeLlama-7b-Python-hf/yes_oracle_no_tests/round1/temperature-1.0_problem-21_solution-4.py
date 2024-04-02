from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ number
	"""
    min_number = numbers[0]
    for n in numbers:
        if n < min_number:
            min_number = n
    if len(numbers) <= 1:
        return [0.0 if n == min_number else 1.0 for n in numbers]
    ma, mi = map(max, zip(*numbers)), map(min, zip(*numbers))
    return [0.0 if n == mi else (n - mi) / (ma - mi) for n in numbers]


from random import random


class BingoCage:
    """Cage of random numbers between 1 and n, which calls randint() only once."""

    def __init__(self, n):
        self.balls = list(range(1, n + 1))
        random()  # to seed the RNG
        self.index = 0
        self._pick_next_number()

    def _pick_next_number(self):
        self.index += 1
        randint = random() * len(self.balls)
        # if randint is an int, self.balls[int(randint)] will be what we want:
        self.number = self.balls[int(randint)]

    def pick(self):
        if self.index == len(self.balls):  # the cage is empty
            raise LookupError
        this_number = self.number
        self._pick_next_number()
        return this_number


def count_bingos(sizes, n_balls):
    """Given sequence of n's (sizes), find number of bingo cards possible,
    with n_balls balls total.
    >>> count_bingos(sizes=[4, 4, 2], n_balls=44)  # 7 bingo cages
    7

    >>> count_bingos(sizes=[1, 2, 3], n_balls=12)
    2
    >>> count_bingos(sizes=[1, 2, 3, 100], n_balls=12