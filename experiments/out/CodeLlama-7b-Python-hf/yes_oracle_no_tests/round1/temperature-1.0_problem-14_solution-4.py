from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in filter(None, [string[i:] for i in range(len(string) + 1)])]
    # return "".join([string[0:i:] for i in range(len(string) + 1)])

    # return ["".join([string[0:i:] for i in range(len(string) + 1)])]


print(all_prefixes("ab"))
print(all_prefixes("abcd"))
# Test.assert_equals( all_prefixes('abc'), ['a', 'ab', 'abc'] )
# Test.assert_equals( all_prefixes(''), [''] )
# Test.assert_equals( all_prefixes('wxy'), ['w', 'wx', 'wxy'] )



# Additional examples
"""
print(all_prefixes("abc"))   ->  ['a', 'ab', 'abc']
print(all_prefixes(""))      ->  ['']
print(all_prefixes('wxy'))   ->  ['w', 'wx', 'wxy']
"""
