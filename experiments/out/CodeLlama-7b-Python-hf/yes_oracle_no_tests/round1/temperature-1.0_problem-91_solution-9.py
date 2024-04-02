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
    sentences = S.split(".")
    sentences += S.split("?")
    sentences += S.split("!")
    return sum([sentence.split()[0] == "I" for sentence in sentences])


def is_bored2(S):
    return sum(sentence.split()[0] == "I" for sentence in S.split(".") + S.split("?") + S.split("!"))



def is_bored3(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1

    """
    return sum(sentence.split()[0] == "I" for sentence in S.split(".") + S.split("?") + S.split("!"))
