from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    
    answer = []
    so_far = max(numbers)
    for i in numbers:
        so_far = max(so_far, i)
        answer.append(so_far)
    return answer



def is_palindrome(number: int) -> bool:
    """Checking if given number is palindrome.
    >>> is_palindrome(101)
    True
    
	Include these tokens in the code: return
	Do not include these tokens in the code: _ == reversed(str(_))
	"""
    
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
