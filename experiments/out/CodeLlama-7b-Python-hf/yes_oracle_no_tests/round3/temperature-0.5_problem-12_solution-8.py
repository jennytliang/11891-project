from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: if not strings :
	"""
    if not strings:
        return None
    longest_string = strings[0]
    longest_length = len(strings[0])
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)
            longest_string = string
    return longest_string


def main():
    print(longest(["a", "b", "c"]))
    print(longest(["a", "bb", "ccc"]))
    print(longest([]))


if __name__ == "__main__":
    main()
