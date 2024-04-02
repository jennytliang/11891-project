def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s . replace (", ", " "
	"""
	words = s.replace(", ", " ").split(" ")
	return words


def unique_list(seq):
    """
    This function takes a list as an input and returns a list of unique elements in the input list.
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def is_prime(n):
    """
    This function takes a number as an input and returns True if the number is prime, False otherwise.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_primes(n):
    """
    This function takes a number as an input and returns the sum of all prime numbers up to the number.
    """
    return sum([x for x in range(2, n) if is_prime(x)])


def sum_primes_list(n):
    """
    This function takes a number as an input and returns a list of all prime numbers up to the number.
    """
    return [x for x in range(2, n) if is_prime(x)]


def max_key_dict(d):
    """
    This function takes a dictionary as an input and returns the key with the maximum value.
    """
    return max(d, key=d.get)


def max_key_dict_list(d):
    """
    This function takes a dictionary as an input and returns a list of the keys with the maximum value.
    """
    return [x for x in d if d[x] == max(d.values())]


def max_key_dict_list_str(d):
    """
    This function takes a dictionary as an input and returns a string of the keys with the maximum value.
    """
    return " ".join(max_key_dict_list(d))


def max_val_dict(d):
    """
    This function takes a dictionary as an input and returns the