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
    """
    date = ''.join(date.split('-'))

    if (len(date) != 14 
        or date[2] not in {'', '0'} 
        or len(date[2:]) > 14
        or date[2:].count(' ') != 8
        or date[5:].count(' ')[0] != date[6:].count(' ')
        or date[8].isdigit() and date[4] != ' ' and (int(date[8]) % 100 < 1 or int(date[8]) % 101 > 12)  # 1:101, yy (2digits), no space, yy
        or any(len(d) > 3 for d in date[::2].split())
        or date[3::2].strip('\n ')
        or any(date.replace(' ', '/', 2).count('/') == 0 for s in ['/m', '/ ', 'm ', ' m', '-d/', '-d ', '/d ', ' d/', 'dm'] if not (date.find('/') is None or date.find('/d') or date == '/') or any(date.rfind(d) and d != date[-2:] for d, l in ['7/', '11/'] if (date[-2], d) == ('12', '7' and int(date[-2]) in {20,16,20,32,48}) or any(date[-2],d in {'0','2','4','6','8'})))
        ):
        
        raise SystemExit


    return (len({date[:-8], date[5]}) != {0,2}, date[-8:], date[5], date[-6:-4], date[-2:])