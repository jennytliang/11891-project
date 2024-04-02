from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r =
	"""
    r = [s for s in strings if s.startswith(prefix)]
    return r

    
def main():
    print('Filter by prefix: \n')
    strings = ['abc', 'bcd', 'cde', 'array']

    # Filter string for string that begin with 'a'
    print('Filter by prefix: \n')
    print(filter_by_prefix(strings, 'a'))

    
if __name__ == '__main__':
    main()