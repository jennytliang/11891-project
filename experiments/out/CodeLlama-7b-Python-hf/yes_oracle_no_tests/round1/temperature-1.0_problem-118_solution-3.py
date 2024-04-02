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
    vowels = 'aeiou'
    if len(word) < 3:
        return ''
    vowels = [i for i in word if i in vowels]
    for i in range(-1, -len(word) - 1, -1):
        if word[i] not in vowels:
            if i + 2 < len(word) and word[i + 1] in vowels and word[i + 2] not in vowels:
                return word[i + 1]
    return ''


def get_closest_vowel2(word):
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
    vowels = 'aeiou'
    if len(word) < 3:
        return ''
    vowels = [i for i in word if i in vowels]
    for i in range(len(word) - 2, -1, -1):
        if word[i] not in vowels:
            if word[i + 1] in vowels and word[i + 2] not in vowels:
                return word[i + 1]
    return ''


def get_closest_vowel3(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the