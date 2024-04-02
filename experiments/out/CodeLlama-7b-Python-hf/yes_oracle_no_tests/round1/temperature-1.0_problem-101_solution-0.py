def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.replace(", ", " ")
	return words.split(" ")


def unique_list(l):
    """
    You will be given a list of integers. You have to return a list of unique values
    from the list in the order that they first appear.
    
    For example:
    unique_list([1, 5, 3, 1, 2, 3, 5, 1, 2, 4]) == [1, 5, 3, 2, 4]
    unique_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    Note that unique_list has to return a list and you have to return it in the same
    order that the values first appear in the given list.
    
    For example:
    a = [1, 1, 2, 3, 2, 1, 4, 5, 2]
    unique_list(a) == [1, 2, 3, 4, 5]
    """
    unique = []
    for i in l:
        if i not in unique:
            unique.append(i)
    return unique


def remove_duplicates(l):
    """
    You will be given a list of integers. You have to return a list of unique values
    from the list in the order that they first appear.
    
    For example:
    remove_duplicates([1, 5, 3, 1, 2, 3, 5, 1, 2, 4]) == [1, 5, 3, 2, 4]
    remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    Note that remove_duplicates has to return a list and you have to return it in the
    same order that the values first appear in the given list.
    
    For example:
    a = [1, 1, 2, 3, 2, 1,