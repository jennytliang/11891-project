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


def valid_email(email):
    """You have to write a function which validates a given email string and
    returns True if the email is valid otherwise False.
    The email is valid if all of the following rules are satisfied:
    1. The email string is not empty.
    2. The email address is not less than 3 characters or higher than 320 characters.
    3. The email address should be in the format: <name>@<domain>.<extension>
    4. The <name> should contain only letters and numbers.
    5. The <domain> should contain only letters.
    6. The <extension> should contain only letters.

    for example: 
    valid_email('user@example.com') => True

    valid_email('abc@abc.abc') => False

    valid_email('abc@abc.c') => False

    valid_email('abc@abc.com') => True
    
	Include these tokens in the code: name = [ 3 320 ,
	"""
    pass


def valid_password(password):
    """You have to write a function which validates a given password string and
    returns True if the password is valid otherwise False.
    The password is valid if all of the following rules are satisfied:
    1. The password should contain at least one uppercase letter.
    2. The password should contain at least one lowercase letter.
    3. The password should contain at least one number.
    4. The password should contain at least one special character.
    5. The password should contain at least 8 characters.
    6. The password should not contain spaces.
    for example: 
    valid_password('HelloWorld1') => True

    valid_password('HelloWorld') => False

    valid_password('Hello1') => True

    valid_password('HelloWorld!') => True
    
	Include these tokens in the code: name = [ 8 8 ,
	"""
    pass


def valid_number(number):
    """You have to write a function which validates a given number and returns
    True if the number is valid