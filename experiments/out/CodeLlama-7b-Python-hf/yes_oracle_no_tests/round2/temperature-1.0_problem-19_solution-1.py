from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""
    
    # SOLUTION 1:
    words = numbers.split()
    return " ".join(sorted(words))
    
    # SOLUTION 2:
    # tokens = []
    # for char in numbers:
    #     if char in [" ", "," ]:
    #         continue
    #
    #     if char not in tokens:
    #         tokens.append(char)
    #
    # tokens.sort()
    #
    # output = []
    # for token in tokens:
    #     output.append(token)
    #
    # return "".join(output)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
