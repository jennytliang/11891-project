def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    counter = -2 # to start from -1 index, because index() return a found index from list. 
    howManyTimes=0
    for times in substring:
        if not (substring != string[counter] and substring != string[(counter)+1] and substring != string[counter]):
            if substring in string[counter:]: # if in string between 2 last indexes +
                substring = counter
                counter = substring + (string[(counter)].find(substring)) -1 # to get the same substring
            howManyTimes += 1

    

        if not substring == "":        
            while counter > (string[-1]+1):
                # reset counter back to start
                counter=-2
    
    counter = -2

    return howManyTimes

 