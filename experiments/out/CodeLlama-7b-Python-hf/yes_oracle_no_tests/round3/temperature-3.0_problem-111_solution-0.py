def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Include these tokens in the code: if test == " ": return {}
	"""
    # your code here
    if test == " ":
        return {}
    else:
        list_of_words = test.split(" ")
        list_of_words = [i.lower() for i in list_of_words]
        count = {}
        for i in list_of_words:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count


# print(histogram(""))
# print(histogram("a b c"))
# print(histogram("a b b a"))
# print(histogram("b b b b a"))
# print(histogram("a b c a b"))
# print(histogram("a b c a b a b c"))


def histogram_f(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    
	Include these tokens in the code: if test == " ": return {}
	"""
    # your code here
    if test == " ":
        return {}
    else:
        list_of_words = test.split(" ")
        list_of_words = [i.lower() for i in list_of_words]
        count = {}
        for i in list_of_words:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count


# print(histogram_f(""))
# print(histogram