def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7 or len(string) == 11 or len(string) == 13 or len(string) == 17 or len(string) == 19 or len(string) == 23 or len(string) == 29 or len(string) == 31 or len(string) == 37 or len(string) == 41 or len(string) == 43 or len(string) == 47 or len(string) == 53 or len(string) == 59 or len(string) == 61 or len(string) == 67 or len(string) == 71 or len(string) == 73 or len(string) == 79 or len(string) == 83 or len(string) == 89 or len(string) == 97 or len(string) == 101:
        return True
    else:
        return False