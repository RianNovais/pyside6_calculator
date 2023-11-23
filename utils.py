#there will be some functions that will be important for our code, such as some checks etc.

import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

# function that receives a text, and if it is a number from 0 to 9 or a dot (.) it will return False, otherwise True
def isNumOrDot(string: str):
    return bool(NUM_OR_DOT_REGEX.search(string))

#function that receives a text, and if it is a number from 0 to 9 or a dot (.) it will return False, otherwise True
def isValidNumber(text):
    valid = False
    try:
        float(text)
        valid = True
    except ValueError:
        valid = False

    return valid

#check if the passed value is empty
def isEmpty(string: str):
    return len(string) == 0