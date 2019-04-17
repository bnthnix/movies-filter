# Print welcome banner from text file.
# Printing from file is better as program owner \
# Can change the design easily as they want to.
def welcomeBanner():
    from datetime import datetime
    # Import datetime to get the date when using this program
    file = open("Display\\welcomeBanner.txt", "r")
    print(file.read())
    file.close()
    now = datetime.now()
    print("Today's Date:", now.strftime("%Y-%m-%d"))


# Print user selection.
def userSelection():
    print("\nPlease select one from ways of filter movies:")
    print("Enter [A] to filter based on Genre.")
    print("Enter [B] to filter based on Rating.")
    print("Enter [C] to filter based on Year.")
    print("Enter [D] to filter based on Month.")
    print("Enter [S] to store sort result into text file.")
    print("Enter [Q] to quit the program.")


# Print Genre/Year/Month from text file.
# Printing from file is better as program owner \
# Can change the design easily as they want to.
def printMenu(sortType):
    file = open("Display\\{}.txt".format(sortType), "r")
    print(file.read())
    file.close()


# Print Quit Banner from text file.
# Printing from file is better as program owner \
# Can change the design easily as they want to.
def quitBanner():
    file = open("Display\\quitBanner.txt", "r")
    print(file.read())
    file.close()
    input("Press any key to quit the program...")


# Print movie list after sorting process.
def printSorted(movie_list):
    print("\nBelow are the movies after the sorting process:")
    y = 1
    for x in movie_list:
        print(str(y) + ". " + x["name"])
        y += 1


# Print sorting process.
def printProcess(process_list):
    print("\nYour sorting process:")
    y = 1
    for x in process_list:
        for k in x:
            print(str(y) + ". " + k + ": " + str(x[k]))
        y += 1


# Print some random string.
def printString(index):
    string = ["You are yet to do any sorting!",
              "\nThere is no movie left based on your sorting options.\n"]
    print(string[index])
