FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = {i: s.count(i) for i in {'a', 'e', 'i', 'o', 'u', 'y'}} # why??
    result = count['y'] - int(s[-1] == 'y')
    res = max(result - 1, result) + count['y'] + sum(
        [count[i] for i in {*'aeiou'}] # why are we using ** ?
    )
    return (res % 5) + max(
        count['a'] - count['o'],  # can we put it in a list and then work with it? yes!
        # yes, but not in this problem. but there is an example at the end that does
        difference = count['a'] + count[i] # add the count of 'a', if a does not exist, defaults to `False`, otherwise 1

    difference
    difference.get('o') # this returns None, but `True`

    difference.has('o') == True # instead of the previous line, which is better to understand what is going on
"""