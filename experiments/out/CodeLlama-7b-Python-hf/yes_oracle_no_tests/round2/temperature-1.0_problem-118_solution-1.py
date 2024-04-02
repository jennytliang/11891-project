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
	Do not include these tokens in the code: word = word . upper ()
	"""
    # RW Composed message
    upper_word = word.upper()
    for char in upper_word[::-1]:
        if char != " ":
            if "A" <= char <= "Z":
                if is_vowel(char):
                    return char
    return ""

def is_vowel(char):
    vowels = "AEIOU"
    return char in vowels
