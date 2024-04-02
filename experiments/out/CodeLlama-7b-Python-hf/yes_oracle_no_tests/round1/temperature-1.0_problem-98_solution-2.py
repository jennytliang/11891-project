def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                cnt += 1
    return cnt


def count_upper_words(s):
    """
    Given a string s, count the number of words in s with an uppercase letter in the first position.
    
    For example:
    count_upper_words('a b C d e f') returns 2
    count_upper_words('a b c d e F') returns 3
    count_upper_words('A b c d e f') returns 1
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    cnt = 0
    for i in range(len(s)):
        if s[i].isupper():
            cnt += 1
    return cnt


def count_upper_sentence(s):
    """
    Given a string s, count the number of sentences in s with an uppercase letter in the first position.
    
    For example:
    count_upper_sentence('This is a sentence. And this is another sentence.') returns 2
    count_upper_sentence('This is a sentence. And this is another sentence?') returns 2
    count_upper_sentence('This is a sentence. And this is another sentence!') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    cnt = 0
    for i in range(len(s)):
        if s[i].isupper() and s[i-1] == ' ':
            cnt += 1
    return cnt


def count_upper_sentence_vowels(s):
    """
    Given a string s, count the number of sentences in s that have an uppercase vowel in the first position.
    
    For example:
    count_upper_sentence_vowels('This is a sentence. And this is another sentence.') returns 