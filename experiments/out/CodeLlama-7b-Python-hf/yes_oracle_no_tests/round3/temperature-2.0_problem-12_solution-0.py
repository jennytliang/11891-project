from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len = max ( len ( x ) for
	"""

    if not strings:
        return None

    # max_len = max(len(x) for x in strings)
    max_len = 0
    longest_string = strings[0]

    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_string = string

    return longest_string


def main():
    strings = input("Enter a list of strings separated by spaces: ").split()
    print(longest(strings))


if __name__ == '__main__':
    main()
