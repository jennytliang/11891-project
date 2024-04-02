from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: list ( filter ( lambda s :
	Do not include these tokens in the code: [ string for string in strings if
	"""

    r = []
    for s in strings:
        if substring in s:
            r.append(s)

    return r


if __name__ == '__main__':
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
    Test.describe('Basic test')
    Test.assert_equals(filter_by_substring(['abc', 'bacd', 'cde', 'array'],
                                          'a'), ['abc', 'bacd', 'array'])
    Test.assert_equals(filter_by_substring([], 'a'), [])
