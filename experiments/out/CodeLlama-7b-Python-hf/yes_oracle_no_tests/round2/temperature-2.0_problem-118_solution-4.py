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

    def is_vow(x):
        return x in "aeiou"

    def is_con(x):
        return x in "bcdfghjklmnpqrstvwxyz"

    def is_vow_con(x):
        return is_vow(x) or is_con(x)

    def is_vow_con_vow(x):
        return is_vow(x) or is_con(x) or is_vow(x)

    def is_vow_con_con_vow(x):
        return is_vow(x) or is_con(x) or is_con(x) or is_vow(x)

    def is_vow_vow_con_vow(x):
        return is_vow(x) or is_vow(x) or is_con(x) or is_vow(x)

    def is_vow_vow_vow_con_vow(x):
        return is_vow(x) or is_vow(x) or is_vow(x) or is_con(x) or is_vow(x)

    if len(word) <= 1:
        return ""
    if len(word) == 2:
        return word[1] if is_vow_con(word[0]) and is_vow_con(word[1]) else ""
    if len(word) == 3:
        return word[1] if is_vow_con_con_vow(word) else ""
    if len(word) == 4:
        return word[2] if is_vow_vow_con_vow(word) else word[1] if is_vow_con_con_vow(word) else ""
    if len(word) == 5:
        return word[3] if is_vow_vow_vow_con_vow(word) else word[2] if is_vow_vow_con_vow(word) else word[1] if is_vow_con