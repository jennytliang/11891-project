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
    # Relying on built-in isvowel() function
    # if not isvowel(word[-1]):
    #     return ""
    # if not isvowel(word[0]):
    #     return ""
    # for i in range(len(word) - 1, 0, -1):
    #     if isvowel(word[i]):
    #         return word[i]
    # return ""

    # Using a custom function
    if not is_vowel(word[-1]):
        return ""
    if not is_vowel(word[0]):
        return ""
    for i in range(len(word) - 2, -1, -1):
        if is_vowel(word[i]):
            return word[i]
    return ""


def is_vowel(ch):
    return ch in "AEIOUaeiou"
