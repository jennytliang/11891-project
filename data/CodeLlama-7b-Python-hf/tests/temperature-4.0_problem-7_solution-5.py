from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    # return list comprehension [string in string for string in list...]
    return [string for string in strings if (substring in string)]  # O(N2)


def get_unique_chars(word: str) -> int:
    """ Count the unique chars from a string (the chars must exist only once for each word)

    Args:
        - words (List): String to evaluate

    Examples:
     >>> get_unique_chars('abcac')
     'abcac'
    >>> [set(char) for char in 'wow'] = {'a'}, {'o'}, {'w'}. The result should only return the single unique characters
    """
    s = set() # O(1 or N)
    # [not a member]
    seen = set()  # size of each word = chars
    unique_chars = [char for char in word if (char not in seen) and (seen.add(char) is None) ]
                            # [len(word == 4) and word.set(word[index]) for word = 'abcd'] and word[index] == 'a' and [True or False] # (True = char not in set) 
    return unique





# for char in string if char not in set
# if char is not in string: 
# 	continue



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 'john') == []
    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']
    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']


check(filter_by_substring)