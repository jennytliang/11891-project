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
    if test == " ":
        return {}
    hist_dict = {}
    hist_array = test.split()
    for i in hist_array:
        if i not in hist_dict:
            hist_dict[i] = 1
        else:
            hist_dict[i] += 1
    
    if len(hist_dict) > 0:
        max_value = max(hist_dict.values())
        result_dict = {i:v for i,v in hist_dict.items() if v == max(hist_dict.values())}
    else: 
        return {}
    return result_dict

# TESTS
from functools import reduce
assert histogram('a b') == {'a': 1, 'b': 1}
assert histogram('a b a') == {'a': 2, 'b': 1}
assert histogram('a b a b') == {'a': 2, 'b': 2}
assert histogram('abcde fghi j') == {'a': 1, 'b': 1, 'c': 1, 'd':1, 'e':1, 'f':1, 'g':1, 'h':1, 'i':1}
assert histogram('') == {}
assert histogram('a b c !') == {}
assert histogram('a b A B') == {}
assert histogram('! ! !! !!! !!!!') == {}
assert histogram('') == {}
assert histogram('H e l l o w o r l d') == {'H':1, 'o': 2, 'r': 2, 'w':1, 'l':4}
assert histogram('s S D d D') == {'s':1, 'd':2}