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
    # Use these helper functions if necessary
    def is_vowel(ch):
        return ch in ['a','e','i','o','u']
    
    def is_consonant(ch):
        return ch in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    
    def is_vowel_between_consonants(word):
        if len(word) <= 2:
            return False
        return is_consonant(word[-1]) and is_consonant(word[-2]) and is_vowel(word[-3])
    
    if is_vowel_between_consonants(word):
        return word[-3]
    else:
        return ""
    
    # Alternatively, you may use this
    # Use slicing to check if the vowel is in the middle
    # if word[1:-1].count('a') or word[1:-1].count('e') or word[1:-1].count('i') or word[1:-1].count('o') or word[1:-1].count('u'):
    #     return word[1:-1][word[1:-1].index('a') or word[1:-1].index('e') or word[1:-1].index('i') or word[1:-1].index('o') or word[1:-1].index('u')]
    # else:
    #     return ""

    # You may use this code if you don't want to use helper functions
    # if len(word) <= 2:
    #     return ""
    # if word[-2] in ['a','e','i','o','u'] and word[-1] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
    #     return word[-3]
    # else:
    #     return ""

    # You may use this code if you don't want