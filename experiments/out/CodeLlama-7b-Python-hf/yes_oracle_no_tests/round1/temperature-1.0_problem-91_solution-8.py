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
    count = 0
    sentences = S.split('. ')
    for s in sentences:
        if 'I' == s.split()[0]:
            count += 1
    return count

print(is_bored("Hello, World!"))
print(is_bored("The sky is blue. The sun is shining. I love this weather."))
print(is_bored("I am happy. Boredom gives way to boredom."))
print(is_bored("We have met the enemy and they're now our friends. I wish we
        could be more like them"))    
