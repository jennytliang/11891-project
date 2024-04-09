from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Do not include these tokens in the code: if len ( numbers ) == 0
	"""


    re = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            re.append(numbers[i])
        else:
            re.append(delimeter)
            re.append(numbers[i])

    return re



if __name__ == "__main__":
    import doctest
    doctest.testmod()
