def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: +
	"""

    return " ".join(map(str, rage(n + 1)))


def rage(n: int) -> list[int]:
    """ Return a list of numbers from 0 to n inclusive.
    >>> rage(5)
    [0, 1, 2, 3, 4, 5]
    >>> rage(0)
    [0]
    >>> rage(1)
    [0, 1]

    Example solution:
    # line 1
    if n == 0:
        # line 2
        return [0]
    # line 3
    return range(n + 1)
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("3")
    # END OF SOLUTION


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "3" == out
    for i in range(0, 10):
        if i != 3:
            assert str(i) != out


if __name__ == '__main__':
    check(string_sequence)
