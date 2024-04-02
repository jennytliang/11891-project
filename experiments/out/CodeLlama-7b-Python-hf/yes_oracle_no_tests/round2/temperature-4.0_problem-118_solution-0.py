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
    if len(word) < 3:
        return ""

    # find the last consonant
    last_consonant_idx = -1
    for i in range(len(word)-1, 0, -1):
        if not is_vowel(word[i]):
            last_consonant_idx = i
            break

    if last_consonant_idx == -1:
        return ""

    # find the second last consonant
    second_last_consonant_idx = -1
    for i in range(last_consonant_idx-1, 0, -1):
        if not is_vowel(word[i]):
            second_last_consonant_idx = i
            break

    if second_last_consonant_idx == -1:
        return ""

    # find the closest vowel
    for i in range(second_last_consonant_idx+1, last_consonant_idx):
        if is_vowel(word[i]):
            return word[i]

    return ""

def is_vowel(ch):
    return ch in "AEIOUaeiou"


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ABCDEFGH") == "E"
    assert get_closest_vowel("ABCDEFGHU") == "E"
    assert get_closest_vowel("ABCDEFGHUY") == "Y"
    assert get_closest_vowel("ABCDEFGHUYI") == "I"
    assert get_closest_vowel("ABCDEFGHUYIOPQRSTUVWXYZ") == "O"
    assert get_closest_vowel("ABCDEFGHUYIOPQRST