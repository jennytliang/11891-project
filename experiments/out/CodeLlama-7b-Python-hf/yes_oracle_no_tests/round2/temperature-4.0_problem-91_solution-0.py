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
    
	Include these tokens in the code: sentences
	Do not include these tokens in the code: words
	"""
    # your code here
    count = 0
    sentence_list = S.split(".")
    sentence_list = [sentence.strip() for sentence in sentence_list]
    for sentence in sentence_list:
        if sentence.startswith("I"):
            count += 1
    return count
    
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
print(is_bored("The sky is blue. The sun is shining. You are dumb"))
print(is_bored("I love this weather"))
print(is_bored("I hate this weather"))