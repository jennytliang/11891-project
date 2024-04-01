from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    new_list = [delim if index != 0 else number if index + 1 < len(numbers) is None else number else delim if index + i <= len(numbers) else delim*i for i, number in enumerate(numbers)]
    delim = new_list[0] #delimiter to be added in between 1 and 2 of the list
    
    for i in new_list:
        delim+=new_list[index]

    
    return [index if index is None else delim+index for index, i in enumerate(list(range(size))) if index%2 == True]




def intersperse_(numbers,delimeter):
    """ another alternate function to interesperse a  list with delimiter """
    new_lst=[delimeter]
    for i in numbers[::1]:   
        add=[delimeter,i] 
    return add       