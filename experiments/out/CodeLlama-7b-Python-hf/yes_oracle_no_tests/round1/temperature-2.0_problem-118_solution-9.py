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
    # RW 1
    # if ('a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word):
    #     return ""
    # else:
    #     for i in range(len(word)-1, 0, -1):
    #         if is_vowel(word[i-1]) and is_consonant(word[i]):
    #             return word[i-1]
    # return ""

    # RW 2
    # for i in range(len(word)-1, 0, -1):
    #     if is_vowel(word[i]):
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ""

    # RW 3
    # for i in range(len(word)-1, 0, -1):
    #     if is_vowel(word[i]):
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ""

    # RW 4
    # for i in range(len(word)-1, 0, -1):
    #     if is_vowel(word[i]):
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ""

    # RW 5
    # for i in range(len(word)-1, 0, -1):
    #     if is_vowel(word[i]):
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ""

    # RW 6
    # for i in range(len(word)-1, 0, -1):
    #    