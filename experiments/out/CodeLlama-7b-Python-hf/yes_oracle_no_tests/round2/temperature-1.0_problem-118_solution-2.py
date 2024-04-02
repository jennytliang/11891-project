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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # R W Com pre h ension
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i in range(len(word)-1, 0, -1):
        if word[i-1] in vowels and word[i] in vowels:
            result = word[i-1]
            break
    return result


def get_closest_vowel_2(word):
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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # R W Com pre h ension
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i in range(len(word)-1, 0, -1):
        if word[i-1] in vowels and word[i] in vowels:
            result = word[i-1]
            break
    return result


def get_closest_vowel_3(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel