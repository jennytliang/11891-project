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

    """
    # create variable to store most common string (or None) and a counter to store the highest number of occurance - if any

    # set counters to 1 to catch for empty array
    common_val = ''
    mc_count = 1

    dict = {}

    # Looping through the provided string to count every occurance and check if it matches highest count
    for i in test:
        mc = min(list(test)[:-2].count())

