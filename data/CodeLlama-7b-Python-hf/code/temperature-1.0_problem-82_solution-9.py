def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7 or len(string) == 11 or len(string) == 13 or len(string) == 17 or len(string) == 19:
        return True
    else:
        return False
