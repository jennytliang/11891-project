def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    pass

def has_more_than(words, threshold):
    """You are given a list of words. Your task is to return a list of words that
    have more than n letters.
    
    Example:
    has_morethan(["Hello", "World", "Baby"], 6) => ["Hello"]
    has_morethan(["Python", "Ruby", "Dart", "C"], 5) => [];
    has_morethan(["Hello", "World", "Baby"], 8) => ["Hello", "World"];
    """
    pass

def remove_substring(string, substring):
    """You are given a string and a substring. You have to remove all occurrences of 
    substring from string.
    
    Example:
    remove_substring("This is a good book to learn Python", "book") ==> "This is a good to learn Python"
    remove_substring("This is a book to learn Python", "oo") ==> "This is a book to learn Pythin"
    remove_substring("This is a book to learn Python", "this") ==> " is a book to learn Python"
    remove_substring("This is a book to learn Python", "zzz") ==> "This is a book to learn Python"
    
    Be aware of overlapping occurrences:
    remove_substring("Hello, Hello everyone", "llo") ==> "He, He everyone"
    
    You may assume that a string contains only lowercase English letters.
    """
    pass

def split(word, sep):
    """You are given a string and a char. You have to split the string from left to right,
    whenever the char is found in the string. If the chracter is not found anywhere, then 
    the word does not change in any case.
    
    Example:
    split("HelloWorld!", "o") ==> ["Hell","Wrld!"]
    split("Home", "a") ==> ["Home"]
    split("Homework", "s") ==> ["Homewo","re"]
    split("Pythonist", "z") ==> ["Pythonist"]
    
    Note: For the sake of simplicity, you