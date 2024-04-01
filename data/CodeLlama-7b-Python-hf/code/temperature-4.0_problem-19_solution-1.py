from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    words: List[str] = [word for word, count in
                    map(
                        lambda number: (number[1],
                        number[1:-1]),
                        map(str.strip, numbers.lower().replace(".", "").replace(",", "").replace("and", "").split(" ")))]

    values: List[str]= ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def convert_position(number: str) -> int:
        
        return next((index for (index, item) in enumerate(values)
                        if item in number or number == item), 9)    

    return " ".join(words[index] for index
                    in sorted(map(lambda word:words.index(word), words),
                    key=convert_position)
                )

if __name__=="__main__":
    print(convert_position("five"))
