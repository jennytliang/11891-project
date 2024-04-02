def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Do not include these tokens in the code: # your code here
	"""
    return re.sub(r'  +', '-', text.replace(" ", "_"))


def split_punctuation(text):
    """
    Given a string text, replace all punctuation in it with spaces, 
    except for periods and commas. 
    If a word has more than 2 consecutive punctuation, 
    then replace all consecutive punctuation with -. 
    
    split_punctuation("Hello, world!") == "Hello , world !"
    split_punctuation("Hi.") == "Hi ."
    split_punctuation("...") == " - "
    split_punctuation("Hello,..,World") == "Hello , - , World"
    
	Do not include these tokens in the code: # your code here
	"""
    return re.sub(r'[^\.,]', r' ', text).replace('.,', '.').replace('.,', ',').replace('..', '-').replace('.,', '.').replace('.,', ',').replace('..', '-')


def replace_digits(text):
    """
    Given a string text, replace all digits in it with @. 
    
    replace_digits("Hello, my name is 12345") == "Hello, my name is @"
    replace_digits("1000 500") == "@@@@"
    replace_digits("1 one 5 five") == "@ one @@ five"
    
	Do not include these tokens in the code: # your code here
	"""
    return re.sub(r'\d', '@', text)


def replace_multiples(text):
    """
    Given a string text, replace all multiple letters with a single letter. 
    If a word has more than 2 consecutive letters, 
    then replace all consecutive letters with a single letter. 
    
    replace_multiples("Hello") == "Helo"
    replace_multiples("Hello, world!") == "Holo, world!"
    replace_multiples("aa bb cc dd ee") == "a b c d e"
    replace