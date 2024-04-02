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
    # word = ''.join(word.split())
    # if len(word) < 3:
    #     return ''

    # vowels = ['A', 'E', 'I', 'O', 'U']
    # for vowel in vowels:
    #     if is_vowel(vowel):
    #         return vowel

    # RW 2
    # vowels = 'AEIOU'
    # for i in range(len(word) - 1, 0, -1):
    #     if is_vowel(word[i]):
    #         if word[i-1] not in vowels and is_consonant(word[i-1]):
    #             if i + 1 < len(word) and word[i + 1] not in vowels and is_consonant(word[i + 1]):
    #                 return word[i]
    # return ''

    # RW 3
    # vowels = 'AEIOU'
    # for i in range(len(word) - 1, 0, -1):
    #     if word[i] in vowels:
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ''

    # RW 4
    # vowels = 'AEIOU'
    # for i in range(len(word) - 1, 0, -1):
    #     if word[i] in vowels:
    #         if is_consonant(word[i-1]) and is_consonant(word[i+1]):
    #             return word[i]
    # return ''

    # RW 5
    # vowels = 'AEIOU'
    # for i in range(len(word) - 1, 0, -1):
    #     if word[i] in vowels:
    #         if is_con