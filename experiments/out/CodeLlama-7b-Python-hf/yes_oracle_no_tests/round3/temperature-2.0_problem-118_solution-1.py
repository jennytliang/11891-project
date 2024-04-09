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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pass get _
	"""
    vowels = "aeiouAEIOU"
    vowel_index = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_index.append(i)

    if len(vowel_index) == 0:
        return ""
    else:
        for i in range(len(vowel_index)-1):
            if vowel_index[i+1] - vowel_index[i] == 1:
                return word[vowel_index[i]+1]
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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: pass get _
	"""
    vowels = "aeiouAEIOU"
    vowel_index = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_index.append(i)

    if len(vowel_index) == 0:
        return ""
    else:
        for i in range(len(vowel_index)-1):
            if vowel_index[i+1] - vowel_index[i] == 1:
                return word[vowel_index[i]+1]
        return ""


def get_closest_vowel3(word):
    """You are given a