def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	Do not include these tokens in the code: wo
	"""
    return s.replace(","," ").split()


def remove_n(s):
    """
    You will be given a string of words separated by commas, periods or spaces. Your
    task is to remove all commas, periods and spaces from the string and return the
    new string.
    
    For example:
    remove_n("Hi, my name is John.") == "Hmynameison"
    remove_n("One, two, three, four, five, six") == "Onetwothreefourfivesix"
    
	Include these tokens in the code: remove_n
	Do not include these tokens in the code: remove
	"""
    return s.replace(",","").replace(".","").replace(" ","")


def remove_n_v2(s):
    """
    You will be given a string of words separated by commas, periods or spaces. Your
    task is to remove all commas, periods and spaces from the string and return the
    new string.
    
    For example:
    remove_n_v2("Hi, my name is John.") == "Hmynameison"
    remove_n_v2("One, two, three, four, five, six") == "Onetwothreefourfivesix"
    
	Include these tokens in the code: remove_n, remove, n
	Do not include these tokens in the code: remove_n_v2
	"""
    return s.replace(" ","").replace(".","").replace(",","")


def remove_n_v3(s):
    """
    You will be given a string of words separated by commas, periods or spaces. Your
    task is to remove all commas, periods and spaces from the string and return the
    new string.
    
    For example:
    remove_n_v3("Hi, my name is John.") == "Hmynameison"
    remove_n_v3("One, two, three, four, five, six") == "Onetwothreefourfivesix"
    
	Include these tokens in the code: remove_n, remove, n
	Do not include