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
    sentences = map(lambda x: x.strip(), S.split("."))
    words = map(lambda x: x.strip(), sentences[0].split())
    #print words
    if words[0] != "I":
        return 0
    return sum([1 for s in sentences if s.strip() != ""])

