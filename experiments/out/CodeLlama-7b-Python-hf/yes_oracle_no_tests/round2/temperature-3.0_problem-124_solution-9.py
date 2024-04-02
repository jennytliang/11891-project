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
    2. The length of the email string is not less than 3 or higher than 30.
    3. The email should contain a single @ character.
    4. The email should contain a single . character.
    5. The @ character should be before the . character.
    6. The email should have a length of at least 7 characters in the local part.
    7. The domain name should have a minimum length of 2 characters and maximum length of 25 characters.
    8. The domain name should contain only letters and numbers.
    9. The domain name should contain at least 1 letter.
    10. The email should be in the format: name@domain.extension

    for example: 
    valid_email('somename@somedomain.com') => True

    valid_email('somename@somedomain') => False

    valid_email('somename@somedomain.co') => False

    valid_email('somename@somedomain.co.uk') => True
    
	Include these tokens in the code: name = [ 3 1 ,
	"""
    pass


def valid_password(password):
    """You have to write a function which validates a given password string and
    returns True if the password is valid otherwise False.
    The password is valid if all of the following rules are satisfied:
    1. The password string is not empty.
    2. The length of the password string is not less than 6 or higher than 12.
    3. The password should contain at least 1 upper case letter.
    4. The password should contain at least 1 lower case letter.
    5. The password should contain at least 1 number.
    6. The password should contain at least 1 special character.
    7. The password should contain at least 1 character.
    8. The password