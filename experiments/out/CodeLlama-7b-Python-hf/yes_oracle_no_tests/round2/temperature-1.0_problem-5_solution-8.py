from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: i
	Do not include these tokens in the code: index , number
	"""

    res = []
  
    # append all numbers to the res array 
    for i in range(0, len(numbers)):
        res.append(numbers[i])
 
    # iterate through the number array 
    for i in range(0, len(numbers)):

        # checks and inserts delimeter after every element
        if (i < len(numbers)-1):
            res.insert(2*i+1, delimeter)

    return res


def subsequence(word: str, letter: str) -> List[int]:
    """
    Return the first subsequence of `word' that starts with the character `letter'
    >>> subsequence("abc", "c")
    ['c', 'b', 'c']
    >>> subsequence("abc", "d")
    []
    >>> subsequence("abc", "a")
    ['a', 'b', 'c']
    >>> subsequence("aaaa", "b")
    []
    """
    result = word.split(",")
    return result
