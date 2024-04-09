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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: # R 1 - O
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = len(word) - 1
    while i > 0:
        if word[i] in vowels:
            #print(word[i])
            if i >= 2 and word[i-1] not in vowels:
                if word[i-2] not in vowels:
                    return word[i]
            elif i >= 1 and word[i-1] not in vowels:
                return word[i]
        i -= 1
    return ""

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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: # R 1 - O
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = len(word) - 1
    while i > 0:
        if word[i] in vowels:
            #print(word[i])
            if i >= 2 and word[i-1] not in vowels:
                if word[i-2] not in vowels:
                    return word[i]
            elif i >= 1 and word[i-1] not in vowels:
                return word[i]
        i -= 1
    return ""
    



def get