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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.replace(' ', '')
    if len(word) < 3:
        return ""
    word = word[::-1]
    for i in range(len(word)):
        if word[i] in vowels:
            if word[i+1] in vowels:
                continue
            if word[i+2] in vowels:
                continue
            return word[i]
    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("happy") == "a"
    assert get_closest_vowel("aesthetic") == "i"
    assert get_closest_vowel("coconut") == "u"
    assert get_closest_vowel("vocal") == "a"
    assert get_closest_vowel("fine") == ""
    assert get_closest_vowel("e") == ""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("us") == ""
    assert get_closest_vowel("qu") == ""
    assert get_closest_vowel("q") == ""
    assert get_closest_vowel("x") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("f") == ""
    assert get_closest_vowel("o") == ""
    assert get_closest_vowel("k") == ""
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("happy") == "a"
    assert get_closest_vowel("aesthetic") == "i"
    assert get_closest_vowel("coconut") == "u"
    assert get_closest_vowel("vocal") == "a"
