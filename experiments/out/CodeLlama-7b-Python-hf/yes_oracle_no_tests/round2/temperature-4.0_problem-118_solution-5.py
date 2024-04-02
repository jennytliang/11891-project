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
    try:
        # get the index of the last consonant
        last_consonant_index = len(word) - 1 - word[::-1].index(word[0])
        
        # get the index of the second last consonant
        second_last_consonant_index = last_consonant_index - 1
        
        # get the index of the vowel between the last consonant and the second last consonant
        vowel_index = last_consonant_index - 1 - word[last_consonant_index - 1::-1].index("a")
        
        # return the vowel at the index
        return word[vowel_index]
    except:
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
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""
    try:
        # get the index of the last consonant
        last_consonant_index = len(word) - 1 - word[::-1].index(word[0])
        
        # get the index of the second last consonant
        second_last_consonant_index = last_consonant_index - 1
        
        # get the index of the vowel between the last consonant and the second last consonant
        vowel_index = last_consonant_index - 1