from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""

    result = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result


print(all_prefixes("abc"))
print(all_prefixes("abcb"))
print(all_prefixes("abcd"))
print(all_prefixes(""))
