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
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: if len
	"""
    # RW Combine the code below
    # word = word.lower()
    # vowels = "aeiou"
    # for i in range(len(word)-1, 0, -1):
    #     if word[i] in vowels and word[i-1] not in vowels:
    #         return word[i]
    # return ""
    
    # RW Using zip
    word = word.lower()
    vowels = "aeiou"
    for i, j in zip(word[-1::-1], word[-2::-1]):
        if i in vowels and j not in vowels:
            return i
    return ""

    # RW Using enumerate
    # word = word.lower()
    # vowels = "aeiou"
    # for i, v in enumerate(word[-1::-1]):
    #     if v in vowels and word[-1-i] not in vowels:
    #         return v
    # return ""

    # RW Using zip
    # word = word.lower()
    # vowels = "aeiou"
    # for i, (a, b) in enumerate(zip(word[-1::-1], word[-2::-1])):
    #     if a in vowels and b not in vowels:
    #         return a
    # return ""

    # RW Using enumerate
    # word = word.lower()
    # vowels = "aeiou"
    # for i, (a, b) in enumerate(zip(word[-1::-1], word[-2::-1])):
    #     if a in vowels and b not in vowels:
    #         return a
    # return ""

    # RW Using enumerate
    # word = word.lower()
    # vowels = "aeiou"
    # for i, (a, b) in enumerate(zip(word[-1::-1], word[-2::-1])):
    #     if a in vowels and b not in v