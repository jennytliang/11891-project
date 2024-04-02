def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Do not include these tokens in the code: words = s . replace (" ","
	"""
    return s.split(", ")


def remove_empty(l):
    """
    Given a list, create a new list with all the empty values removed.
    
    For example:
    remove_empty([1, "", 3, "", 5]) == [1, 3, 5]
    remove_empty(["", "", "", "test", "", "not empty", "", "test", "empty"]) == ["test", "not empty", "test", "empty"]
    
    The order of the items in the new list should be the same as in the old list.
    
	Do not include these tokens in the code: new_list = l . filter (lambda x: x != "")
    """
    return list(filter(lambda x: x != "", l))


def even_keys(d):
    """
    Given a dictionary, create a new dictionary that only has the even keys from the original dictionary.
    
    For example:
    even_keys({1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}) == {2: "two", 4: "four"}
    even_keys({10: "ten", 11: "eleven", 12: "twelve"}) == {}
    
    The order of the keys in the new dictionary should be the same as in the original dictionary.
    
	Do not include these tokens in the code: new_dict = d . filter (lambda k, v: k % 2 == 0)
    """
    return dict(filter(lambda k, v: k % 2 == 0, d.items()))


def odd_values(d):
    """
    Given a dictionary, create a new dictionary that only has the odd values from the original dictionary.
    
    For example:
    odd_values({1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}) == {1: "one", 3: "three", 5: "five"}
    odd_values({10: "ten", 11: "eleven", 1