from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for k in range(len(strings)):
        r = r + strings[k] + " "
    return r[:-1]

print(concatenate(["A", "B", "C"]))
print(concatenate([]))
print(concatenate(["a", "b", "c"]))