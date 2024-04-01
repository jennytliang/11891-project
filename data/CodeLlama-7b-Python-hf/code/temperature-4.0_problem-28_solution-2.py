from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    if strings == []: return ''
    else: return strings[0] if len(strings) == 1 else \
        (concatenate(strings[1:]) + strings[0])
 

if __name__ == '__main__':
    # import doctest

    # doctest.testmod()
    