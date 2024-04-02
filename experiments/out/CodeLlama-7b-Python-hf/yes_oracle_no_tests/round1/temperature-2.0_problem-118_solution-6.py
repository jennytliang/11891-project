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
    # R = len(word) - 1
    # while R >= 0:
    #     if isvowel(word[R]) == True:
    #         return word[R]
    #     R -= 1
    # return ""
    
    # def isvowel(ch):
    #     vowels = "aeiouy"
    #     return ch in vowels
    
    # return min(filter(isvowel, word[1:]), default='', key=word.rindex)
    
    # return min(filter(isvowel, word[1:]), key=word.rindex, default='')
    
    # return min(filter(isvowel, word[1:]), key=word.rindex) or ''
    
    # return min(filter(isvowel, word[1:]), key=word.rindex, default='')
    
    # return min(filter(isvowel, word[1:]), default='', key=word.rindex)
    
    # return min(filter(isvowel, word[1:]), default='', key=lambda x: word.rindex(x))
    
    # vowels = "aeiouy"
    # return min(filter(lambda ch: ch in vowels, word[1:]), default='', key=lambda x: word.rindex(x))
    
    # return min(filter(lambda ch: ch in vowels, word[1:]), default='', key=word.rindex)
    
    # return min(filter(lambda ch: ch in vowels, word[1:]), key=word.rindex) or ''
    
    # return min(filter(lambda ch: ch in vowels, word[1:]), key=word.rindex, default='')
    
    # return min(filter(lambda ch: ch in vowels, word[1:]), default='', key=lambda x: word.rindex(x))
    
    # return min(filter(lambda ch: ch in vowels, word[1:]), key=lambda x: word.rindex(x))