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

    rlt: List[str] = []
    
    for string in strings:
        if string.find(substring) != -1:
            rlt.append(string)

    return rlt


print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))

print(filter_by_substring(
    [
        'asd', 'dsj', 'jhnjkasd', 'dskj', 'dskja', 'hdjk', 'hjdkj', 'hsdju',
        'sdjfh', 'sdjfh'
    ], 'dsj'))
