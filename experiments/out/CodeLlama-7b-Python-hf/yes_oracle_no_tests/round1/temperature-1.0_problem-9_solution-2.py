from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    max_so_far : List = []
    for num in numbers:
        if len(max_so_far) == 0 or num >= num:
            max_so_far.append(num)
        else:
            max_so_far.append(max_so_far[-1])
    
    return max_so_far



def string_to_list(s:str) -> List[str]:
    """ From a given string, generate a list of characters.
    >>> string_to_list('1234556')
    ['1', '2', '3', '4', '5', '5', '6']
    """

    return [string[i] for i in range(len(string))]  # your code goes here


def string_to_tuple(s:str) -> List[Tuple[str]]:
    """ From a given string, generate a list of characters.
    >>> string_to_tuple('1234556')
    ['1', '2', '3', '4', '5', '5', '6']
    """

    return [(string[i], str(i)) for i in range(len(string))]  # your code goes here


def list_comprehension(s:str) -> List[str]:
    """ From a given string, generate a list of tuples, each tuple will contain 
    number of occurence of char for char in a given string. Example below :
    >>> list_comprehension('aabbacc')
    [('a',2), ('b',2), ('c',3)]

	Include these tokens in the code: return, +=, for
	Do not include these tokens in the code: list, for 
    """
    list_occurance = []
    tmp_num = tmp_char = ''
    for num in s:
        if num == tmp_num: continue
        tmp_num = num
        tmp_char = (num,0)
        list_occurance.append(tmp_char)
        for char in s:
            tmp_char = (num,tmp_char