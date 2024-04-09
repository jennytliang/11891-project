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
    2. The length of the email string is not greater than 100 characters.
    3. The email should be in the format: <name>@<domain>.<extension>
    4. The <name> is composed of letters, numbers, dashes (-), underscores (_) and dots (.).
    5. The <domain> is composed of letters, numbers, dashes (-), underscores (_) and dots (.).
    6. The <extension> is composed of letters.
    
    for example: 
    valid_email('bob_m@live.com') => True

    valid_email('bob-m@live.com') => False

    valid_email('bob_m@live.c') => False
    
	Include these tokens in the code:
    name = [a-zA-Z0-9-_.]
    domain = [a-zA-Z0-9-_.]
    extension = [a-zA-Z]
    """
    pass


def valid_password(password):
    """You have to write a function which validates a given password string and
    returns True if the password is valid otherwise False.
    The password is valid if all of the following rules are satisfied:
    1. The password string is not empty.
    2. The length of the password string is not less than 6 characters.
    3. The password should not contain any of the following characters: <, >, %, ", \, \, /, \t, \n, \r.
    For example:
    valid_password('12345') => False
    valid_password('1234567') => True
    valid_password('123456789') => True
    valid_password('1234567890') => False
    valid_password('<123