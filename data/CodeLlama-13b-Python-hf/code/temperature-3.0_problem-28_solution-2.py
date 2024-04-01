from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


TEST_CONCATENATE_1 = [
    {
        'input': [],
        'expected': '',
    },
    {
        'input': ['a', 'b', 'c'],
        'expected': 'abc',
    },
]

