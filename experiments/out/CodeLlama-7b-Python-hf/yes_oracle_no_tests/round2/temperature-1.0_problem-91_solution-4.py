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
    
	Do not include these tokens in the code: # Split sentence :
	"""
    i = -1
    for j in S:
        j=S[i]
        i-=1
        if j.isupper() and S[i+2] == "I":
            return 1
    return 0 