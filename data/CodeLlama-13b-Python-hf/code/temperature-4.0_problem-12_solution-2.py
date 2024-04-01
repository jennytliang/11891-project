from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if strings == []:
        return None

    length = []
    max_length = 0
    for word in strings:
        length.append((len(word), word))  # Creates a tuple with the letters as key and the word
        if length[-1] > max_length:  # Gets the largest word
            max_length = length[-1]

    # Get the largest string, if it is a tie the first string will get selected
    for word in length:
        # Compare two first elements of each tuple until find the largest
        for string in strings:
            # Compares each string (from list) with all strings in the tuple if they match append them on the word
            # list. If is not appended it will be discarded
            if word[0] == len(string) and len(word) == 2:
                word.append(word[1])
        if word[0] == len(word[1]):  # Check only the list appended with the string tuple
            if len(word) == 3:
                longest_string = word
                return longest_string[1]
                
            return word