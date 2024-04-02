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
    # Rough Code:
    # for i in range(len(word)-1, 0, -1):
    #     if is_vowel(word[i]):
    #         for j in range(i-1, 0, -1):
    #             if is_consonant(word[j]):
    #                 for k in range(j-1, 0, -1):
    #                     if is_consonant(word[k]):
    #                         return word[i]
    # return ""

    # Refactored Code:
    for i in range(len(word)-1, 0, -1):
        if is_vowel(word[i]):
            for j in range(i-1, 0, -1):
                if is_consonant(word[j]):
                    return word[i]
    return ""


def is_vowel(ch):
    return ch in "AEIOUaeiou"


def is_consonant(ch):
    return not is_vowel(ch)


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("abcd") == ""
    assert get_closest_vowel("xxyy") == "y"
    assert get_closest_vowel("abcb") == ""
    assert get_closest_vowel("xyyzz") == "y"
    assert get_closest_vowel("aaaa") == ""
    assert get_closest_vowel("xxyyzz") == "y"
    assert get_closest_vowel("abcdefghijklmnopqrstuvwxyz") == "y"
    assert get_closest_vowel("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "Y"