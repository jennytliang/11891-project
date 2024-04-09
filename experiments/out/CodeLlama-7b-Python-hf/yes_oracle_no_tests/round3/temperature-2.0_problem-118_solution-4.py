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
    
	Include these tokens in the code: owel
	Do not include these tokens in the code: ow
	"""


    de_vowels = "aeiou"
    vowels = "aeiouAEIOU"
    word = word.lower()
    vowel_pos = []
    for i, char in enumerate(word):
        if char in vowels:
            vowel_pos.append(i)

    if len(vowel_pos) == 0:
        return ""
    
    for i in range(len(vowel_pos)-1, -1, -1):
        if vowel_pos[i] > vowel_pos[-1] - 2:
            return word[vowel_pos[i]]

    return ""


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
    assert get_closest_vowel("ab") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("o") == ""
    assert get_closest_vowel("u") == ""
    assert get_closest_vowel("z") == ""
    assert get_closest_vowel("yogurtz") == "u"
    assert get_closest_vowel("yogurtzj") == "u"
    assert get_closest_vowel("yogurtjz") == "u"
    assert get_closest_vowel("yogurjt") == ""
    assert get_closest_vowel("yogurtju") == "u"
    assert get_closest_vowel("yogurtjuo") == "u"
    assert get_closest_vowel("yogurtoj") == ""
    assert get_closest_vowel("yogurtjo") == ""
    assert get_closest_vowel("yogurtoj") == ""
    assert get_closest_vowel("yogurtj") == ""
   