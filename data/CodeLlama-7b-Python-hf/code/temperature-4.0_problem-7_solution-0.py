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
