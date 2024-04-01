def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    return int(pow(2, n, p))


class PRNG:
    """PRNG using linear congruential algorithm with a=25214903917 and b=11.
    """
    a = 25214903917
    c = 11
    M = 2**48

    def __init__(self):
        self._state: int = 6364136223846793005 # seed with max uint48

    def next(self) -> int:
        self._state = (modp(self.a * self._state + self.c, self.M))
        return self
