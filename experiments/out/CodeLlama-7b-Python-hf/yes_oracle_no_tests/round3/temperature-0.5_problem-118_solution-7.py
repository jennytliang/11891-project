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
    
	Include these tokens in the code: : str ) -> bool :
	Do not include these tokens in the code: ):
	"""

    def is_vow(letter):
        vowels = "aeiou"
        return letter in vowels

    def is_consonant(letter):
        vowels = "aeiou"
        return letter not in vowels

    def has_consonant_before(word):
        for i in range(len(word) - 1, 0, -1):
            if is_consonant(word[i]):
                return True
        return False

    def has_consonant_after(word):
        for i in range(len(word) - 1):
            if is_consonant(word[i]):
                return True
        return False

    def has_vow_after(word):
        for i in range(len(word) - 1):
            if is_vow(word[i]):
                return True
        return False

    # your code here
    if len(word) < 2:
        return ""

    if has_consonant_before(word) and has_consonant_after(word):
        for i in range(len(word) - 1, 0, -1):
            if is_vow(word[i]) and has_consonant_after(word[i+1:]):
                return word[i]

    if has_consonant_before(word) and has_vow_after(word):
        for i in range(len(word) - 1):
            if is_vow(word[i]) and has_consonant_after(word[i+1:]):
                return word[i]

    return ""
