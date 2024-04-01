from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    pass
"""
Hint #1:
One line solution.
Example:
>>> print('' if xs else ' '.join(xs))
Note: '' represents the NULL string.
Example #2:
>>> print("{}" if x == '' else "{{ {} }}".format(
    ''.join(map(lambda e: '{'+e+'}+{}+{', x))))

There are better ways to format output.
But since you are beginner, we'll keep them simple for now. Feel free to ask us for hints on that part if needed :)
Note: This might be the easiest implementation for this solution. But it gives you the wrong result for ["1","","{}"]
Why? 😅 😅 Because it uses the first non empty argument for the default formatting argument to print. And it should be a string or a string formatted using formatting arguments.
"""


"""
Testing: See tests/c_python_1/b_concatenate.py for testing. 
In the main code block are just a few functions to help run the tests in a dev environment.
""" 
__all__ = ['concatenate']    