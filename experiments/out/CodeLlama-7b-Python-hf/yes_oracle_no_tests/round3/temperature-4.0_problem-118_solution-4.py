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
    # R1:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
                return word[i].lower()
            if word[i-1].isupper():
                return word[i].lower()
        i -= 1
    return ""

    # R2:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
                return word[i].lower()
        i -= 1
    return ""

    # R3:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
                return word[i].lower()
            if word[i-1].isupper():
                return word[i].lower()
        i -= 1
    return ""

    # R4:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
                return word[i].lower()
        i -= 1
    return ""

    # R5:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
                return word[i].lower()
            if word[i-1].isupper():
                return word[i].lower()
        i -= 1
    return ""

    # R6:
    vowels = 'aeiou'
    i = len(word)-1
    while i > 0:
        if word[i].islower():
            if word[i] in vowels:
               