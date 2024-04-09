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
    # Your code goes here
    if test == " ":
        return {}
    else:
        test = test.split(" ")
        test = "".join(test)
        test = test.lower()
        test = test.split()
        dict = {}
        for x in test:
            if x in dict.keys():
                dict[x] += 1
            else:
                dict[x] = 1
        return dict


# 	Another way
# 	import collections
# 	from collections import Counter
# 	dict = collections.Counter(test.lower().split())
# 	return dict
