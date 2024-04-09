from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: _
	"""


    if not strings:
        return None

  #  strings.sort(key=len, reverse=True)

    return sorted(strings, key=len, reverse=True)[0]

    # return max(strings, key=len)
    # longest = ""
    # for string in strings:
    #     if len(string) > len(longest):
    #         longest = string
    # return longest


# print(longest([]))
# print(longest(["a", "b", "c"]))
# print(longest(["a", "bb", "ccc"]))
# print(longest(["a", "bb", "ccc", "dddd"]))
# print(longest(["a", "bb", "ccc", "dddd", "eeeee"]))
# print(longest(["a", "bb", "ccc", "dddd", "eeeee", "eeeee"]))
# print(longest(["a", "bb", "ccc", "dddd", "eeeee", "eeeee", "ffffff"]))


def longest_with_builtin(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    
	Do not include these tokens in the code: _
	"""


    return max(strings, key=len)

    # return max(strings, key=len)
    # longest = ""
    # for string in strings:
    #     if len(string) > len(longest):
    #         longest = string
    # return longest


# print(longest([]))
# print(longest(["a", "b", "c"]))
# print(longest(["a", "bb", "ccc"]))
# print(longest(["a", "bb", "ccc", "dddd"]))