def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
    return s.split(", ")


def to_camel_case(s):
    """
    You will be given a sentence inputString. The sentence will be in camel case, such as "firstString".
    Convert this to snake case, as in "first_string".
    
    For this problem you should assume that any words in all_uppercase are meant to be treated as private
    class attributes, so you should not modify their casing when converting to snake case. Words in the
    inputString that contain both lower and upper case letters should be treated as camel case, not separate
    words.
    
    Examples
    to_camel_case("helloThere") == "hello_there"
    to_camel_case("hello_world") == "hello_world"
    to_camel_case("HelloWorld") == "Hello_world"
    to_camel_case("HELLOWORLD") == "HELLOWORLD"
    """
    return "_".join(a.lower() if i == 0 else a.title() for i, a in enumerate(s.split("_")))


def reverse_list(input_list):
    """
    Write a function to reverse a list. For example, if the list originally contained [1, 2, 3, 4],
    the call reverse_list would change it to [4, 3, 2, 1].
    
    Fill in the blanks in the code below to reverse a copy of this list.
    """
    return input_list[::-1]
