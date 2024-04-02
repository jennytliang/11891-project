from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
	Include these tokens in the code: to _ int = {' zero ':
	"""

    # Split the string into a list of words
    words = numbers.split()

    # Create a list to store the sorted words
    sorted_words: List[str] = []

    # Create a list to store the number values
    values: List[int] = []

    # Loop through the list of words
    for word in words:
        # Check if the word is a number
        if word in int:
            # Add the number value to the values list
            values.append(int[word])
        # If the word is not a number, add it to the sorted words list
        else:
            sorted_words.append(word)

    # Sort the values list
    values.sort()

    # Loop through the values list
    for value in values:
        # Loop through the sorted words list
        for word in sorted_words:
            # If the value is less than the word, add it to the start of the sorted words list
            if value < int[word]:
                sorted_words.insert(0, word)
                break
            # If the value is greater than or equal to the word, add it to the end of the sorted words list
            elif value >= int[word]:
                sorted_words.append(word)

    # Return the sorted words
    return ' '.join(sorted_words)


if __name__ == "__main__":
    print(sort_numbers("one five three"))
