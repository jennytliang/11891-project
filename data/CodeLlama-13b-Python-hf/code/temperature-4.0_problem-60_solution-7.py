def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    i, total = 1, 0
    while i <= n:
        total += i
        i += 1 
    return total

def reverse_string_recur(s):
    """Reverses a given string iteratively.
        Note: this is a recursive algorithm.
        Note: the string cannot be of type 'bytes' because of how pytest
        uses this function.

    Preconditions:
        s: a string 
        Ex: "I am codeneats"

    :param s: [a string to reverse in the given order]

    :return: [the same string with the order reversed and
                each character replaced with a reversed version]
    """
    # stop condition: no more characters left
    try:
        s[-1]
    except IndexError as e: 

        return ""
    
    # return one reversed character
    return(reverse_string_recur(s[1:]) + s[0])
