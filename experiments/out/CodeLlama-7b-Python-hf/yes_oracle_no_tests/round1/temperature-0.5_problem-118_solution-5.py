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
    
	Include these tokens in the code:  def is _ v owel ( ch
	Do not include these tokens in the code: ow els =
	"""

    vowels = 'aeiouAEIOU'
    last_vowel_index = -1
    first_consonant_index = -1
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            last_vowel_index = i
        if word[i] not in vowels and first_consonant_index == -1:
            first_consonant_index = i
        if first_consonant_index != -1 and last_vowel_index != -1:
            break
    if last_vowel_index == -1 or first_consonant_index == -1:
        return ""
    return word[last_vowel_index]


def test_function():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("happy") == "a"
    assert get_closest_vowel("daily") == "a"
    assert get_closest_vowel("apple") == "a"
    assert get_closest_vowel("green") == "a"
    assert get_closest_vowel("oak") == ""
    assert get_closest_vowel("banana") == "a"
    assert get_closest_vowel("act") == ""
    assert get_closest_vowel("fruitful") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("act") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("b") == ""
    assert get_closest_vowel("bc") == ""
    assert get_closest_vowel("c") == ""
    assert get_closest_vowel("cde") == ""
    assert get_closest_vowel("cda") == "a"
    assert get_closest_vowel("cdaf") == "a"
    assert get_closest_vowel