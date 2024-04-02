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
    
    for i in range(len(word) - 2, -1, -1):
        if is_vowel(word[i]):
            # There's a vowel (the closest left)
            if not is_vowel(word[i + 1]) and is_consonant(word[i + 2]):
                return word[i]
            
    # If nothing met the condition above
    return ""

def is_vowel(ch):
    return ch in ('A','a','E','e','I','i','O','o','U','u')

def is_consonant(ch):
    return not is_vowel(ch)


assert(get_closest_vowel("yogurt") == 'u')
assert(get_closest_vowel("FULL") == 'U')
assert(get_closest_vowel("quick") == '')
assert(get_closest_vowel("ab") == '')