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
    # Rough code
    # if len(word) < 4: return ''
    # if is_vowel(word[-1]): return ''
    # if is_vowel(word[-2]): return ''
    # if is_vowel(word[-3]): return ''
    # if is_vowel(word[-4]): return ''
    # return word[-3]
    # Need to check if vowel
    # Find index of first consonant
    # Find index of second consonant
    # return word[index_of_second_consonant]
    if len(word) < 4:
        return ''
    if is_vowel(word[-1]):
        return ''
    if is_vowel(word[-2]):
        return ''
    if is_vowel(word[-3]):
        return ''
    if is_vowel(word[-4]):
        return ''
    return word[-3]


def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u']


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("c") == ""
    assert get_closest_vowel("d") == ""
    assert get_closest_vowel("e") == ""
    assert get_closest_vowel("f") == ""
    assert get_closest_vowel("g") == ""
    assert get_closest_vowel("h") == ""
    assert get_closest_vowel("i") == ""
    assert get_closest_vowel("j") == ""
    assert get_closest_vowel("k") == ""
    assert