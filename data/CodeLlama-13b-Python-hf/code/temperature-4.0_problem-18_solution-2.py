def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    counter = 0
    if len(string) == 0 or len(string) <= len(substring):
        return counter
    
    start_index = 0
    
    while start_index != len(string):
        try:
            next_index = 1 + string.index(substring, start_index)
            start_index = next_index
            counter += 1
            
        except ValueError:
            break

    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()