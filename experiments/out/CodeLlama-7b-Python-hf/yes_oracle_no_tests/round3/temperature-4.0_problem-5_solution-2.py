from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: [] if numbers == [] :
	"""

    
    if len(numbers) == 0:
        return numbers

    output = [numbers[0]]
    for i in range(1, len(numbers)):
        output.append(delimeter)
        output.append(numbers[i])

    return output


if __name__ == "__main__":
    import doctest

    doctest.testmod()
