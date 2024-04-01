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
    i = len(word)-2
    while i > 0:
        if is_vowel(word[i]):
            return word[i]
        i -= 1
    return ""

def is_vowel(ch):
    return ch in "AEIOUaeiou"

def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("ABC") == ""
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("xyz") == ""
    assert get_closest_vowel("apple") == "e"
    assert get_closest_vowel("mmm") == ""
    assert get_closest_vowel("blabla") == "a"
    assert get_closest_vowel("vvv") == ""
    assert get_closest_vowel("nnn") == ""
    assert get_closest_vowel("ppp") == ""
    assert get_closest_vowel("rrr") == ""
    assert get_closest_vowel("ttt") == ""
    assert get_closest_vowel("wwwww") == ""
    assert get_closest_vowel("mmmmm") == ""
    assert get_closest_vowel("yyyyy") == ""
    assert get_closest_vowel("ooooo") == ""
    assert get_closest_vowel("uuuuu") == ""
    assert get_closest_vowel("iiii") == ""
    assert get_closest_vowel("aaaaa") == ""
    assert get_closest_vowel("jjjjj") == ""
    assert get_closest_vowel("bbbbb") == ""
    assert get_closest_vowel("ppppp") == ""
    assert get_clos