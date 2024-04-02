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
    import re
    d = [re.findall(r"\b1\b",dates) for dates in date]
    
    if len(date)<1:
        return print(False)
    elif len(date)==11 and len(d[0])!=1:
        return print(False)
    # elif len(date)==12 and list(date[-4])!=['-']:
    elif len(date.split("-")[-1])==4 and len(re.findall(r"[^\d]+",date.split("-")[0]))==0:
        return print(False)
    elif int(date.split("-")[0])%2==0 and list(date.split("-")[0])[0]!=1:
        return print(False)
    elif int(date.split("-")[0][::2])!=int(date.split("-")[0][1::2]):
        return print(False)
    else:
        if int(date.split("-")[1].split("-")[0])<=0:
            return print(False)
        elif int(date.split("-")[1].split("-")[0])>31:
            return print(False)
        elif int(date.split("-")[1].split("-")[1])<=0:
            return print(False)
        elif int(date.split("-")[-1].split("-")[1])<=0:
            return print(False)
        elif (int(date.split("-")[-1].split("-")[0])!=2) and (int(date.split("-")[1].split("-")[1])>30):
            return print(False)
        elif (int(date.split("-")[-1].split("-")[0])==2) and (int(date.split("-")[-1].split("-")[1])>29):
            return print(False)
        else:
            return print(True)
