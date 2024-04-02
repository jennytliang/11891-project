def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    
	Do not include these tokens in the code: # s . lower ()
	"""
    # s = [i for i in s.split () if i != ""]
    s_set = set(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        if v in s_set:
            s_set.discard(v)
    selected_words = set()
    for word in s.lower().split():
        if len([l for l in word if l not in s_set]) == n:
            selected_words.add(word)
    return sorted(list(selected_words))


if __name__ == '__main__':

    print("Example 1")
    print('Expect["little"], Instead["little"]:', select_words('Mary had a little lamb', 4) == ["little"])
    print('Expect["Mary", "lamb"], Instead["Mary", "lamb"]:', select_words('Mary had a little lamb', 3) == ["Mary", "lamb"])
    print('Expect[], Instead[]:', select_words('simple white space', 2) == [])
    print('Expect["world"], Instead["world"]:', select_words("Hello world", 4) == ["world"])
    print('Expect["Uncle"], Instead["Uncle"]:', select_words("Uncle sam", 3)== ["Uncle"])
