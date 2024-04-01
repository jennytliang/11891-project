from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    if not prefix or not strings:
        return list() 
    filtered = list()    
    
    check_letter = prefix[0]
    prefix_length = len(prefix)
    for string in strings:
        # if first letter in string is the first letter in filter
        # or if all letters in filter is already matched
        if string[0] == check_letter and len(string) >= prefix_length:  
            if string[0:prefix_length]  == prefix:
                #add to the return list if the string start with the filter
                filtered.append(string)
            # else if there is enough letters to match the check letter, and they are not perfect match, then assign new letter checker, and remove last char from filter so we check both letters again
            # and repeat this loop until all chars match, or string not included in filter     
            elif string[1] != check_letter:   # not perfect match, update filter letter, remove 1 char from filter length                 
                check_letter = string[1]  # Update filter
                prefix_length -= 1 # Update prefix length to check
    return filter_by_prefix(strings, check_letter)    
        
    
            
    # return list without prefix string

    
    