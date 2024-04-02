def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    """STUDENT NOTES:
    Code from: https://stackabuse.com/python-strings-split-with-delimiters/:
    split (str=None, maxsplit=-1) - Splits the string into substrings if delimiters are encountered.
    The separator(s) (str) is passed as an argument, with none (or None) being the default value.
    This is useful for splitting a string into a list of substrings if the separator is encountered. 
    Example: 
    split('1,2;3-4:5', ',;:-') yields ['1', '2', '3', '4', '5']
   
    The maxsplit (int) is passed as an argument.
    If given, indicate that at most maxsplit splits should occur.
    Example:
    split('1,2;3-4:5', ',;:-', maxsplit=1) yields ['1,2', '3-4:5']
   
    The default value of maxsplit is -1 which is the maximum possible number of split times.
    """
    # split at delimiter
    token_list = S.split(".")
    token_list += S.split("?")
    token_list += S.split("!")
    # count how many sentences starting with "i"
    # return len([t for t in token_list if t.lower().startswith("i")])
    return len([s for s in token_list if s.islower() and s.startswith("i")])
