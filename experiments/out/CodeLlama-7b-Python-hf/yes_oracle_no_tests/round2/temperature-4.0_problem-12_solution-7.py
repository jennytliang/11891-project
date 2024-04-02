from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Include these tokens in the code: max len =
	Do not include these tokens in the code: return
	"""

    if not strings:
        return None
    max_len = 0
    max_string = None
    for string in strings:
        string_len = len(string)
        if string_len > max_len:
            max_len = string_len
            max_string = string
    return max_string


def main():
    strings = []
    num_strings = int(input("How many strings? "))
    for _ in range(num_strings):
        strings.append(input("String: "))
    print(longest(strings))


if __name__ == "__main__":
    main()
