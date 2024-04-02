from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: if not strings : return None
	"""
    if not strings:
        return None
    strings.sort(key=len, reverse=True)
    return strings[0]


def main():
    print(longest(['a', 'b', 'c']))
    print(longest(['a', 'bb', 'ccc']))
    print(longest(['aa', 'bb', 'ccc']))
    print(longest(['aa', 'bbb', 'ccc']))
    print(longest(['aa', 'bbbb', 'ccc']))
    print(longest(['aa', 'bbbbb', 'ccc']))
    print(longest(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))


if __name__ == '__main__':
    main()
