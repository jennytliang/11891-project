from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return _filter_by_substring(strings, substring)

def _filter_by_substring(current_list, substring, compare_list=[]):
    if not len(current_list):
        if not len(compare_list) or \
                _is_list_included(compare_list, []):
            compare_list.extend(compare_list[:])
            return compare_list
        return [] # We need a copy to not modify the reference

    res = []
    head_word = current_list.pop()
    
    # Compare to all items of current list
    if _is_list_included(compare_list, current_list):
        if substring:
            if (head_word in substring):
                res += current_list[:]
        else:
            res = current_list[:]

    return _filter_by_substring(current_list, substring, compare_list+res)
    

def filter_from_list_of_lists(input_lists:List[List[str]], filter_string: str):
    """ Filter a list of lists based on filter string. Filter is substring
        Return only the items that contain a substring
    
    
    """



def _is_list_included(first_list:List[str], other: List[str], other_idx=0):
    # Return False if any element in both lists is different and the idx is lower
    # Return True if we are already passed the head of other or there are just
    # two elements to check

    # if the index is lower or all the list are used return false
    if other_idx < 0 or (first_list and other_idx+1 == len(first_list) ) or \
        len(first_list) == 0:
        return False # We are too low or reach the last item of the list
    elif not other: # We have finished the first list, so it is included
        return True 

    # We are the head of another list, so include if the current one is included 
    # or if there is one element remaining

    curent_elem, rest = first_list.pop(other_idx) if other_idx <= len(first_list) else None, True
    
    return ((other and curent_elem==other.pop(0)) or len(other)==1) and \
        ( _is_list_included(first_list, rest, other_idx) if \
        (other_idx+1) < len(first_list))