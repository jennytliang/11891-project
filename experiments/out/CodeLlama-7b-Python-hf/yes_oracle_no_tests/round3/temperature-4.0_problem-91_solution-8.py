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
    
	Include these tokens in the code: sentences = map ( lambda x : x
	Do not include these tokens in the code: # your code here if
	"""
    sentences = map(lambda x: x, S.split("."))
    boredom = 0
    for i in range(len(sentences)):
        if sentences[i][:2] == "I ":
            boredom += 1
    return boredom


def is_bored_2(S):
    return len([x for x in S.split(".") if x.startswith("I ")])
