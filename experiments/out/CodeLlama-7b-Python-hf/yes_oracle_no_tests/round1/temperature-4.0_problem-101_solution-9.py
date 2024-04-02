def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.replace(", ", " ").split()


def unique_list(l):
    """
    You will be given a list of integers in a variable nums. You have to remove all
    duplicates from the list, and return a list of unique values in the same order as they were in nums.
    
    For example:
    unique_list([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4]
    unique_list([1, 2, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4]
    unique_list([1, 2, 2, 3, 4, 4, 4]) == [1, 2, 3, 4]
    
    The order of the unique elements in the output list doesn't matter.
    """
    return list(set(l))


def reverse_list(l):
    """
    You will be given a list of integers in a variable nums. Your task is to reverse the list in place.
    
    For example:
    reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    reverse_list([1, 2, 3]) == [3, 2, 1]
    reverse_list([1, 2]) == [2, 1]
    
    Note: You should submit the revised list, don't change the function name or return anything.
    """
    return l[::-1]


def remove_negatives(l):
    """
    You will be given a list of integers in a variable nums. You have to remove all
    negative numbers from the list and return them as a separate list.
    
    For example:
    remove_negatives([1, 2, 3, -4, 5]) == [-4]
    remove_negatives([1, 3, 5, -4]) == [-4]
    remove