from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == ''
    assert candidate(['a', 'b', 'c']) == 'abc'
    assert candidate(['a', 'b', 'c', 'd']) == 'abcd'


if __name__ == '__main__':
    check(concatenate)
