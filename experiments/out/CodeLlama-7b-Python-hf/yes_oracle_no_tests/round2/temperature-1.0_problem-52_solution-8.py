def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	Do not include these tokens in the code: result = True
	"""
    
    return all ( [x < t for x in l])
print(below_threshold([1, 2, 4, 10], 100))
from doctest import run_docstring_examples
run_docstring_examples(__doc__,globals(),True)