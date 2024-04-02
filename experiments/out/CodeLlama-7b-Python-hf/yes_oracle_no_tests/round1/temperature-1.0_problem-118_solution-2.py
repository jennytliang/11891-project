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
    # RW Comprehension
    # vowels = list("aeiouAEIOU")
    # return min([(i, word[i]) for i in range(len(word)-1, -1, -1) if word[i] in vowels and is_consonant(word[i+1]) and is_consonant(word[i-1])], key=lambda x: x[0])[1]

    # SOLUTION --------------------------------------------------
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels and is_consonant(word[i+1]) and is_consonant(word[i-1]):
            return word[i]
    return ""


def is_consonant(ch):
    vowels = "aeiouAEIOU"
    return ch not in vowels
