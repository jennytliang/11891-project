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
    # RW Combine word and vowels into a string
    vowels = "aeiouAEIOU"
    word_vowels = ""
    for ch in word:
        if ch in vowels:
            word_vowels += ch
    # RW Get the last vowel
    last_vowel = word_vowels[-1]
    # RW Get the last consonant
    last_consonant = word[-1]
    # RW Get the second last consonant
    second_last_consonant = word[-2]
    # RW Get the index of the last vowel
    index_last_vowel = word.find(last_vowel)
    # RW Get the index of the last consonant
    index_last_consonant = word.find(last_consonant)
    # RW Get the index of the second last consonant
    index_second_last_consonant = word.find(second_last_consonant)
    # RW Get the index of the rightmost consonant
    index_rightmost_consonant = index_last_consonant
    # RW If the last vowel is the last consonant
    if last_vowel == last_consonant:
        # RW Get the second last index of the last vowel
        index_second_last_vowel = word_vowels.find(last_vowel)
        # RW if there is a second last vowel
        if index_second_last_vowel != -1:
            # RW Get the index of the second last vowel
            index_second_last_vowel = index_second_last_vowel + index_second_last_consonant
            # RW If the index of the second last vowel is less than the index of the last vowel
            if index_second_last_vowel < index_last_vowel:
                # RW Get the second last consonant
                second_last_consonant = word[index_second_last_consonant]
                # RW Get the index of the