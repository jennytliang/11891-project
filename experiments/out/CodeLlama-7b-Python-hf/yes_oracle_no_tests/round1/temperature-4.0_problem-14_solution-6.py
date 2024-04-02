from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""
    return [string[:(i + 1)] for i in range(len(string))]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    
	Include these tokens in the code: return [ string [ i:
	"""
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: return [ all_prefixes
	"""
    return all_prefixes(string) + all_suffixes(string)


def all_substrings_no_duplicates(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings_no_duplicates('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: return [ list(set(all_
	"""
    return list(set(all_substrings(string)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
