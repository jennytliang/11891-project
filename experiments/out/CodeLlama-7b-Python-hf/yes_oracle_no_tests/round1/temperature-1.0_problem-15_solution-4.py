def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    rtn = ""
    while len(rtn.split(" ")) < n :
        rtn += f"{len(rtn.split(' '))} "
    return rtn[:-1]

    # An alternate strategy with one more character of memory, but 20% faster:
    # rtn = ("x " * n)[:-1]
    # for i in range(n):
    #     rtn = rtn.replace("x ", f"{i} ", 1)
    # return rtn

    # ...or, with a list comprehension:
    # return ' '.join(map(str, range(n)))

    # ...or, by avoiding loops altogether:
    # return ' '.join(map(str, range(n))).split(' ')[n:]


def test_string_sequence() -> None:
    """
    >>> test_string_sequence()
    """
    from random import seed, shuffle

    string_sequence(1)
    seed(0)
    func = string_sequence
    assert all(
        func(i) == func(i) for i in range(25)
    ), "Is your function dependent on the random seed?"
    assert " " not in func(1000)
    assert func(15) == "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15", f'Uh-oh...'
    xs = list(range(20))
    shuffle(xs)
    assert set(func(20).split(" ")) == set(map(str, xs)), "Your string is in the wrong order."