def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    
	Include these tokens in the code: days = [ 3 1 ,
	"""
    pass


def valid_credit_card_number(credit_card_number):
    """You have to write a function which validates a given credit card number.
    The credit card number is valid if all of the following rules are satisfied:
    1. The credit card number should be 16 digits.
    2. The credit card number should only contain digits.
    3. The sum of the odd digits should be equal to 2 times of the sum of the even digits.
    4. The credit card number should not start with 4,5,6 which are the IIN(issue number) of the credit card.
    For example: 4111-1111-1111-1111 is invalid.
    5. The credit card number should not start with 37,34,31 which are the IIN(issue number) of the American Express card.
    6. The credit card number should not start with 62,65 which are the IIN(issue number) of the UnionPay card.
    7. The credit card number should not start with 300-309,304,305,306,307,308,309 which are the IIN(issue number) of the Diner’s Club card.

    for example:
    valid_credit_card_number('4242424242424242') => True

    valid_credit_card_number('4111111111111111') => False

    valid_credit_card_number('6011-0000-0000-0000') => False

    valid_credit_card_number('378282246310005') => True
    
    Include these tokens in the code:
    odd_sum = 0
    even_sum = 0
    """
    pass


def is_vowel(letter):
    """You have to write a function which checks whether a given letter is a vowel or not.
