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
    # Take advantage of the fact that the word is in English
    if len(word) < 3:
        return ""
    for i in range(len(word)-2, 0, -1):
        if word[i].isalpha() and word[i].isupper():
            if is_vowel(word[i+1]) and is_consonant(word[i-1]):
                return word[i+1]
            elif is_vowel(word[i-1]) and is_consonant(word[i+1]):
                return word[i-1]
    return ""

def is_vowel(ch):
    return ch in "AEIOUaeiou"

def is_consonant(ch):
    return ch in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"