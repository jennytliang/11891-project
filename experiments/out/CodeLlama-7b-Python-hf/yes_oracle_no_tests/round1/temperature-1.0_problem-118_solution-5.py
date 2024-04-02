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
    word = word.lower()
    for i in range(len(word))[::-1]:
        ch = word[i]
        if ch.islower() and ch.isalpha() and is_vowel(ch):
            if i > 0 and is_consonant(word[i-1]) and \
               i + 1 < len(word) and is_consonant(word[i+1]):
                return ch     
    return ""


def is_vowel(char):
    return char.lower() in "aeiouy"

def is_consonant(char):
    return not is_vowel(char)