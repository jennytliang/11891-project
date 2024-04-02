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
    # R1 - O(N)
    vowels = 'aeiou'
    if len(word) < 3:
        return ''
    for i in range(len(word) - 2, 0, -1):
        if word[i].isalpha() and word[i].lower() in vowels and word[i + 1].isalpha() and word[i + 2].isalpha():
            return word[i]
    return ''

    # R2 - O(N)
    # vowels = 'aeiou'
    # if len(word) < 3:
    #     return ''
    # for i in range(len(word) - 2, -1, -1):
    #     if word[i].isalpha() and word[i].lower() in vowels:
    #         if not word[i + 1].isalpha():
    #             return word[i]
    #         if not word[i + 2].isalpha():
    #             return word[i]
    # return ''

    # R3 - O(N)
    # vowels = 'aeiou'
    # if len(word) < 3:
    #     return ''
    # for i in range(len(word) - 2, -1, -1):
    #     if word[i].isalpha() and word[i].lower() in vowels and word[i + 1].isalpha() and word[i + 2].isalpha():
    #         return word[i]
    # return ''

    # R4 - O(N)
    # vowels = 'aeiou'
    # if len(word) < 3:
    #     return ''
    # for i in range(len(word) - 2, -1, -1):
    #     if word[i].isalpha() and word[i].lower() in vowels and word[i + 1].isalpha() and word[i + 2].isalpha():
    #         return word[i]
    # return ''

    #