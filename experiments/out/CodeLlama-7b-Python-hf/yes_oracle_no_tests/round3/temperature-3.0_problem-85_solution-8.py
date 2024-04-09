def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Do not include these tokens in the code: # Add your code here
	"""
    # Add your code here
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 0])



def count_vowels(s):
    """Given a string s, count the number of vowels in the string.

    Examples:
        count_vowels('hello') ==> 2 
        count_vowels('world') ==> 3 
    
    Do not include these tokens in the code: # Add your code here
    """
    # Add your code here
    return sum([1 for i in s if i.lower() in 'aeiou'])



def count_digits(s):
    """Given a string s, count the number of digits in the string.

    Examples:
        count_digits('hello') ==> 0 
        count_digits('world') ==> 0 
        count_digits('36') ==> 2 
        count_digits('123') ==> 3 
    
    Do not include these tokens in the code: # Add your code here
    """
    # Add your code here
    return sum([1 for i in s if i.isdigit()])



def count_upper(s):
    """Given a string s, count the number of uppercase letters in the string.

    Examples:
        count_upper('hello') ==> 2 
        count_upper('world') ==> 2 
        count_upper('HeLLo') ==> 2 
        count_upper('HeLLo') ==> 2 
    
    Do not include these tokens in the code: # Add your code here
    """
    # Add your code here
    return sum([1 for i in s if i.isupper()])



def count_lower(s):
    """Given a string s, count the number of lowercase letters in the string.

    Examples:
        count_lower('hello') ==> 3 
        count_lower('world') ==> 5 
        count_lower('HeLLo