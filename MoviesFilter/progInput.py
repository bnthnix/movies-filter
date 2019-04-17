# Get and validate user selection.
def getSortSel():
    user_input = input("Selection: ")
    while (user_input != "A" and user_input != "a" and
           user_input != "B" and user_input != "b" and
           user_input != "C" and user_input != "c" and
           user_input != "D" and user_input != "d" and
           user_input != "S" and user_input != "s" and
           user_input != "Q" and user_input != "q"):
        print("Error! Try again!")
        user_input = input("Selection: ")
    return user_input


# Get user to input file name and validate it.
def getFileName():
    user_input = input("Please enter your file name: ")
    while user_input == "":
        print("Error! Try again!")
        user_input = input("Please enter your file name: ")
    return user_input


# Get user to input genre or month and validate it based on data in list.
def getGenreOrDate(whatever_list, string):
    # The try and except thing is not being taught in lecture.
    while True:
        user_input = input("Please enter %s: " % string)
        try:
            # Try if user input is integer.
            user_input = int(user_input)
            # Limit input range based on number of elements inside the list.
            if user_input < 1 or user_input > len(whatever_list):
                print("Error! Try again!")
            else:
                break
        except ValueError:
            # Error won't appear if the error is ValueError.
            # Run if user input is not integer.
            print("Please input a number!")
    # Replace user input with value inside list.
    user_input = whatever_list[user_input - 1]
    return user_input


# Get user to input rating and validate it.
def getRating():
    # The try and except thing is not being taught in lecture.
    while True:
        user_input = input("Please enter rating (from 0 to 10): ")
        try:
            # Try if user input is float.
            user_input = float(user_input)
            if user_input < 0 or user_input > 10:
                print("Error! Try again!")
            else:
                break
        except ValueError:
            # Error won't appear if the error is ValueError.
            # Run if user input is not integer.
            print("Please input a number!")
    return user_input


# Get user to input Y or N and validate it.
def getRestart():
    user_input = input("Do you want to restart the program? (Y/N): ")
    while (user_input != "Y" and user_input != "N"
           and user_input != "y" and user_input != "n"):
        print("Error! Try again!")
        user_input = input("Do you want to restart the program? (Y/N): ")

    if user_input == "Y" or user_input == "y":
        return True
    else:
        return False
