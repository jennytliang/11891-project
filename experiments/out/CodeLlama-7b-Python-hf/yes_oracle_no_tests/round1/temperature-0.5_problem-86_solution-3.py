def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code:  words = s . split (" ")
	"""

    # Code here
    def anti_shuffle_helper(s):
        if s == "":
            return s
        else:
            return anti_shuffle_helper(s[1:]) + s[0]
    
    def anti_shuffle_helper2(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper2(s[1:])
    
    def anti_shuffle_helper3(s):
        if s == "":
            return s
        else:
            return anti_shuffle_helper3(s[1:]) + " " + s[0]
    
    def anti_shuffle_helper4(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper4(s[1:])
    
    def anti_shuffle_helper5(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper5(s[1:])
    
    def anti_shuffle_helper6(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper6(s[1:])
    
    def anti_shuffle_helper7(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper7(s[1:])
    
    def anti_shuffle_helper8(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper8(s[1:])
    
    def anti_shuffle_helper9(s):
        if s == "":
            return s
        else:
            return s[0] + anti_shuffle_helper9(s[1:])
    
    def anti_shuffle_helper10(s):
        if s == "":
            return s
        else:
            return s[0]