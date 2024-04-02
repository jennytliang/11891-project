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
    word = word + '_'  # add a special token to represent left of the vowel

    idx = None  # index of the next right consonant
    for i, ch in enumerate(word):
        if is_vowel(ch):
            newest_vowel = ch
            idx = i
        elif not is_vowel(ch) and idx is not None:
            if idx < i - 1:
                old_consonant = ch + word[i + 1]
                new_consonant = ch + newest_vowel
                idx = None  # reset idx
            elif idx > i + 1:
                old_consonant = newest_vowel + word[:idx]
                new_consonant = newest_vowel + ch + newest_vowel
                idx = None  # reset idx
            elif idx == i - 1:
                new_consonant = ch + newest_vowel
    if idx == None:
        return ''
    else:
        return old_consonant[1]


def is_vowel(ch):
    return ch.upper () == "A" or ch.upper () == "E" or ch.upper () == "I" or ch.upper () == "O" or ch.upper () == "U"


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("yogUrT") == "U"
    assert get_closest_vowel("yogUrTu") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("abc") == ""
    assert get_closest_vowel("bac") == "a"
    assert get_closest_vowel("cab") == "a"


if __name__ == '__main__':
    test_function()
