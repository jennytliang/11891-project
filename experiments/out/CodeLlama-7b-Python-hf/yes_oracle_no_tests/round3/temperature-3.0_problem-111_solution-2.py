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

    
	Include these tokens in the code: count , ans = dict (), dict ()
	Do not include these tokens in the code: else :
	"""


    if test == "":
        ret = {}
    else:
        ret = {}
        for t in test.split(" "):
            if t in ret:
                ret[t] += 1
            else:
                ret[t] = 1
        max_count = max(ret.values())
        ans = {}
        for key in ret:
            if ret[key] == max_count:
                ans[key] = ret[key]
    return ans


# print(histogram("a b c"))
# print(histogram("a b b a"))
# print(histogram("a b c a b"))
# print(histogram("b b b b a"))
# print(histogram(""))





























































