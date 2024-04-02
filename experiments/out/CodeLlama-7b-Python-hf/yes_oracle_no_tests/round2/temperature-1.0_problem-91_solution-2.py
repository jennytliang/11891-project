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
	Do not include these tokens in the code: # Write your code here
	"""
    sentences = map(lambda x: x.strip(), S.split("."))
    return len(filter(lambda x: x.startswith("I"), sentences))

print is_bored ("Hello world") == 0
print is_bored('The sky is blue. The sun is shining. I love this weather') == 1
print is_bored('It is boring. I am tired. Hence, I will sleep.') == 1
print is_bored('Boredom is interesting as boredom is the absence of boring
activity') == 1
print is_bored('I am tired. I slept now I will go watch a movie.') == 0
print is_bored('There are certain things that are boring. I think it would be a
good idea for you to go do those things.') == 0
print is_bored ('I am tired, I will sleep.') == 1
print is_bored("This statement might be interesting. This statement has
certainly been boring") == 0