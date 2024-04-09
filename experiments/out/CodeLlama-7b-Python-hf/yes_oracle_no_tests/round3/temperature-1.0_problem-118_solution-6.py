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
    # Take advantage of the fact that the index of the last char is -1
    # and the index of the second last is -2
    #
    # 1. Find the index of the last vowel
    # 2. Find the index of the second last vowel
    # 3. Return the vowel between these two vowels
    #
    # Edge cases:
    # 1. Return '' if the word has no vowels
    # 2. Return '' if the word has only one vowel
    
    # Find the index of the last vowel
    #
    # Assumptions:
    # 1. The word only contains letters
    # 2. The word only contains uppercase letters
    # 3. The word only contains vowels and consonants
    last_vowel_index = -1
    for i in range(len(word)-1, -1, -1):
        if is_vowel(word[i]):
            last_vowel_index = i
            break
    
    if last_vowel_index == -1:
        # No vowels
        return ''
    
    # Find the index of the second last vowel
    #
    # Assumptions:
    # 1. The word only contains letters
    # 2. The word only contains uppercase letters
    # 3. The word only contains vowels and consonants
    second_last_vowel_index = -1
    for i in range(last_vowel_index-1, -1, -1):
        if is_vowel(word[i]):
            second_last_vowel_index = i
            break
    
    if second_last_vowel_index == -1:
        # No vowels
        return ''
    
    # Return the vowel between these two vowels
    return word[second_last_vowel_index+1:last_vowel_index+1]

def is_vowel(char):
    """
    Return true if the given char is a vowel
    """
    return char in "AEIOUY"