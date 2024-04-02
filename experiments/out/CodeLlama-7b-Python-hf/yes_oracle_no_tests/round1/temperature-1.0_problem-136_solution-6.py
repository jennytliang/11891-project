def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    
	Include these tokens in the code: neg = list ( filter ( lambda x : x
	'''
    neg = list(filter(lambda x: x < 0, lst))
    pos = list(filter(lambda x: x > 0, lst))
    if not neg and not pos:
        return (None, None)
    elif not pos:
        return (max(neg), None)
    elif not neg:
        return (None, min(pos))
    else:
        return (max(neg), min(pos))


def num_to_str(num):
    '''
    Create a function that returns a string of number in words.

    Examples:
    num_to_str(123) == "one hundred twenty three"
    num_to_str(456789) == "four hundred fifty six thousand seven
    hundred eighty nine"
    num_to_str(101) == "one hundred one"
    num_to_str(1000) == "one thousand"
    num_to_str(1) == "one"
    num_to_str(100) == "one hundred"
    num_to_str(1000000) == "one million"
    num_to_str(1000000000) == "one billion"
    num_to_str(1000000000000) == "one trillion"
    num_to_str(0) == "zero"
    num_to_str(1234567890) == "one billion two hundred thirty four million
    five hundred sixty seven thousand eight hundred ninety"
    num_to_str(12345678901234567890) == "one hundred twenty three trillion
    four hundred fifty six billion seven hundred eighty nine million
    four hundred fifty six thousand seven hundred eighty nine"
    num_to_str(1234567890123456789012345678901234567890) == "one hundred
    twenty