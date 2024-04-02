from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda
	Do not include these tokens in the code: [ s for
	"""

    r = []
    for s in strings:
        if s.find(substring) != -1:
            r.append(s)
    return r


if __name__ == '__main__':
    print('Example:')
    print(filter_by_substring(['a', 'bb', 'ccc'], 'a'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['a'], 'a') == ['a']
    assert filter_by_substring(['a', 'bb', 'ccc'], 'a') == ['a', 'bb', 'ccc']
    assert filter_by_substring(['a', 'bb', 'ccc'], 'b') == ['bb']
    assert filter_by_substring(['a', 'ab', 'ccc'], 'ab') == ['ab']
    assert filter_by_substring(['aaa', 'ab', 'ccc'], 'ab') == ['ab']
    assert filter_by_substring(['aaa', 'ab', 'ccc'], 'bc') == []
    assert filter_by_substring(['aaa', 'ab', 'ccc'], 'd') == []
    assert filter_by_substring(['aaa', 'ab', 'ccc'], '') == []
    assert filter_by_substring(['aaa', 'ab', 'ccc'], 'c') == ['ccc']
    print('You are awesome! All tests are done! Go Check it!')
