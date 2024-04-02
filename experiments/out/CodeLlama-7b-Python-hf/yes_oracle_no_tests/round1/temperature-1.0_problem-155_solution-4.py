def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    for ch in str(abs(num)):
        if int(ch) % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd


def sum_divisible_by(n):
    """ return the sum of all the numbers between 1 and 1000
      that are divisible by input number n.
      return -1 if no number is divisible.

      example:
        sum_divisible_by(5) ==> 161
        sum_divisible_by(3) ==> 161
    """
    total = 0
    for i in range(1, 1001):
        if i % n == 0:
            total += i
    print(total)
    return total


def repeat_character(char):
    """ Given a character return a string that has the same character repeating 1, 2, 3 times
      The order of the return values does not matter
      return all the string values as a list
      example:
        repeat_character("*") ==> ['**', '***']
        repeat_character("-") ==> ["---", "----"]
      Use a loop rather than calculating repetitions
    """
    result = []
    for i in range(1, 4):
        result.append(char * i)
    result


def has_no_e(stringa):
    return True if not "e" in stringa else False


def has_no_e_fn(stringa):
    return stringa.find("e") == -1


n = 1245
even, odd = even_odd_count(n)

assert sum_divisible_by(5) == 161, "incorrect result."

assert sum_divisible_by(3) == 161, "incorrect result."
assert repeat_character("*") == ["**", "***"], "incorrect result."
assert repeat_character("-") == ["---", "----"], "incorrect result."

assert has_no