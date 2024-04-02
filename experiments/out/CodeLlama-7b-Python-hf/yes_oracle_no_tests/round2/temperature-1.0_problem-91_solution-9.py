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
    
	Include these tokens in the code: map ( lambda x : x
	Do not include these tokens in the code: S
	"""

    sentencelist = S.split(".")
    sentencelist = [x.strip() for x in sentencelist]
    sentencelist = [x for x in sentencelist if x]
    isbored = [True if x.split()[0] == "I" else False for x in sentencelist]
    return sum(isbored)


#print(is_bored("The sky is blue. The sun is shining. I love this weather"))
