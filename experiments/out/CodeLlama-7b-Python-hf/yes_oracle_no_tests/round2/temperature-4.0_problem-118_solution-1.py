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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # R ely ing on built -
	"""
    # Relying on built-in functions
    # return min(filter(str.isalpha, word))

    # Relying on my own built-in function
    # return min(word, key=is_vowel)

    # Relying on list comprehension
    # return min([c for c in word if c.isalpha() and is_vowel(c)])

    # Relying on list comprehension with filter
    # return min([c for c in word if c.isalpha() and is_vowel(c)], default="")

    # Relying on list comprehension with lambda
    # return min([c for c in word if c.isalpha() and is_vowel(c)], key=lambda x: x)

    # Relying on list comprehension with lambda
    # return min([c for c in word if c.isalpha() and is_vowel(c)], key=lambda x: x) or ""

    # Relying on list comprehension with lambda
    # return next((c for c in word if c.isalpha() and is_vowel(c)), "")

    # Relying on list comprehension with lambda
    # return next((c for c in word if c.isalpha() and is_vowel(c)), "") or ""

    # Relying on list comprehension with lambda
    # return next(filter(lambda x: is_vowel(x), word)) or ""

    # Relying on list comprehension with lambda
    # return next(filter(lambda x: is_vowel(x), word), "")

    # Relying on list comprehension with lambda
    return next((c for c in word if is_vowel(c)), "")


def is_vowel(char):
    return char in "aeiouAEIOU"


def test_get_closest_vowel():
    assert get_closest_vowel("yogurt") == "u"
    assert get_closest_vowel("FULL") == "U"
    assert get_closest_vowel("quick") == ""
   