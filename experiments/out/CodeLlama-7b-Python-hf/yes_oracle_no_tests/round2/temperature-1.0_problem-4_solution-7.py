from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: (
	Do not include these tokens in the code: ([
	"""


    mean = sum(numbers) / len(numbers)
    retu = 0
    for i in range(len(numbers)):
      retu += abs(numbers[i] - mean)
    retu = retu / len(numbers)
    return retu


if __name__ == '__main__':
   
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_val(req, fields):
        req_fields = set(fields)
        for r in req:
            req_fields.add(r[0])
        return sorted(req_fields) == sorted(set(fields))

    # or you can use
    # req_fields.difference(fields) empty?
    # or
    # set(fields) == set(req_fields)

    assert json_val([['project', 'name', 'status'],
                      ['id', 1, 'COMPLETED'],
                      ['name', 'Software Design', 'STARTED'],
                      ['id', 2, 'IN DEVELOPMENT']],
                     ["name", "id", "status"])

    assert not json_val([['project', 'name', 'status'],
                          ['id', 1, 'COMPLETED'],
                          ['name', 'Software Design', 'STARTED'],
                          ['id', 2, 'IN DEVELOPMENT']],
                         ["project", "id", "status", "priority"])


    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
