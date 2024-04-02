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
    # Your code here
    if test == " ":
        return {}
    t = test.split()
    d = {}
    for e in t:
        d[e] = d.get(e, 0) + 1
    return d

print(
    histogram(
        "s s i i s d f s a d f s adsf asdf asdf asdf asdf asdf asdf asdf asdf asdf"
    )
)
