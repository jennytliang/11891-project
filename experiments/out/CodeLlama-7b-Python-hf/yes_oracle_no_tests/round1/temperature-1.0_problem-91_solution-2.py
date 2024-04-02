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
     
    # Write your code here
    return lambda sent_list: sum(sent[0] == 'I' for sent in sent_list.split('.'))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
