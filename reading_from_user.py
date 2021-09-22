def read_nonempty_string(prompt):
    while True:
        s = input(prompt)
        s_with_no_spaces = s.replace(' ', '')
        if len(s_with_no_spaces) > 0 :
            break
        else:
            print("Please type letters only")
    return s

def read_nonempty_alphabetical_string(prompt):
    something_is_wrong = True
    while something_is_wrong:
        s = input(prompt)
        copy_without_spaces = s.replace(" ", "")
        if len(s) > 0 and copy_without_spaces.isalpha():
            something_is_wrong = False
        else:
            print("Letters only please...")
    return s


def read_positive_integer(prompt):
    something_is_wrong= True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            something_is_wrong = number <= 0
            if number <= 0:
                print("Number must be positive")
        except:
            print("Must be numeric...")
    return number


def read_integer(prompt):
    something_is_wrong= True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            something_is_wrong = False
        except:
            print("Must be numeric...")
    return number


def read_range_integer(prompt, min_range, max_range):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if min_range <= number <= max_range:
                something_is_wrong = False
            else:
                print("Values out of range...please try again...")
        except:
            print("Must be numeric...")
    return number

def read_nonnegative_integer(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def read_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            something_is_wrong = False
        except:
            print("Must be numeric...")
    return number


def read_nonnegative_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number


def read_range_float(prompt, min_range, max_range):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            if min_range <= number <= max_range:
                something_is_wrong = False
            else:
                print("Values out of range...please try again...")
        except:
            print("Must be numeric...")
    return number


def read_percentage_float(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = float(input(prompt))
            if 100 >= number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number
