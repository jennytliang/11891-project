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
    # RW Combine all the steps into one
    # RW Use negative values to represent that there is no vowel
    # RW Loop through the string backwards
    # RW If the character is a vowel, check if there is a consonant on the left
    # RW If there is, return the vowel
    # RW If the character is a consonant, check if there is a vowel on the right
    # RW If there is, return the vowel
    # RW If you reach the end, return the vowel
    # RW If you reach the end, return the vowel
    # RW If there is no vowel, return an empty string
    # RW Use negative values to represent that there is no vowel
    # RW Loop through the string backwards
    # RW If the character is a vowel, check if there is a consonant on the left
    # RW If there is, return the vowel
    # RW If the character is a consonant, check if there is a vowel on the right
    # RW If there is, return the vowel
    # RW If you reach the end, return the vowel
    # RW If you reach the end, return the vowel
    # RW If there is no vowel, return an empty string
    vowels = "aeiou"
    idx = len(word) - 1
    closest_vowel = ""
    while idx >= 0:
        if word[idx].lower() in vowels:
            if idx > 0 and word[idx - 1].lower() in vowels:
                return word[idx].lower()
            if idx < len(word) - 1 and word[idx + 1].lower() in vowels:
                return word[idx].lower()
            break
        idx -= 1
    return closest_vowel


def get_closest_vowel_old(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels