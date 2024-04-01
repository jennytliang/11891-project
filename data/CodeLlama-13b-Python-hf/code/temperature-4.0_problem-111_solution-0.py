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
        mc = min(list(test)[:-2].count(test[-1]),) + 1

        # if it is, add the value to the string to store
        val_mc.append(test[-1])  # <----------- THIS
        mc_value = min(list['value'].split())

        dict['value'] = list(['value'].split(' '))[
            len(val_list_mc) == max_common]  # <--------
        return(dict)
    else:
        return(None)                                     ## <------


val = "a b b b a a a"
print(val, histogaram(val))
# print(test)