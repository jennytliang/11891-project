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
    # RW Combine the two functions together
    # Use the reverse function to get the closest vowel from the right side
    # Check if the vowel is between two consonants
    # If so, return the vowel
    # If not, return empty string
    pass


def get_closest_vowel_reverse(word):
    """Find the closest vowel that stands between two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.
    
    Example:
    get_closest_vowel_reverse("yogurt") ==> "u"
    get_closest_vowel_reverse("FULL") ==> "U"
    get_closest_vowel_reverse("quick") ==> ""
    get_closest_vowel_reverse("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    # RW Get the reverse of the word
    # Use the is_vowel function to check if the character is a vowel
    # If so, return the character
    # If not, check if the character is a consonant
    # If so, check if the character is the closest vowel to the right side
    # If so, return the character
    # If not, return empty string
    pass


def is_vowel(ch):
    """Check if the character is a vowel
    
    You may assume that the given string contains English letter only.
    
    Example:
    is_vowel("a") ==> True
    is_vowel("b") ==> False
    is_vowel("y") ==> True
    """
    # RW You may use the following tokens in the code
    # A vowel is defined as:
    # "AEIOUaeiou"
    pass


def is_consonant(ch):
    """Check if the character is a consonant
    
   