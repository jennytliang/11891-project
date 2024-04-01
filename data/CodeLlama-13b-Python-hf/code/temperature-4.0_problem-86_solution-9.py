def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = [list(w) for w in s.split()]
    return ' '.join(map(lambda w: ''.join(sorted(list(w))),words))

    # return ','.join([w[0].upper()+sum(map(w.__delitem__.get(0),w.pop().lower())) if sum('a' in n and 'e' in n and 'y' in n for i in map(n.__len__,' '.join(map(str,[n[i]])+['_']).split(',')))==sum(n[i] for i in range(-len(n))) for w in sentence.lower().replace('.',' ').replace(',',' ') if sum(map(w.upper.get(i,' '),[' '+n for n in '-:;/\\\?!`~@$%^&"#*_+=<>[]{}|}{,.<>']))==0])

def test_function():
    assert anti_shuffle("Younger the mouse and his brother were eating cheezes and his sister-in") == "eYouhngertn the mourse and hbis brorker weatreing eaezzing and hihr sistr-in"