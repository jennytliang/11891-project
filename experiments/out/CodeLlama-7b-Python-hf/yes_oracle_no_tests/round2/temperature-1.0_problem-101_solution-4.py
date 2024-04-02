def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words
	"""
    return s.replace(" "," ").split(",")

def get_hi(s):
    """
    Your task is to write a function that returns the amount of HI the string contains. 
    For example, "Hello, Hi" will return 2.

    As a reminder, in python you are able to access characters of a string by their index, 
    i.e. stringVariable[index]. Remember that indexing will be from 0 to `stringLength - 1`,
    and the last index would be stringLength - 1.
    """
    count = 0
    for i in [2, 3]:
        if s[i] == 'i':
            count+=1
            if s[i-1] == ' ' or s[i-2] == ' ':
                count+=1
    print('Hi' * count)
    return count

        



def string_splosion(str):
    """
    Write a function that receives a string and returns a new string made of every
    second character starting with the first, but each letter doubled.
    For example:
    stringSplosion('Code') === 'CCoode'
    stringSplosion('Code Jam') = 'CCoJamme'
    stringSplosion('') === ''
    """
    splosion = ''
    for i, letter in enumerate(str):
        if i % 2 == 0:
            splosion += letter * 2
    return splosion

def ArrayCount9(nums):
    """
    We have an array of integers, and an integer X.
    Our task is to write a function that counts the number of times that X occurs in the given array.
    For instance, the array [4, 3, 5, 4, 4, 5, 2, 3, 2] has two 4s, and zero 7s. We would then return 2.
    """
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

a = ArrayCount9([1,