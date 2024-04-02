def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # BEGIN PROBLEM 1
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
    # END PROBLEM 1


def reverse_string(string):
    """Given a string, return a reversed string.
    
    Example:
    reverse_string('apple') returns 'elppa'
    
    Hint: use slicing.
    """
    # BEGIN PROBLEM 2
    return str(string)[::-1]
    # END PROBLEM 2


def remove_middle(str):
    """Assume that the length of str is at least 3.

    Given a string, return a copy of the string with the middle character(s)
    removed.  If the length of str is odd, return the string with one middle
    character removed; if the length of str is even, return the string with two
    middle characters removed.  Do not mutate str.

    Example:
    remove_middle('abcd') returns 'ad'
    remove_middle('apple') returns 'aple'
    """
    # BEGIN PROBLEM 3
    return str[0] + str[-1]
    # END PROBLEM 3


def list_mutations(str):
    """Return a list of all possible non-empty proper subsets of the string str.

    The set of mutations S consists of:
        - an empty string,
        - str itself,
        - all strings of length 1 obtained by removing a single character,
        - all strings of length 2 obtained by removing a single pair of
          adjacent characters, and
        - all other strings obtained by removing any number of characters
          in the middle of str (not at the beginning or end).

    Examples:
    list_mutations('abc') returns ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
    list_mutations('abcd') returns ['',